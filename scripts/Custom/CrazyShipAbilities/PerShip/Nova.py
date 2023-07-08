import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

DRONE_PREFIX = "Drone"
BEEFY_DRONE_PREFIX = "BeefyDrone"
DUD_DRONE_PREFIX = "DudDrone"
MAX_DRONES_IN_PERIOD = 2
DRONE_COOLDOWN_S = 6
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

def Reset():
	global Cooldown, DroneNames, LastSpawnDroneTime, DroneSpawnTimes, EnemyGroup, LastBoostTime
	DroneNames = []
	LastSpawnDroneTime = 0
	DroneSpawnTimes = []
	EnemyGroup = None
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(DRONE_COOLDOWN_S)

def GetTitle():
	return 'Drone'

def GetCooldownS():
	return Cooldown.GetCooldownS()

def GetNReady():
	return Cooldown.GetNReady()

def GetNCooldowns():
	return Cooldown.GetNCooldowns()

def UseAbility(pPlayer):
	if not Cooldown.IsReady():
		return

	Cooldown.Trigger()

	global LastSpawnDroneTime, DroneSpawnTimes, DroneNames

	velocity = pPlayer.GetVelocityTG()
	velocity.Scale(18)
	pPlayer.SetVelocity(velocity)

	for i in range(0, MAX_DRONES_IN_PERIOD):
		DroneSpawnTimes.append(App.g_kUtopiaModule.GetGameTime())

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

		shipName = Custom.CrazyShipAbilities.Utils.GenChildShipName(shipNamePrefix, len(DroneNames), pPlayer)
		DroneNames.append(shipName)

		if shipType == 'Transport':
			distance = SPAWN_DISTANCE
		else:
			distance = SPAWN_DISTANCE * 2

		SetEnemyGroup(pPlayer)
		import MissionLib
		pShip = Custom.CrazyShipAbilities.Utils.SpawnDroneShip(
			shipType,
			shipName,
			distance,
			pPlayer,
			group = MissionLib.GetMission().GetFriendlyGroup()
		)
		Custom.CrazyShipAbilities.Utils.SetSameVelocityAndDirectionAsPlayer(pShip, pPlayer)

		dynamicGroup = App.ObjectGroup_FromModule(__name__, "EnemyGroup")
		import QuickBattle.QuickBattleFriendlyAI
		try:
			pAI = QuickBattle.QuickBattleFriendlyAI.CreateDroneAI(pShip, groupToAttack = dynamicGroup)
			pShip.SetAI(pAI)
		except:
			print('Failed to create AI. Probably because there isnt any enemy ships yet or something')

def SetEnemyGroup(pPlayer):
	global EnemyGroup
	
	if not EnemyGroup:
		EnemyGroup = App.ObjectGroup()
	EnemyGroup.RemoveAllNames()
	target = Custom.CrazyShipAbilities.Utils.GetCurrentTarget(pPlayer)
	if target:
		EnemyGroup.AddName(target.GetName())