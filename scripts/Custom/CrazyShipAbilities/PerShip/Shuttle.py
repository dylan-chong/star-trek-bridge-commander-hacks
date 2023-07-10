import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

MAX_NUKES_PER_PERIOD = 3
NUKE_COOLDOWN_PERIOD = 24
NUKE_PREFIX = '42km Nuke'

def Initialize(OverrideExisting):
	global Cooldown, NukeNames
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.ParallelCooldown(NUKE_COOLDOWN_PERIOD, MAX_NUKES_PER_PERIOD)
	NukeNames = []

def GetTitle():
	return 'Nuke'

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

	shipName = Custom.CrazyShipAbilities.Utils.GenChildShipName(NUKE_PREFIX, len(NukeNames), pPlayer)
	NukeNames.append(shipName)

	import MissionLib
	nuke = Custom.CrazyShipAbilities.Utils.SpawnDroneShip(
		'Probe',
		shipName,
		0,
		pPlayer,
		group = MissionLib.GetMission().GetNeutralGroup()
	)
	nuke.EnableCollisionsWith(pPlayer, 0)
	nuke.SetScale(200)

	# Allow the ship to drift
	nuke.GetImpulseEngineSubsystem().SetPowerPercentageWanted(0)
	nuke.GetShields().SetPowerPercentageWanted(0)

	originalPlayerVelocity = pPlayer.GetVelocityTG()

	nukeVelocity = Custom.CrazyShipAbilities.Utils.Unitized(pPlayer.GetWorldForwardTG())
	nukeVelocity.Scale(Custom.CrazyShipAbilities.Utils.KphToInternalGameSpeed(8000))

	playerVelocityKnockback = Custom.CrazyShipAbilities.Utils.Unitized(nukeVelocity)
	playerVelocityKnockback.Scale(-150)

	newPlayerVelocity = Custom.CrazyShipAbilities.Utils.CloneVector(playerVelocityKnockback)
	newPlayerVelocity.Add(originalPlayerVelocity)
	pPlayer.SetVelocity(newPlayerVelocity)

	nuke.SetVelocity(nukeVelocity)
	nuke.AlignToVectors(pPlayer.GetWorldForwardTG(), pPlayer.GetWorldUpTG())