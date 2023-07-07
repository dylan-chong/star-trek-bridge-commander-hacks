import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

MAX_NUKES_PER_PERIOD = 3
NUKE_COOLDOWN_PERIOD = 24
NUKE_PREFIX = '42km Nuke'


def Reset():
    global Cooldown, NukeNamesAndSpawnTimes
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

def CanLaunchNextNuke():
	now = App.g_kUtopiaModule.GetGameTime()
	nNukesLaunchedInPeriod = 0

	for (NukeName, NukeSpawnTime) in NukeNamesAndSpawnTimes:
		if NukeSpawnTime + SHUTTLE_NUKE_COOLDOWN_PERIOD >= now:
			nNukesLaunchedInPeriod = nNukesLaunchedInPeriod + 1

	return nNukesLaunchedInPeriod < MAX_NUKES_PER_PERIOD
