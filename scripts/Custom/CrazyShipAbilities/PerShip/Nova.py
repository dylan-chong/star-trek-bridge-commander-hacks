import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

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



def Reset():
	global Cooldown, DroneNames, LastSpawnDroneTime, DroneSpawnTimes, enemyGroup, LastBoostTime
	DroneNames = []
	LastSpawnDroneTime = 0
	DroneSpawnTimes = []
	enemyGroup = None
    Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(NUKE_COOLDOWN_PERIOD)
	NukeNamesAndSpawnTimes = []

def GetTitle():
    return 'Dash'

def GetRemainingCooldown():
    return Cooldown.GetRemainingCooldown()

def UseAbility(pPlayer):
    if not Cooldown.IsReady():
        return

    Cooldown.Trigger()

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
        SetSameVelocityAndDirectionAsPlayer(pShip, pPlayer)

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
