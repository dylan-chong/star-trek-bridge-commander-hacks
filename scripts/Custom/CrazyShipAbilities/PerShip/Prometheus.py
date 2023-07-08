import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

DASHBACK_COOLDOWN_S = 16

def Reset():
	global Cooldown
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(DASHBACK_COOLDOWN_S)
	pass

def GetTitle():
	return 'Dashback'

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

	dashbackVelocity = Custom.CrazyShipAbilities.Utils.Unitized(pPlayer.GetWorldForwardTG())
	dashbackVelocity.Scale(Custom.CrazyShipAbilities.Utils.KphToInternalGameSpeed(-250000))

	newVelocity = pPlayer.GetVelocityTG()
	newVelocity.Add(dashbackVelocity)
	pPlayer.SetVelocity(newVelocity)
