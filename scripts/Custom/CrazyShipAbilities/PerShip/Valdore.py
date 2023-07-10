import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

WALL_COOLDOWN_S = 8
MAX_SIMULTANEOUS_WALLS = 1
WALL_LIFETIME_S = WALL_COOLDOWN_S * MAX_SIMULTANEOUS_WALLS - 1 # TODO this only applies when spawning a new wall


def Initialize(OverrideExisting):
	global Cooldown, WallNamesAndSpawnTimes
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(WALL_COOLDOWN_S)
	WallNamesAndSpawnTimes = []

def GetTitle():
	return 'Wall'

def GetCooldownS():
	return Cooldown.GetCooldownS()

def GetNReady():
	return Cooldown.GetNReady()

def GetNCooldowns():
	return Cooldown.GetNCooldowns()

def UseAbility(pPlayer):
	import MissionLib

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

	shipName = Custom.CrazyShipAbilities.Utils.GenChildShipName('Wall', len(WallNamesAndSpawnTimes), pPlayer)

	pShip = Custom.CrazyShipAbilities.Utils.SpawnDroneShip(
		'Wall',
		shipName,
		distance=0.0,
		pPlayer=pPlayer,
		group = MissionLib.GetMission().GetNeutralGroup()
	)
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

	perpendicular = Custom.CrazyShipAbilities.Utils.GetAnyPerpendicularVector(direction, pPlayer)
	pShip.AlignToVectors(
		Custom.CrazyShipAbilities.Utils.Unitized(direction),
		Custom.CrazyShipAbilities.Utils.Unitized(perpendicular)
	)

	WallNamesAndSpawnTimes.append((shipName, App.g_kUtopiaModule.GetGameTime()))

