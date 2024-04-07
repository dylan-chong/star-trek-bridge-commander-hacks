"""
BugRammer - highly maneuverable ship that uses collisions as it's primary attack method.
Upon colliding with a ship with sufficient speed, does damage to the enemy ship, and any damage done to the rammer itself is reversed.
Healing over a short time is also triggered, and also the rammer is increased in size temporarily to increase speed and collision damage.

Damage done to the shields is bled-through as a balancing mechanism.
The rammer can collide with enemies to heal and offset this damage, therefore allowing this ship to fulfill the role as a tank.
"""

import math
import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils
import Custom.CrazyShipAbilities.Constants

BUG_DRONE_SPAWN_DISTANCE = 100
BUG_DRONE_COOLDOWN_S = 10.5
BUG_DRONE_HP = 150
BUG_DRONE_NAME_PREFIX = 'Ram'
BUG_DRONE_SCALE = 1.2
EACH_N_DRONE_IS_BEEFY = 8
BUG_BEEFY_DRONE_HP = 20000
BUG_BEEFY_DRONE_NAME_PREFIX = 'BeefyRam'
BUG_BEEFY_DRONE_SCALE = 3.0
BUG_BEEFY_DRONE_SPEED_MULT = 0.8

def Initialize(OverrideExisting):
	global Cooldown, RammerNames
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(BUG_DRONE_COOLDOWN_S)
	RammerNames = []

def GetTitle():
	return 'Spawn Ram'

def GetCooldownS():
	return Cooldown.GetCooldownS()

def GetNReady():
	return Cooldown.GetNReady()

def GetNCooldowns():
	return Cooldown.GetNCooldowns()

# TODO this old function needs a refactor. Could simply remove as it seems to cause the ship to be overpowered.
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
				BUG_DRONE_SPAWN_DISTANCE,
				pPlayer,
				group = MissionLib.GetMission().GetNeutralGroup()
			)

			if isBeefyDrone:
				pNewShip.SetScale(BUG_BEEFY_DRONE_SCALE)
				pNewShip.SetMass(2000)
				# Scaling the ship also scales up the speed for some reason
				pNewShip.GetImpulseEngineSubsystem().SetPowerPercentageWanted(1.0 / BUG_BEEFY_DRONE_SCALE * BUG_BEEFY_DRONE_SPEED_MULT)
				pNewShip.DamageSystem(pNewShip.GetHull(), pNewShip.GetHull().GetMaxCondition() - BUG_BEEFY_DRONE_HP)
				pNewShip.GetHull().GetProperty().SetMaxCondition(BUG_BEEFY_DRONE_HP)
			else:
				pNewShip.SetMass(50)
				pNewShip.SetScale(BUG_DRONE_SCALE)
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

			vZero = App.TGPoint3()
			vZero.SetXYZ(0.0, 0.0, 0.0)
			pShip.SetVelocity(target.GetVelocityTG())
			pShip.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
		else:
			pShip.SetAI(None)

def SetShipKamazakeAI(pShip, targetName):
	pKamakaze = App.PlainAI_Create(pShip, 'MoveIn')
	pKamakaze.SetScriptModule('Ram')
	pKamakaze.SetInterruptable(1)
	pScript = pKamakaze.GetScriptInstance()
	pScript.SetTargetObjectName(targetName)
	pShip.SetAI(pKamakaze)