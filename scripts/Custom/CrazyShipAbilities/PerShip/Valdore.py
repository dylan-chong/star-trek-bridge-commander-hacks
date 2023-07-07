import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

WALL_COOLDOWN_S = 8
MAX_SIMULTANEOUS_WALLS = 1
WALL_LIFETIME_S = WALL_COOLDOWN_S * MAX_SIMULTANEOUS_WALLS - 1 # TODO this only applies when spawning a new wall


def Reset():
    global Cooldown, WallNamesAndSpawnTimes
    Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(WALL_COOLDOWN_S)
	WallNamesAndSpawnTimes = []

def GetTitle():
    return 'Wall'

def GetRemainingCooldown():
    return Cooldown.GetRemainingCooldown()

def UseAbility(pPlayer):
    if not Cooldown.IsReady():
        return

    Cooldown.Trigger()

    target = pPlayer.GetTarget()
    if not target:
        return

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

