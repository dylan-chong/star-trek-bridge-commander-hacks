import math
import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

BUG_DRONE_COOLDOWN_S = 12
BUG_DRONE_HP = 50
BUG_DRONE_NAME_PREFIX = 'Ram'
EACH_N_DRONE_IS_BEEFY = 8
BUG_BEEFY_DRONE_NAME_PREFIX = 'BeefyRam'
BUG_BEEFY_DRONE_SCALE = 1.5
BUG_BEEFY_DRONE_SPEED_MULT = 0.5

ET_DECREMENT_BUFFED_REPAIR_POINTS = App.UtopiaModule_GetNextEventType()
ET_RECORD_RAMMER_HEALTH = App.UtopiaModule_GetNextEventType()

SCALE_BOOST = 0.1
DAMAGE_FROM_SCALE_MULT = 1.0

def Initialize(OverrideExisting):
	global Cooldown, RammerNames, RecordHealthTimerId
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(BUG_DRONE_COOLDOWN_S)
	RammerNames = []

	Custom.CrazyShipAbilities.Utils.ReregisterEventHanders([
		(App.ET_OBJECT_COLLISION, 'ObjectCollisionHandler'),
		(App.ET_WEAPON_HIT, 'WeaponHitHandler'),
		(ET_DECREMENT_BUFFED_REPAIR_POINTS, 'RepairBoostFinished'),
		(ET_RECORD_RAMMER_HEALTH, 'RecordRammerHealth'),
	], App.Game_GetCurrentGame(), __name__)

    if RecordHealthTimerId:
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

def RecordRammerHealth(_pObject, _pEvent):
    global LastRammerHealth
    if not IsPlayerRammer():
        return

    hull = pPlayer.GetHull()
    if not hull:
    LastRammerHealth = hull.GetCondition()

def ObjectCollisionHandler(pObject, pEvent):
	source = App.ShipClass_Cast(pEvent.GetSource())
	target = App.ShipClass_Cast(pEvent.GetDestination())

    if not Custom.CrazyShipAbilities.Utils.IsPlayer(source):
        return

    import MissionLib
    player = MissionLib.GetPlayer()
    hull = player.GetHull()
    healthDifference = LastRammerHealth - hull.GetCondition()

    hull.SetCondition(LastRammerHealth)

def WeaponHitHandler(pObject, pEvent):
	target = App.ShipClass_Cast(pEvent.GetTargetObject())
	firing = App.ShipClass_Cast(pEvent.GetFiringObject())

    if not Custom.CrazyShipAbilities.Utils.IsPlayer(target):
        return
    if not pEvent.IsHullHit():
        return

    extraDamage = pEvent.GetDamage() *
    Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER - 1

    hull = target.GetHull()
    hull.SetCondition(hull.GetCondition() - extraDamage)

def RepairBoostFinished(_pObject, _pEvent):
    player = App.Game_GetCurrentPlayer()
    if not player:
        return

    # TODO NEXT damage boost and scale
    player.SetScale(player.GetScale() - SCALE_BOOST)
	Custom.CrazyShipAbilities.Utils.ChangePlayerRepairPointsBy(-5000)

def IsPlayerRammer():
	return 'BugRammer' == Custom.CrazyShipAbilities.Utils.GetPlayerShipType()
