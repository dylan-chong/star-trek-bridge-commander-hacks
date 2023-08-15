import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

DASH_COOLDOWN_S = 12

def Initialize(OverrideExisting):
	global Cooldown
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(DASH_COOLDOWN_S)

def GetTitle():
	return 'Dash'

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

	velocity = pPlayer.GetVelocityTG()
	velocity.Scale(14)
	pPlayer.SetVelocity(velocity)
