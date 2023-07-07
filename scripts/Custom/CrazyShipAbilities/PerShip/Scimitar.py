import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

DASH_COOLDOWN_S = 15

def Reset():
	global Cooldown
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(DASH_COOLDOWN_S)

def GetTitle():
	return 'Dash'

def GetRemainingCooldown():
	return Cooldown.GetRemainingCooldown()

def UseAbility(pPlayer):
	if not Cooldown.IsReady():
		return

	Cooldown.Trigger()

	velocity = pPlayer.GetVelocityTG()
	velocity.Scale(20)
	pPlayer.SetVelocity(velocity)
