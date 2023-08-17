import App
import Custom.CrazyShipAbilities.Abilities
import Custom.CrazyShipAbilities.KeyBinds

ET_REFRESH_USE_ABILITY = App.Game_GetNextEventType()

ButtonRefreshTimerId = None

def Reset():
    global ButtonRefreshTimerId, AbilityButtons
    AbilityButtons = []

    if ButtonRefreshTimerId:
        App.g_kTimerManager.DeleteTimer(ButtonRefreshTimerId)
        ButtonRefreshTimerId = None

    Custom.CrazyShipAbilities.KeyBinds.SetUpKeyHandler()

def ButtonCreated(button):
    global AbilityButtons
    AbilityButtons.append(button)

    if ButtonRefreshTimerId:
        return

    SetupButtonTitleRefreshTimer()

def SetupButtonTitleRefreshTimer():
    global ButtonRefreshTimerId
    AbilityButtons[0].AddPythonFuncHandlerForInstance(ET_REFRESH_USE_ABILITY, __name__ + '.RefreshButtonsTitles')

    pEvent = App.TGEvent_Create()
    pEvent.SetEventType(ET_REFRESH_USE_ABILITY)
    pEvent.SetDestination(AbilityButtons[0])

    pTimer = App.TGTimer_Create()
    pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 0.125)
    pTimer.SetDelay(0.125)
    pTimer.SetDuration(-1)
    pTimer.SetEvent(pEvent)
    ButtonRefreshTimerId = App.g_kTimerManager.AddTimer(pTimer)

def RefreshButtonsTitles(_pObject, _pEvent):
    title = GetAbilityButtonTitle()
    for button in AbilityButtons:
        button.SetName(title)

def UseAbility(_pObject, _pEvent):
    Custom.CrazyShipAbilities.Abilities.UseAbility()

def GetAbilityButtonTitle():
    if not Custom.CrazyShipAbilities.Abilities.IsSupported():
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
        return App.TGString(title + ' (' + FormatCooldownS(cooldownS) + ')')

def GetButtonTitleForCompoundCooldown(nCooldowns):
    title = Custom.CrazyShipAbilities.Abilities.GetTitle()
    nReady = Custom.CrazyShipAbilities.Abilities.GetNReady()

    if nReady == nCooldowns:
        return App.TGString(title + ' (' + str(nCooldowns) + '/' + str(nCooldowns) + ')')
    else:
        s = FormatCooldownS(Custom.CrazyShipAbilities.Abilities.GetCooldownS())
        return App.TGString(title + ' (' + str(nReady) + '/' + str(nCooldowns) + ') (' + s + ')')

def FormatCooldownS(cooldownS):
    import math
    return str(int(math.ceil(cooldownS))) + 's'
