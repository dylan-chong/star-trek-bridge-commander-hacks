import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

DASHBACK_COOLDOWN_S = 20 # same as AAAAAAAAATorpReloadDelay scripts\ships\Hardpoints\Prometheus.py

def Initialize(OverrideExisting):
	global Cooldown
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return 
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(DASHBACK_COOLDOWN_S)

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
