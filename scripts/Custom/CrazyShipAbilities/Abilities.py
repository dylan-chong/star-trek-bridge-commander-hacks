import App
import loadspacehelper

import Custom.CrazyShipAbilities.PerShip.NoAbilities
import Custom.CrazyShipAbilities.PerShip.Prometheus

SHIP_TO_ABILITY_MODULES = {
	'Prometheus': Custom.CrazyShipAbilities.PerShip.Prometheus
}

DRONE_PREFIX = "Drone"
BEEFY_DRONE_PREFIX = "BeefyDrone"
DUD_DRONE_PREFIX = "DudDrone"
MAX_DRONES_IN_PERIOD = 2
PERIOD_S = 6
SPAWN_DISTANCE = 50
POSSIBLE_SHIPS = [
	"Rectangle",
	"Asteroid",
	"Nova",
	"Sabre",
	"Fighter",
	"Transport",
	"BugRammer"
]

DEFIANT_BOOST_COOLDOWN_S = 10
SCIMITAR_BOOST_COOLDOWN_S = 15
AKIRA_BOOST_COOLDOWN_S = 10
PROMETHEUS_BOOST_COOLDOWN_S = 16

BUG_DRONE_COOLDOWN_S = 12
BUG_DRONE_HP = 50
BUG_DRONE_NAME_PREFIX = 'Ram'
EACH_N_DRONE_IS_BEEFY = 8
BUG_BEEFY_DRONE_NAME_PREFIX = 'BeefyRam'
BUG_BEEFY_DRONE_SCALE = 1.5
BUG_BEEFY_DRONE_SPEED_MULT = 0.5

VALDORE_WALL_COOLDOWN_S = 8
VALDORE_MAX_SIMULTANEOUS_WALLS = 1
WALL_LIFETIME_S = VALDORE_WALL_COOLDOWN_S * VALDORE_MAX_SIMULTANEOUS_WALLS - 1 # TODO this only applies when spawning a new wall

MAX_NUKES_PER_PERIOD = 3
SHUTTLE_NUKE_COOLDOWN_PERIOD = 24
NUKE_PREFIX = '42km Nuke'

def Reset():
	global DroneNames, LastSpawnDroneTime, DroneSpawnTimes, enemyGroup, LastBoostTime, WallNamesAndSpawnTimes, RammerNames, NukeNamesAndSpawnTimes
	DroneNames = []
	LastSpawnDroneTime = 0
	DroneSpawnTimes = []
	enemyGroup = None
	LastBoostTime = -999999999
	WallNamesAndSpawnTimes = []
	RammerNames = []
	NukeNamesAndSpawnTimes = []

	for mod in SHIP_TO_ABILITY_MODULES.values():
		mod.Reset()

Reset()

def GetRemainingCooldown(): 
	return GetAbilityModule().GetRemainingCooldown()

def GetTitle(): 
	# TODO NEXT implement title
	# TODO AFTER fix the defiant next
	return GetAbilityModule().GetTitle()

def UseAbility():
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	return GetAbilityModule().UseAbility(pPlayer)

	import MissionLib
	global LastBoostTime
	global NDrones
	
	if pPlayer.GetShipProperty().GetName().GetCString() == 'Defiant':
		if LastBoostTime + DEFIANT_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
			velocity = pPlayer.GetVelocityTG()
			velocity.Scale(10) 
			pPlayer.SetVelocity(velocity)
			LastBoostTime = App.g_kUtopiaModule.GetGameTime()

	if pPlayer.GetShipProperty().GetName().GetCString() == 'Scimitar':
		if LastBoostTime + SCIMITAR_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
			velocity = pPlayer.GetVelocityTG()
			velocity.Scale(20) 
			pPlayer.SetVelocity(velocity)
			LastBoostTime = App.g_kUtopiaModule.GetGameTime()

	if pPlayer.GetShipProperty().GetName().GetCString() == 'Akira':
		if LastBoostTime + AKIRA_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
			velocity = pPlayer.GetVelocityTG()
			velocity.Scale(40)
			pPlayer.SetVelocity(velocity)
			LastBoostTime = App.g_kUtopiaModule.GetGameTime()
		
	if pPlayer.GetShipProperty().GetName().GetCString() == 'Prometheus':
		if LastBoostTime + PROMETHEUS_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
			knockbackVelocity = Unitized(pPlayer.GetWorldForwardTG())
			knockbackVelocity.Scale(kphToInternalGameSpeed(-250000))

			newVelocity = pPlayer.GetVelocityTG()
			newVelocity.Add(knockbackVelocity)
			pPlayer.SetVelocity(newVelocity)

			LastBoostTime = App.g_kUtopiaModule.GetGameTime()

	if pPlayer.GetShipProperty().GetName().GetCString() == 'Valdore':
		global WallNamesAndSpawnTimes
		if LastBoostTime + VALDORE_WALL_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
			LastBoostTime = App.g_kUtopiaModule.GetGameTime()
			# Not actually boost
			
			target = pPlayer.GetTarget()
			if target:
				global WallNamesAndSpawnTimes, WALL_LIFETIME_S

				for (wallName, spawnTime) in WallNamesAndSpawnTimes:
					if spawnTime + WALL_LIFETIME_S > App.g_kUtopiaModule.GetGameTime():
						continue
				
					wall = MissionLib.GetShip(wallName)
					if not wall:
						continue

					wall.SetScale(0.001)
					wall.SetInvincible(0)
					
					pSystem = wall.GetHull()
					pSystem.SetConditionPercentage(0)

				shipName = GenChildShipName('Wall', len(WallNamesAndSpawnTimes), pPlayer)
				
				pShip = SpawnDroneShip('Wall', shipName, distance=0.0, pPlayer=pPlayer, group = MissionLib.GetMission().GetNeutralGroup())
				pShip.SetScale(25)
				pShip.SetInvincible(1)
				pShip.SetCollisionsOn(0)

				direction = target.GetWorldLocation()
				direction.Subtract(pPlayer.GetWorldLocation())
				direction.Scale(0.75)
				
				betweenPoint = App.TGPoint3()
				betweenPoint.Set(pPlayer.GetWorldLocation())
				betweenPoint.Add(direction)

				pShip.SetTranslate(betweenPoint)

				perpendicular = GetAnyPerpendicularVector(direction, pPlayer)
				pShip.AlignToVectors(Unitized(direction), Unitized(perpendicular))

				WallNamesAndSpawnTimes.append((shipName, App.g_kUtopiaModule.GetGameTime()))

	if pPlayer.GetShipProperty().GetName().GetCString() == 'BugRammer':
		global RammerNames
		target = GetCurrentTarget(pPlayer)
		targetName = target and target.GetName() or None

		if LastBoostTime + BUG_DRONE_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
			velocity = pPlayer.GetVelocityTG()
			velocity.Scale(1.6)
			pPlayer.SetVelocity(velocity)
		
			LastBoostTime = App.g_kUtopiaModule.GetGameTime()
			
			if targetName:
				isBeefyDrone = len(RammerNames) % EACH_N_DRONE_IS_BEEFY == EACH_N_DRONE_IS_BEEFY - 1

				newShipNamePrefix = isBeefyDrone and BUG_BEEFY_DRONE_NAME_PREFIX or BUG_DRONE_NAME_PREFIX
				newShipName = GenChildShipName(newShipNamePrefix, len(RammerNames), pPlayer)

				SetEnemyGroup(pPlayer)
				pNewShip = SpawnDroneShip('BugRammer', newShipName, 30, pPlayer, group = MissionLib.GetMission().GetNeutralGroup())

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
			if not target:
				pShip.SetAI(None)

			SetShipKamazakeAI(pShip, targetName)

			AlignShipToFaceTarget(pShip, target)

			vZero = App.TGPoint3()
			vZero.SetXYZ(0.0, 0.0, 0.0)
			pShip.SetVelocity(target.GetVelocityTG())
			pShip.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

	if pPlayer.GetShipProperty().GetName().GetCString() == 'Shuttle':
		if CanLaunchNextNuke():
			global NNukes
			shipName = GenChildShipName(NUKE_PREFIX, len(NukeNamesAndSpawnTimes), pPlayer)
			NukeNamesAndSpawnTimes.append((shipName, App.g_kUtopiaModule.GetGameTime()))

			nuke = SpawnDroneShip('Probe', shipName, 0, pPlayer, group = MissionLib.GetMission().GetNeutralGroup())
			nuke.EnableCollisionsWith(pPlayer, 0)
			nuke.SetScale(200)

			# Allow the ship to drift
			nuke.GetImpulseEngineSubsystem().SetPowerPercentageWanted(0)
			nuke.GetShields().SetPowerPercentageWanted(0)

			originalPlayerVelocity = pPlayer.GetVelocityTG()

			nukeVelocity = Unitized(pPlayer.GetWorldForwardTG())
			nukeVelocity.Scale(kphToInternalGameSpeed(8000))

			playerVelocityKnockback = Unitized(nukeVelocity)
			playerVelocityKnockback.Scale(-150)

			newPlayerVelocity = CloneVector(playerVelocityKnockback)
			newPlayerVelocity.Add(originalPlayerVelocity)
			pPlayer.SetVelocity(newPlayerVelocity)

			nuke.SetVelocity(nukeVelocity)
			nuke.AlignToVectors(pPlayer.GetWorldForwardTG(), pPlayer.GetWorldUpTG())

	if pPlayer.GetShipProperty().GetName().GetCString() == 'Nova':
		global LastSpawnDroneTime, DroneSpawnTimes, MAX_DRONES_IN_PERIOD, PERIOD_S, DroneNames

		for i in range(0, len(DroneSpawnTimes)):
			if DroneSpawnTimes[0] + PERIOD_S < App.g_kUtopiaModule.GetGameTime():
				del DroneSpawnTimes[0]

		# if time.clock() - LastSpawnDroneTime > 2:
		NDronesSpawned = 0
		while len(DroneSpawnTimes) < MAX_DRONES_IN_PERIOD :
			DroneSpawnTimes.append(App.g_kUtopiaModule.GetGameTime())
			NDronesSpawned = NDronesSpawned + 1

			randomShipNum = App.g_kSystemWrapper.GetRandomNumber(100)
			shipNamePrefix = DRONE_PREFIX
			if randomShipNum < 2:
				shipType = "Rectangle"
				shipNamePrefix = BEEFY_DRONE_PREFIX
			elif randomShipNum < 9:
				shipType = "Asteroid"
				shipNamePrefix = DUD_DRONE_PREFIX
			elif randomShipNum < 15:
				shipType = "Nova"
			elif randomShipNum < 18:
				shipType = "Sabre"
				shipNamePrefix = BEEFY_DRONE_PREFIX
			elif randomShipNum < 47:
				shipType = "Fighter"
			else:
				shipType = "Transport"

			shipName = GenChildShipName(shipNamePrefix, len(DroneNames), pPlayer)
			DroneNames.append(shipName)

			if shipType == 'Transport':
				distance = SPAWN_DISTANCE
			else:
				distance = SPAWN_DISTANCE * 2

			SetEnemyGroup(pPlayer)
			pShip = SpawnDroneShip(shipType, shipName, distance, pPlayer, group = MissionLib.GetMission().GetFriendlyGroup())
			SetVelocityAndDirectionAsPlayer(pShip, pPlayer)

			dynamicGroup = App.ObjectGroup_FromModule("Bridge.XOMenuHandlers", "enemyGroup")
			import QuickBattle.QuickBattleFriendlyAI
			try:
				pAI = QuickBattle.QuickBattleFriendlyAI.CreateDroneAI(pShip, groupToAttack = dynamicGroup)
				pShip.SetAI(pAI)
			except:
				print('Failed to create AI. Probably because there isnt any enemy ships yet or something')

		if NDronesSpawned > 0:
			velocity = pPlayer.GetVelocityTG()
			velocity.Scale(18)
			pPlayer.SetVelocity(velocity)

def GetAbilityModule():
	pGame = App.Game_GetCurrentGame()
	pPlayer = App.ShipClass_Cast(pGame.GetPlayer())
	playerShipName = pPlayer.GetShipProperty().GetName().GetCString()

	mod = SHIP_TO_ABILITY_MODULES[playerShipName]
	if not mod:
		return Custom.CrazyShipAbilities.NoAbilities
	
	return mod

def GenChildShipName(prefix, i, pPlayer):
	return prefix + ' ' + str(i + 1) + ' (' + pPlayer.GetName() + ')'

def SpawnDroneShip(shipType, shipName, distance, pPlayer, group):
	import MissionLib
	pSetName = MissionLib.GetPlayerSet().GetName()
	pSet = App.g_kSetManager.GetSet(pSetName)

	pShip = loadspacehelper.CreateShip(shipType, pSet, shipName, None, 0, 1)

	kPoint = App.TGPoint3()
	kPoint.Set(pPlayer.GetWorldLocation())
	import math
	rads = (App.g_kSystemWrapper.GetRandomNumber(201) - 100) / 100.0 * 6.28
	
	XOff = distance * math.sin(rads)
	YOff = distance * math.cos(rads)
	kPoint.SetX(kPoint.GetX() + XOff)
	kPoint.SetY(kPoint.GetY() + YOff)
	kPoint.SetZ(kPoint.GetZ() + (App.g_kSystemWrapper.GetRandomNumber(201) - 100) / 100.0 * distance)
	pShip.SetTranslate(kPoint)

	group.AddName(shipName)
	
	return pShip

def SetVelocityAndDirectionAsPlayer(pShip, pPlayer):
	up = pPlayer.GetWorldUpTG()
	forward = pPlayer.GetWorldForwardTG()
	pShip.AlignToVectors(forward, up)

	pShip.SetVelocity(pPlayer.GetVelocityTG())

def SetEnemyGroup(pPlayer):
	global enemyGroup
	
	if not enemyGroup:
		enemyGroup = App.ObjectGroup()
	enemyGroup.RemoveAllNames()
	target = GetCurrentTarget(pPlayer)
	if target:
		enemyGroup.AddName(target.GetName())

def GetCurrentTarget(pPlayer):
	target = pPlayer.GetTarget()
	if target:
		castedTarget = App.ShipClass_Cast(target)
		if castedTarget:
			return castedTarget

	return None

def GetAnyPerpendicularVector(direction, anyShip):
	up = Unitized(anyShip.GetWorldUpTG())
	perp = Unitized(direction).UnitCross(up)

	if perp.Length() > 0.5: 
		return perp

	# direction must be equal to up, as cross product will return invalid result (0,0,0)
	forward = Unitized(anyShip.GetWorldForwardTG())
	return Unitized(direction).UnitCross(forward)

def AlignShipToFaceTarget(pShip, target):
	direction = target.GetWorldLocation()
	direction.Subtract(pShip.GetWorldLocation())
	perpendicular = GetAnyPerpendicularVector(direction, target)
	pShip.AlignToVectors(direction, perpendicular)

def SetShipKamazakeAI(pShip, targetName):
	pKamakaze = App.PlainAI_Create(pShip, 'MoveIn')
	pKamakaze.SetScriptModule('Ram')
	pKamakaze.SetInterruptable(1)
	pScript = pKamakaze.GetScriptInstance()
	pScript.SetTargetObjectName(targetName)
	pShip.SetAI(pKamakaze)

def CanLaunchNextNuke():
	now = App.g_kUtopiaModule.GetGameTime()
	nNukesLaunchedInPeriod = 0

	for (NukeName, NukeSpawnTime) in NukeNamesAndSpawnTimes:
		if NukeSpawnTime + SHUTTLE_NUKE_COOLDOWN_PERIOD >= now:
			nNukesLaunchedInPeriod = nNukesLaunchedInPeriod + 1

	return nNukesLaunchedInPeriod < MAX_NUKES_PER_PERIOD