import App
import Custom.CrazyShipAbilities.Abilities

ET_REFRESH_USE_ABILITY = App.Game_GetNextEventType()

g_bHasSetUpRefreshAbilityTimer = 0
g_pAbilityButton = None

def ButtonCreated(button):
    global g_pAbilityButton
    g_pAbilityButton = button

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
    g_pAbilityButton.SetName(GetAbilityButtonTitle())

def UseAbility(_pObject, _pEvent):
    Custom.CrazyShipAbilities.Abilities.UseAbility()

def GetAbilityButtonTitle():
    if Custom.CrazyShipAbilities.Abilities.IsAvailable():
        return App.TGString('No ability available')

    nCooldowns = Custom.CrazyShipAbilities.Abilities.GetNCooldowns()

    if nCooldowns == 1:
        return GetButtonTitleForSingleCooldown()
    
    return GetButtonTitleForCompoundCooldown(nCooldowns)

def GetButtonTitleForSingleCooldown():
    title = Custom.CrazyShipAbilities.Abilities.GetTitle()
    cooldownS = Custom.CrazyShipAbilities.Abilities.GetCooldownS()

    if cooldownS == 0:
        return App.TGString(title + ' (Ready)')
    else:
        return App.TGString(title + ' (' + FormatCooldownS(cooldownS) + 's)')

def GetButtonTitleForCompoundCooldown(nCooldowns):
    title = Custom.CrazyShipAbilities.Abilities.GetTitle()
    nReady = Custom.CrazyShipAbilities.Abilities.GetNReady()

    if nReady == nCooldowns:
        return App.TGString(title + ' (' + nCooldowns + '/' + nCooldowns + ')')
    else:
        s = Custom.CrazyShipAbilities.Abilities.GetCooldownS()
        return App.TGString(title + ' (' + nReady + '/' + nCooldowns + ') (' + s + ')')

def FormatCooldownS(cooldownS):
    import math
    return str(int(math.ceil(cooldownS))) + 's'