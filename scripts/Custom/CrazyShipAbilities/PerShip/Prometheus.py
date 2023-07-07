import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

KNOCKBACK_COOLDOWN_S = 16

def Reset():
    global cooldown
    cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(KNOCKBACK_COOLDOWN_S)
    pass

def GetRemainingCooldown():
    return cooldown.GetRemainingCooldown()

def UseAbility(pPlayer):
    if not cooldown.IsReady():
        return

    cooldown.Trigger()
        
    knockbackVelocity = Custom.CrazyShipAbilities.Utils.Unitized(pPlayer.GetWorldForwardTG())
    knockbackVelocity.Scale(Custom.CrazyShipAbilities.Utils.KphToInternalGameSpeed(-250000))

    newVelocity = pPlayer.GetVelocityTG()
    newVelocity.Add(knockbackVelocity)
    pPlayer.SetVelocity(newVelocity)
