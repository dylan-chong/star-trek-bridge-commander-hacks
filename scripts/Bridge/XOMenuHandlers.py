# File: X (Python 1.5)

import App
import BridgeUtils

def CreateMenus():
    pTopWindow = App.TopWindow_GetTopWindow()
    pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pXOMenu = App.STTopLevelMenu_CreateW(pDatabase.GetString('Commander'))
    pXOPane = App.STStylizedWindow_CreateW('StylizedWindow', 'NoMinimize', pDatabase.GetString('Commander'), 0.0, 0.0)
    pXOPane.AddChild(pXOMenu, 0.0, 0.0, 0)
    pXOMenu.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, 'Bridge.BridgeMenus.ButtonClicked')
    import BridgeMenus
    pCommunicate = BridgeMenus.CreateCommunicateButton('XO', pXOMenu)
    pXOMenu.AddChild(pCommunicate, 0.0, 0.0, 0)
    pReport = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Damage Report'), App.ET_REPORT, 0, pXOMenu)
    pXOMenu.AddChild(pReport, 0.0, 0.0, 0)
    pXOMenu.AddChild(BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Green Alert'), App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_GREEN, pXOMenu), 0.0, 0.0, 0)
    pXOMenu.AddChild(BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Yellow Alert'), App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_YELLOW, pXOMenu), 0.0, 0.0, 0)
    pXOMenu.AddChild(BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Red Alert'), App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_RED, pXOMenu), 0.0, 0.0, 0)
    pObjectives = App.STCharacterMenu_CreateW(pDatabase.GetString('Objectives'))
    pXOMenu.AddChild(pObjectives, 0.0, 0.0, 0)
    pShowLog = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Show Mission Log'), App.ET_SHOW_MISSION_LOG, 0, pXOMenu)
    pXOMenu.AddChild(pShowLog, 0.0, 0.0, 0)
    pContactStarfleet = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Contact Starfleet'), App.ET_CONTACT_STARFLEET, 0, pXOMenu)
    pXOMenu.AddChild(pContactStarfleet, 0.0, 0.0, 0)
    pContactEngineering = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Contact Engineering'), App.ET_CONTACT_ENGINEERING, 0, pXOMenu)
    pXOMenu.AddChild(pContactEngineering, 0.0, 0.0, 0)
    pContactEngineering.SetDisabled()
    if App.g_kUtopiaModule.IsMultiplayer():
        pReport.SetDisabled()
        pCommunicate.SetDisabled()
        pObjectives.SetDisabled()
        pShowLog.SetDisabled()
        pContactStarfleet.SetDisabled()
        pContactEngineering.SetDisabled()
    
    App.g_kLocalizationManager.Unload(pDatabase)
    pXOPane.SetNotVisible()
    pXOMenu.SetNotVisible()
    pXOMenu.SetNoSkipParent()
    pTacticalControlWindow.AddChild(pXOPane, 0.0, 0.0, 0)
    pTacticalControlWindow.AddMenuToList(pXOMenu)
    pXOMenu.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + '.SetAlertLevel')
    pXOMenu.AddPythonFuncHandlerForInstance(App.ET_OBJECTIVES, __name__ + '.Objectives')
    pXOMenu.AddPythonFuncHandlerForInstance(App.ET_CONTACT_ENGINEERING, 'Bridge.EngineerCharacterHandlers.ContactEngineering')
    pXOMenu.AddPythonFuncHandlerForInstance(App.ET_COMMUNICATE, 'Bridge.Characters.CommonAnimations.NothingToAdd')
    pXOMenu.AddPythonFuncHandlerForInstance(App.ET_SHOW_MISSION_LOG, __name__ + '.ShowLog')
    return pXOMenu


def SetAlertLevel(pObject, pEvent):
    iType = pEvent.GetInt()
    pGame = App.Game_GetCurrentGame()
    pPlayer = App.ShipClass_Cast(pGame.GetPlayer())
    if App.IsNull(pPlayer):
        pObject.CallNextHandler(pEvent)
        return None
    
    iLevel = 0
    if iType == App.CharacterClass.EST_ALERT_GREEN:
        iLevel = pPlayer.GREEN_ALERT
    
    if iType == App.CharacterClass.EST_ALERT_YELLOW:
        iLevel = pPlayer.YELLOW_ALERT
    
    if iType == App.CharacterClass.EST_ALERT_RED:
        iLevel = pPlayer.RED_ALERT
    
    if iLevel != pPlayer.GetAlertLevel():
        if iType == App.CharacterClass.EST_ALERT_GREEN:
            App.TGSoundAction_Create('GreenAlertSound').Play()
        
        if iType == App.CharacterClass.EST_ALERT_YELLOW:
            App.TGSoundAction_Create('YellowAlertSound').Play()
        
        if iType == App.CharacterClass.EST_ALERT_RED:
            App.TGSoundAction_Create('RedAlertSound').Play()
        
        pAlertEvent = App.TGIntEvent_Create()
        pAlertEvent.SetSource(pObject)
        pAlertEvent.SetDestination(pPlayer)
        pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
        pAlertEvent.SetInt(iLevel)
        App.g_kEventManager.AddEvent(pAlertEvent)
    
    pObject.CallNextHandler(pEvent)


def Objectives(pObject, pEvent):
    pObject.CallNextHandler(pEvent)


def SetContactEngineeringEnabled(bEnabled):
    pBridge = App.g_kSetManager.GetSet('bridge')
    pXO = App.CharacterClass_GetObject(pBridge, 'XO')
    pMenu = pXO.GetMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pButton = pMenu.GetButtonW(pDatabase.GetString('Contact Engineering'))
    if pButton:
        if bEnabled:
            pButton.SetEnabled()
        else:
            pButton.SetDisabled()
    
    App.g_kLocalizationManager.Unload(pDatabase)


def ShowLog(pObject, pEvent):
    pLog = App.STMissionLog_GetMissionLog()
    pTopWindow = App.TopWindow_GetTopWindow()
    App.g_kUtopiaModule.Pause(1)
    pWindow = App.STStylizedWindow_Cast(pLog.GetFirstChild())
    if pWindow != None:
        pWindow.ScrollToBottom()
    
    pTopWindow.MoveToFront(pLog)
    pLog.SetVisible()
    pTopWindow.SetFocus(pLog)
    pObject.CallNextHandler(pEvent)

