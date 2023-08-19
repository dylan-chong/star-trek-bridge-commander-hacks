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
MAX_SCALE_BOOST = 0.5
DAMAGE_BOOST_FROM_SCALE = 0.2

# 7.5 force is pretty normal for a impulse 6 impact (a pretty reasonable speed to get an impact)
BASE_RAM_DAMAGE_VELOCITY = 7.5
BASE_RAM_DAMAGE = 1200.0
# 20 force is pretty normal for a impulse 9 impact. Do triple damage
HIGH_RAM_DAMAGE_VELOCITY = 20.0
HIGH_RAM_DAMAGE = BASE_RAM_DAMAGE * 3.0
# Ram limits
MIN_RAM_DAMAGE_VELOCITY = 2.0
MIN_RAM_DAMAGE = 100
MAX_RAM_DAMAGE = BASE_RAM_DAMAGE * 4.0

MIN_COLLISION_PERIOD_S = 0.333

SHIELD_DAMAGE_BLEEDTHROUGH = 0.8

def Initialize(OverrideExisting):
	global Cooldown, RammerNames, Buffs, RecordHealthTimerId, LastUsedCollisionTime, LastRammerHealth
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(BUG_DRONE_COOLDOWN_S)
	RammerNames = []
	Buffs = []
	LastUsedCollisionTime = None
	LastRammerHealth = None

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

	ReversePlayerRammingDamage()
	RecordRammerHealth() # Prevent 2 close collisions from reverting healing

	if not target: return
	if not CanUseCollisionYet(): return
	SetCollisionUsed()

	damageDealt = DamageTarget(target, source)

	HealAndBuffFromDamageDealt(damageDealt)

def CanUseCollisionYet():
	if not LastUsedCollisionTime: return 1
	return App.g_kUtopiaModule.GetGameTime() > LastUsedCollisionTime + MIN_COLLISION_PERIOD_S

def SetCollisionUsed():
	global LastUsedCollisionTime
	LastUsedCollisionTime = App.g_kUtopiaModule.GetGameTime()

def WeaponHitHandler(pObject, pEvent):
	target = App.ShipClass_Cast(pEvent.GetTargetObject())
	if not Custom.CrazyShipAbilities.Utils.IsPlayer(target): return

	if pEvent.IsHullHit():
		damageMultiplier = Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER - 1
	else:
		damageMultiplier = SHIELD_DAMAGE_BLEEDTHROUGH * Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER

	DamageHull(damageMultiplier * pEvent.GetDamage(), target)

def DamageHull(damage, ship):
	hull = ship.GetHull()
	hull.SetCondition(hull.GetCondition() - damage)

def ReversePlayerRammingDamage():
	player = App.Game_GetCurrentPlayer()
	hull = player.GetHull()
	if not hull: return

	hull.SetCondition(LastRammerHealth)
	if hull.GetCondition() == hull.GetMaxCondition():
		player.RemoveVisibleDamage()

def DamageTarget(target, source):
	# Velocities are not the ramming velocities, but the bounce away velocities.
	# The bigger the ramming, the bigger the bounce away velocities.
	#
	# The reason we use the velocity diff between the two ships is because when the mass of the
	# rammer is small and the target big, the force on the collision event always is 0.
	# This would result in 0 damage being done to large ships.
	velocityDiff = Custom.CrazyShipAbilities.Utils.CloneVector(source.GetVelocityTG())
	velocityDiff.Subtract(target.GetVelocityTG())
	velocityLength = velocityDiff.Length()

	GRADIENT = (HIGH_RAM_DAMAGE - BASE_RAM_DAMAGE) / (HIGH_RAM_DAMAGE_VELOCITY - BASE_RAM_DAMAGE_VELOCITY)

	damage = GRADIENT * (velocityLength - BASE_RAM_DAMAGE_VELOCITY) + BASE_RAM_DAMAGE
	cappedDamage = max(MIN_RAM_DAMAGE, min(MAX_RAM_DAMAGE, damage))
	scaledDamage = cappedDamage + cappedDamage * (source.GetScale() - 1) * DAMAGE_BOOST_FROM_SCALE

	if velocityLength < MIN_RAM_DAMAGE_VELOCITY: return 0

	hull = target.GetHull()
	hull.SetCondition(hull.GetCondition() - scaledDamage)
	return scaledDamage

def HealAndBuffFromDamageDealt(damageDealt):
	if damageDealt == 0: return

	healing = CalcHealingBoost(damageDealt)
	scale = CalcScaleBoost(damageDealt)
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