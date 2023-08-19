import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils
import Custom.CrazyShipAbilities.Constants

BUG_DRONE_COOLDOWN_S = 12
BUG_DRONE_HP = 50
BUG_DRONE_NAME_PREFIX = 'Ram'
EACH_N_DRONE_IS_BEEFY = 8
BUG_BEEFY_DRONE_NAME_PREFIX = 'BeefyRam'
BUG_BEEFY_DRONE_SCALE = 1.5
BUG_BEEFY_DRONE_SPEED_MULT = 0.5
ET_STOP_BUFF = App.UtopiaModule_GetNextEventType()
ET_RECORD_RAMMER_HEALTH = App.UtopiaModule_GetNextEventType()

BUFF_DURATION_S = 6

HEALING_FROM_DAMAGE_FACTOR = 4.0 * Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER

MIN_SCALE_BOOST = 0.1
MAX_SCALE_BOOST = 0.8
DAMAGE_BOOST_FROM_SCALE = 0.2

# 1.8 force is pretty normal for a impulse 7 impact (a pretty reasonable speed to get an impact)
BASE_RAM_DAMAGE_FORCE = 1.8
BASE_RAM_DAMAGE = 1200.0
# 4.1 force is pretty normal for a impulse 9 impact. Do triple damage
HIGH_RAM_DAMAGE_FORCE = 4.1
HIGH_RAM_DAMAGE = BASE_RAM_DAMAGE * 3.0
# Ram limits
MIN_RAM_DAMAGE_FORCE = 0.01
MIN_RAM_DAMAGE = 200
MAX_RAM_DAMAGE = HIGH_RAM_DAMAGE

def Initialize(OverrideExisting):
	global Cooldown, RammerNames, Buffs, RecordHealthTimerId
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(BUG_DRONE_COOLDOWN_S)
	RammerNames = []
	Buffs = []

	Custom.CrazyShipAbilities.Utils.ReregisterEventHanders([
		(App.ET_OBJECT_COLLISION, 'ObjectCollisionHandler'),
		(App.ET_WEAPON_HIT, 'WeaponHitHandler'),
		(ET_STOP_BUFF, 'BuffFinished'),
		(ET_RECORD_RAMMER_HEALTH, 'RecordRammerHealth'),
	], App.Game_GetCurrentGame(), __name__)

	if 'RecordHealthTimerId' in globals().keys():
		App.g_kTimerManager.DeleteTimer(RecordHealthTimerId)
	RecordHealthTimerId = CreateHealthRecorderTimer()

def GetTitle():
	return 'Spawn Ram'

def GetCooldownS():
	return Cooldown.GetCooldownS()

def GetNReady():
	return Cooldown.GetNReady()

def GetNCooldowns():
	return Cooldown.GetNCooldowns()

def UseAbility(pPlayer):
	import MissionLib
	global RammerNames
	target = Custom.CrazyShipAbilities.Utils.GetCurrentTarget(pPlayer)
	targetName = target and target.GetName() or None

	if Cooldown.IsReady():
		Cooldown.Trigger()

		if targetName:
			isBeefyDrone = len(RammerNames) % EACH_N_DRONE_IS_BEEFY == EACH_N_DRONE_IS_BEEFY - 1

			newShipNamePrefix = isBeefyDrone and BUG_BEEFY_DRONE_NAME_PREFIX or BUG_DRONE_NAME_PREFIX
			newShipName = Custom.CrazyShipAbilities.Utils.GenChildShipName(newShipNamePrefix, len(RammerNames), pPlayer)

			pNewShip = Custom.CrazyShipAbilities.Utils.SpawnDroneShip(
				'BugRammer',
				newShipName,
				30,
				pPlayer,
				group = MissionLib.GetMission().GetNeutralGroup()
			)

			if isBeefyDrone:
				pNewShip.SetScale(BUG_BEEFY_DRONE_SCALE)
				pNewShip.SetMass(2000)
				# Scaling the ship also scales up the speed for some reason
				pNewShip.GetImpulseEngineSubsystem().SetPowerPercentageWanted(1.0 / BUG_BEEFY_DRONE_SCALE * BUG_BEEFY_DRONE_SPEED_MULT)
			else:
				pNewShip.SetMass(100)
				pNewShip.SetScale(0.8)
				pNewShip.DamageSystem(pNewShip.GetHull(), pNewShip.GetHull().GetMaxCondition() - BUG_DRONE_HP)
				pNewShip.GetHull().GetProperty().SetMaxCondition(BUG_DRONE_HP)

			pNewShip.EnableCollisionsWith(pPlayer, 0)

			for shipName in RammerNames:
				pExistingShip = MissionLib.GetShip(shipName)
				if not pExistingShip:
					continue
				pNewShip.EnableCollisionsWith(pExistingShip, 0)

			RammerNames.append(newShipName)

	for shipName in RammerNames:
		pShip = MissionLib.GetShip(shipName)
		if not pShip:
			continue

		if target:
			SetShipKamazakeAI(pShip, targetName)
			Custom.CrazyShipAbilities.Utils.AlignShipToFaceTarget(pShip, target)
		else:
			pShip.SetAI(None)

		vZero = App.TGPoint3()
		vZero.SetXYZ(0.0, 0.0, 0.0)
		pShip.SetVelocity(target.GetVelocityTG())
		pShip.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

def SetShipKamazakeAI(pShip, targetName):
	pKamakaze = App.PlainAI_Create(pShip, 'MoveIn')
	pKamakaze.SetScriptModule('Ram')
	pKamakaze.SetInterruptable(1)
	pScript = pKamakaze.GetScriptInstance()
	pScript.SetTargetObjectName(targetName)
	pShip.SetAI(pKamakaze)

def CreateHealthRecorderTimer():
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(ET_RECORD_RAMMER_HEALTH)
	pEvent.SetDestination(App.Game_GetCurrentGame())

	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 0.125)
	pTimer.SetDelay(0.125)
	pTimer.SetDuration(-1)
	pTimer.SetEvent(pEvent)
	return App.g_kTimerManager.AddTimer(pTimer)

def RecordRammerHealth(_pObject = None, _pEvent = None):
	global LastRammerHealth
	if not IsPlayerRammer(): return

	hull = App.Game_GetCurrentPlayer().GetHull()
	if not hull: return
	LastRammerHealth = hull.GetCondition()

def ObjectCollisionHandler(pObject, pEvent):
	source = App.ShipClass_Cast(pEvent.GetSource())
	target = App.ShipClass_Cast(pEvent.GetDestination())

	if not source or not Custom.CrazyShipAbilities.Utils.IsPlayer(source):
		return

	damageDealt = DamageTarget(target, pEvent.GetCollisionForce(), source)
	ReversePlayerRammingDamage()
	HealAndBuffFromDamageDealt(damageDealt)
	RecordRammerHealth() # Prevent 2 close collisions from reverting healing

def WeaponHitHandler(pObject, pEvent):
	target = App.ShipClass_Cast(pEvent.GetTargetObject())
	firing = App.ShipClass_Cast(pEvent.GetFiringObject())

	if not Custom.CrazyShipAbilities.Utils.IsPlayer(target): return
	if not pEvent.IsHullHit(): return

	extraDamage = pEvent.GetDamage() * Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER - 1

	hull = target.GetHull()
	hull.SetCondition(hull.GetCondition() - extraDamage)

def ReversePlayerRammingDamage():
	player = App.Game_GetCurrentPlayer()
	hull = player.GetHull()

	hull.SetCondition(LastRammerHealth)
	if hull.GetCondition() == hull.GetMaxCondition():
		player.RemoveVisibleDamage()

def DamageTarget(target, force, source):
	GRADIENT = (HIGH_RAM_DAMAGE - BASE_RAM_DAMAGE) / (HIGH_RAM_DAMAGE_FORCE - BASE_RAM_DAMAGE_FORCE)

	damage = GRADIENT * (force - BASE_RAM_DAMAGE_FORCE) + BASE_RAM_DAMAGE
	cappedDamage = max(MIN_RAM_DAMAGE, min(MAX_RAM_DAMAGE, damage))
	scaledDamage = cappedDamage * source.GetScale()

	if force < MIN_RAM_DAMAGE_FORCE: return 0

	hull = target.GetHull()
	hull.SetCondition(hull.GetCondition() - scaledDamage)
	return cappedDamage

def HealAndBuffFromDamageDealt(damageDealt):
	if damageDealt == 0: return

	healing = CalcHealingBoost(damageDealt)
	scale = CalcScaleBoost(damageDealt)
	print ('- buffing: ', (healing, scale))
	Buffs.insert(0, (healing, scale))

	ChangePlayerScale(scale)
	Custom.CrazyShipAbilities.Utils.ChangePlayerRepairPointsBy(healing)

	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_STOP_BUFF, BUFF_DURATION_S)

def CalcScaleBoost(damageDealt):
	GRADIENT = (MAX_SCALE_BOOST - MIN_SCALE_BOOST) / (MAX_RAM_DAMAGE - MIN_RAM_DAMAGE)
	return GRADIENT * (damageDealt - MIN_RAM_DAMAGE) + MIN_SCALE_BOOST

def CalcHealingBoost(damageDealt):
	REPAIR_TICKS_PER_SECOND = 3
	N_REPAIR_TICKS = BUFF_DURATION_S * REPAIR_TICKS_PER_SECOND

	totalHealing = damageDealt * HEALING_FROM_DAMAGE_FACTOR
	return totalHealing / N_REPAIR_TICKS

def BuffFinished(_pObject, _pEvent):
	if not App.Game_GetCurrentPlayer(): return
	if len(Buffs) == 0: return

	healing, scale = Buffs.pop()
	Custom.CrazyShipAbilities.Utils.ChangePlayerRepairPointsBy(-healing)
	ChangePlayerScale(-scale)

def IsPlayerRammer():
	return 'BugRammer' == Custom.CrazyShipAbilities.Utils.GetPlayerShipType()

def ChangePlayerScale(amount):
	player = App.Game_GetCurrentPlayer()
	player.SetScale(player.GetScale() + amount)