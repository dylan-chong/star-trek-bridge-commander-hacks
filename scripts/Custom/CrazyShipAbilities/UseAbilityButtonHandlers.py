import App
import Custom.CrazyShipAbilities.Abilities
import Custom.CrazyShipAbilities.PerShip.NoAbilities

ET_REFRESH_USE_ABILITY = App.Game_GetNextEventType()

g_bHasSetUpRefreshAbilityTimer = 0
g_pAbilityButton = None

def ButtonCreated(button):
    global g_pAbilityButton
    g_pAbilityButton = button

# TODO can you replace tactical menu with the button itself
def SetupUseAbilityRefreshTimer():
    global g_bHasSetUpRefreshAbilityTimer
    if g_bHasSetUpRefreshAbilityTimer:
        return
    g_bHasSetUpRefreshAbilityTimer = 1

    g_pAbilityButton.AddPythonFuncHandlerForInstance(ET_REFRESH_USE_ABILITY, __name__ + '.RefreshUseAbilityButton')

    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_REFRESH_USE_ABILITY)
    pEvent.SetDestination(g_pAbilityButton)

    pTimer = App.TGTimer_Create()
    pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 0.125)
    pTimer.SetDelay(0.125)
    pTimer.SetDuration(-1)
    pTimer.SetEvent(pEvent)
    App.g_kTimerManager.AddTimer(pTimer)

def RefreshUseAbilityButton(_pObject, _pEvent):
    g_pAbilityButton.SetName(GetNewAbilityButtonTitle())

def UseAbility(_pObject, _pEvent):
    Custom.CrazyShipAbilities.Abilities.UseAbility()


def GetNewAbilityButtonTitle():
    remainingCooldown = Custom.CrazyShipAbilities.Abilities.GetRemainingCooldown()
    title = Custom.CrazyShipAbilities.Abilities.GetTitle()

    if (remainingCooldown == Custom.CrazyShipAbilities.PerShip.NoAbilities.NO_ABILITIES_COOLDOWN):
        return App.TGString('No ability available')
    elif (remainingCooldown == 0):
        return App.TGString(title + ' (Ready)')
    else:
        import math
        cooldownString = str(int(math.ceil(remainingCooldown)))
        return App.TGString(title + ' (' + cooldownString + 's)')

    # nuke / compound
    # need: nAvailable, remainingCooldown, nCooldown
    # if none available
    #     show (remainingCooldown till next available)
    # if all available
    #     show ready (n/n)
    # if some available
    #     show ready (n/n)