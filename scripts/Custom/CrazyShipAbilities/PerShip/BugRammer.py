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

def Reset():
	global Cooldown, RammerNames
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(BUG_DRONE_COOLDOWN_S)
	RammerNames = []

def GetTitle():
	return 'Ram'

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