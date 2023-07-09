# File: T (Python 1.5)

import App
import BridgeHandlers
import BridgeUtils
import MissionLib
import Custom.CrazyShipAbilities.UseAbilityButtonHandlers
if App.Game_GetCurrentGame():
    App.Game_GetCurrentGame().AddPersistentModule(__name__)

EST_FIRST_ORDER = 1
EST_ORDER_DESTROY = 1
EST_ORDER_DISABLE = 2
EST_ORDER_STOP = 3
EST_ORDER_DEFENSE = 4
EST_LAST_ORDER = 9
EST_FIRST_TACTIC = 10
EST_TACTIC_ATWILL = 10
EST_TACTIC_LEFT = 11
EST_TACTIC_RIGHT = 12
EST_TACTIC_FORE = 13
EST_TACTIC_AFT = 14
EST_TACTIC_TOP = 15
EST_TACTIC_BOTTOM = 16
EST_LAST_TACTIC = 19
EST_FIRST_MANEUVER = 20
EST_MANEUVER_ATWILL = 20
EST_MANEUVER_CLOSE = 21
EST_MANEUVER_MAINTAIN = 22
EST_MANEUVER_SEPARATE = 23
EST_LAST_MANEUVER = 29
EST_USE_ABILITY = 31

g_bIgnoreNextAIDone = 0
g_fLastWarnTime = 0
g_lPlayerFireAIs = []
g_idCurrentAI = None
g_idTacticalMenu = App.NULL_ID
g_iAutoTargetChange = 0
g_iOrderState = -1
g_lOrders = [
    ('OrderDestroy', EST_ORDER_DESTROY),
    ('OrderDisable', EST_ORDER_DISABLE),
    ('OrderStop', EST_ORDER_STOP),
    ('OrderDefense', EST_ORDER_DEFENSE)]
g_pOrdersStatusUI = None
g_pOrdersStatusUIPane = None
g_idOrdersStatusDisplay = App.NULL_ID
g_lAttackOrders = [
    g_lOrders[0][0],
    g_lOrders[1][0]]
g_iTacticState = 0
g_lTactics = [
    ('TacticAtWill', EST_TACTIC_ATWILL),
    ('TacticLeft', EST_TACTIC_LEFT),
    ('TacticRight', EST_TACTIC_RIGHT),
    ('TacticFore', EST_TACTIC_FORE),
    ('TacticAft', EST_TACTIC_AFT),
    ('TacticTop', EST_TACTIC_TOP),
    ('TacticBottom', EST_TACTIC_BOTTOM)]
g_iManeuverState = 0
g_lManeuvers = [
    ('ManeuverAtWill', EST_MANEUVER_ATWILL),
    ('ManeuverClose', EST_MANEUVER_CLOSE),
    ('ManeuverMaintain', EST_MANEUVER_MAINTAIN),
    ('ManeuverSeparate', EST_MANEUVER_SEPARATE)]

def Mix(vMain, vSecondary):
    vMain.Scale(2.0)
    vMain.Add(vSecondary)
    vMain.Unitize()
    return vMain

vLeftBack = Mix(App.TGPoint3_GetModelLeft(), App.TGPoint3_GetModelForward())
vLeft = App.TGPoint3_GetModelLeft()
vLeftFwd = Mix(App.TGPoint3_GetModelLeft(), App.TGPoint3_GetModelForward())
vFwd = App.TGPoint3_GetModelForward()
vRightFwd = Mix(App.TGPoint3_GetModelRight(), App.TGPoint3_GetModelForward())
vRight = App.TGPoint3_GetModelRight()
vRightBack = Mix(App.TGPoint3_GetModelRight(), App.TGPoint3_GetModelForward())
vUpFwd = Mix(App.TGPoint3_GetModelUp(), App.TGPoint3_GetModelForward())
vUp = App.TGPoint3_GetModelUp()
vUpBack = Mix(App.TGPoint3_GetModelUp(), App.TGPoint3_GetModelBackward())
vDownFwd = Mix(App.TGPoint3_GetModelDown(), App.TGPoint3_GetModelForward())
vDown = App.TGPoint3_GetModelDown()
vDownBack = Mix(App.TGPoint3_GetModelDown(), App.TGPoint3_GetModelBackward())
del Mix
g_dAIs = {
    ('OrderDestroy', 'TacticAtWill', 'ManeuverAtWill'): ('DestroyFreely', ()),
    ('OrderDestroy', 'TacticAtWill', 'ManeuverClose'): ('DestroyFreelyClose', ()),
    ('OrderDestroy', 'TacticAtWill', 'ManeuverMaintain'): ('DestroyFreelyMaintain', ()),
    ('OrderDestroy', 'TacticAtWill', 'ManeuverSeparate'): ('DestroyFreelySeparate', ()),
    ('OrderDestroy', 'TacticLeft', 'ManeuverAtWill'): ('DestroyFromSide', (vLeft, 45.0)),
    ('OrderDestroy', 'TacticLeft', 'ManeuverClose'): ('DestroyFromSide', (vLeftFwd, 45.0)),
    ('OrderDestroy', 'TacticLeft', 'ManeuverMaintain'): ('DestroyFromSide', (vLeft, 45.0)),
    ('OrderDestroy', 'TacticLeft', 'ManeuverSeparate'): ('DestroyFromSide', (vLeftBack, 45.0)),
    ('OrderDestroy', 'TacticRight', 'ManeuverAtWill'): ('DestroyFromSide', (vRight, 45.0)),
    ('OrderDestroy', 'TacticRight', 'ManeuverClose'): ('DestroyFromSide', (vRightFwd, 45.0)),
    ('OrderDestroy', 'TacticRight', 'ManeuverMaintain'): ('DestroyFromSide', (vRight, 45.0)),
    ('OrderDestroy', 'TacticRight', 'ManeuverSeparate'): ('DestroyFromSide', (vRightBack, 45.0)),
    ('OrderDestroy', 'TacticFore', 'ManeuverAtWill'): ('DestroyForeClose', ()),
    ('OrderDestroy', 'TacticFore', 'ManeuverClose'): ('DestroyForeClose', ()),
    ('OrderDestroy', 'TacticFore', 'ManeuverMaintain'): ('DestroyFore', ()),
    ('OrderDestroy', 'TacticAft', 'ManeuverAtWill'): ('DestroyAft', ()),
    ('OrderDestroy', 'TacticAft', 'ManeuverMaintain'): ('DestroyAft', ()),
    ('OrderDestroy', 'TacticAft', 'ManeuverSeparate'): ('DestroyAftSeparate', ()),
    ('OrderDestroy', 'TacticTop', 'ManeuverAtWill'): ('DestroyFaceSide', (vUpFwd,)),
    ('OrderDestroy', 'TacticTop', 'ManeuverClose'): ('DestroyFaceSide', (vUpFwd,)),
    ('OrderDestroy', 'TacticTop', 'ManeuverMaintain'): ('DestroyFaceSide', (vUp,)),
    ('OrderDestroy', 'TacticTop', 'ManeuverSeparate'): ('DestroyFaceSide', (vUpBack,)),
    ('OrderDestroy', 'TacticBottom', 'ManeuverAtWill'): ('DestroyFaceSide', (vDownFwd,)),
    ('OrderDestroy', 'TacticBottom', 'ManeuverClose'): ('DestroyFaceSide', (vDownFwd,)),
    ('OrderDestroy', 'TacticBottom', 'ManeuverMaintain'): ('DestroyFaceSide', (vDown,)),
    ('OrderDestroy', 'TacticBottom', 'ManeuverSeparate'): ('DestroyFaceSide', (vDownBack,)),
    ('OrderDisable', 'TacticAtWill', 'ManeuverAtWill'): ('DisableFreely', ()),
    ('OrderDisable', 'TacticAtWill', 'ManeuverClose'): ('DisableFreelyClose', ()),
    ('OrderDisable', 'TacticAtWill', 'ManeuverMaintain'): ('DisableFreelyMaintain', ()),
    ('OrderDisable', 'TacticAtWill', 'ManeuverSeparate'): ('DisableFreelySeparate', ()),
    ('OrderDisable', 'TacticLeft', 'ManeuverAtWill'): ('DisableFromSide', (vLeft, 45.0)),
    ('OrderDisable', 'TacticLeft', 'ManeuverClose'): ('DisableFromSide', (vLeftFwd, 45.0)),
    ('OrderDisable', 'TacticLeft', 'ManeuverMaintain'): ('DisableFromSide', (vLeft, 45.0)),
    ('OrderDisable', 'TacticLeft', 'ManeuverSeparate'): ('DisableFromSide', (vLeftBack, 45.0)),
    ('OrderDisable', 'TacticRight', 'ManeuverAtWill'): ('DisableFromSide', (vRight, 45.0)),
    ('OrderDisable', 'TacticRight', 'ManeuverClose'): ('DisableFromSide', (vRightFwd, 45.0)),
    ('OrderDisable', 'TacticRight', 'ManeuverMaintain'): ('DisableFromSide', (vRight, 45.0)),
    ('OrderDisable', 'TacticRight', 'ManeuverSeparate'): ('DisableFromSide', (vRightBack, 45.0)),
    ('OrderDisable', 'TacticFore', 'ManeuverAtWill'): ('DisableForeClose', ()),
    ('OrderDisable', 'TacticFore', 'ManeuverClose'): ('DisableForeClose', ()),
    ('OrderDisable', 'TacticFore', 'ManeuverMaintain'): ('DisableFore', ()),
    ('OrderDisable', 'TacticAft', 'ManeuverAtWill'): ('DisableAft', ()),
    ('OrderDisable', 'TacticAft', 'ManeuverMaintain'): ('DisableAft', ()),
    ('OrderDisable', 'TacticAft', 'ManeuverSeparate'): ('DisableAftSeparate', ()),
    ('OrderDisable', 'TacticTop', 'ManeuverAtWill'): ('DisableFaceSide', (vUpFwd,)),
    ('OrderDisable', 'TacticTop', 'ManeuverClose'): ('DisableFaceSide', (vUpFwd,)),
    ('OrderDisable', 'TacticTop', 'ManeuverMaintain'): ('DisableFaceSide', (vUp,)),
    ('OrderDisable', 'TacticTop', 'ManeuverSeparate'): ('DisableFaceSide', (vUpBack,)),
    ('OrderDisable', 'TacticBottom', 'ManeuverAtWill'): ('DisableFaceSide', (vDownFwd,)),
    ('OrderDisable', 'TacticBottom', 'ManeuverClose'): ('DisableFaceSide', (vDownFwd,)),
    ('OrderDisable', 'TacticBottom', 'ManeuverMaintain'): ('DisableFaceSide', (vDown,)),
    ('OrderDisable', 'TacticBottom', 'ManeuverSeparate'): ('DisableFaceSide', (vDownBack,)),
    ('OrderDefense', None, None): ('Defense', ()),
    ('OrderStop', None, None): ('Stay', ()),
    ('OrderStopSelect', None, None): ('StaySelectTarget', ()) }

def CreateMenus():
    global ET_TARGETING_TOGGLED, ET_PHASERS_ONLY
    ET_TARGETING_TOGGLED = App.Game_GetNextEventType()
    ET_PHASERS_ONLY = App.Game_GetNextEventType()
    LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
    App.g_kVarManager.SetFloatVariable('global', 'atoggle', 0)
    pTopWindow = App.TopWindow_GetTopWindow()
    pTacticalWindow = App.TacticalControlWindow_Create()
    kInterfacePane = App.TGPane_Create(LCARS.SCREEN_WIDTH, LCARS.SCREEN_HEIGHT)
    kBackgroundPane = App.TGPane_Create(LCARS.SCREEN_WIDTH, LCARS.SCREEN_HEIGHT)
    kBackgroundPane.SetNoFocus()
    pTacticalMenuPane = CreateTacticalMenu()
    kInterfacePane.AddChild(pTacticalMenuPane, 0.0, 0.0, 0)
    pTacticalMenuPane.Layout()
    pTacticalMenu = App.STMenu_Cast(pTacticalMenuPane.GetInteriorPane().GetFirstChild())
    if pTacticalMenu != None:
        pTacticalMenu.ForceUpdate()
        pTacticalWindow.AddMenuToList(pTacticalMenu)
    
    pESDisplayPane = CreateEnemyShipDisplay(pTacticalWindow)
    kInterfacePane.AddChild(pESDisplayPane, 0.0, 0.0, 0)
    pESDisplayPane.AlignTo(pTacticalMenuPane, App.TGUIObject.ALIGN_BL, App.TGUIObject.ALIGN_UL)
    pRadarDisplayPane = CreateRadarDisplay(pTacticalWindow)
    pRadarDisplayPane.ResizeUI()
    pRadarDisplayPane.RepositionUI()
    pTargetListPane = CreateTargetList(pTacticalWindow)
    TARGET_LIST_WIDTH = LCARS.TACTICAL_MENU_WIDTH
    TARGET_LIST_HEIGHT = LCARS.SCREEN_HEIGHT - pTacticalMenuPane.GetHeight() - pRadarDisplayPane.GetHeight() - LCARS.SEPERATOR_GAP_Y - pESDisplayPane.GetHeight()
    kInterfacePane.AddChild(pTargetListPane, 0.0, 0.0, 0)
    pTargetListPane.Resize(TARGET_LIST_WIDTH, TARGET_LIST_HEIGHT, 0)
    pTargetListPane.AlignTo(pESDisplayPane, App.TGUIObject.ALIGN_BL, App.TGUIObject.ALIGN_UL)
    pTargetList = App.STMenu_Cast(pTargetListPane.GetFirstChild())
    if pTargetList != None:
        pTargetList.ForceUpdate()
    
    pRadarTogglePane = CreateRadarToggle(pTacticalWindow)
    pShipDisplayPane = CreateShipDisplay(pTacticalWindow)
    kInterfacePane.AddChild(pRadarTogglePane, pRadarDisplayPane.GetWidth() - pRadarTogglePane.GetWidth(), LCARS.SCREEN_HEIGHT - pRadarDisplayPane.GetHeight())
    pRadarTogglePane.SetNotVisible()
    kInterfacePane.AddChild(pRadarDisplayPane, 0.0, LCARS.SCREEN_HEIGHT - pRadarDisplayPane.GetHeight())
    kInterfacePane.AddChild(pShipDisplayPane, 0.0, 0.0, 0)
    pOrdersStatusPane = CreateOrdersStatusDisplay(LCARS.SCREEN_WIDTH - LCARS.TACTICAL_MENU_WIDTH - pTacticalMenuPane.GetBorderWidth(), pTacticalMenuPane.GetFirstChild())
    kInterfacePane.AddChild(pOrdersStatusPane, LCARS.SCREEN_WIDTH - pOrdersStatusPane.GetWidth(), 0.0, 0)
    if App.g_kUtopiaModule.IsMultiplayer():
        if App.g_kUtopiaModule.GetTestMenuState() < 3:
            pOrdersStatusPane.SetNotVisible()
        
    
    pWeaponsDisplayPane = CreateWeaponsDisplay(pTacticalWindow)
    kInterfacePane.AddChild(pWeaponsDisplayPane, 0.0, 0.0, 0)
    pWeaponsDisplayPane.SetPosition(LCARS.SCREEN_WIDTH - pWeaponsDisplayPane.GetWidth() - LCARS.WEAPONS_DISPLAY_GAP_X, LCARS.SCREEN_HEIGHT - pWeaponsDisplayPane.GetHeight(), 0)
    pWeaponsControlPane = CreateWeaponsControl(pTopWindow, pTacticalWindow)
    kInterfacePane.AddChild(pWeaponsControlPane, 0.0, 0.0, 0)
    pWeaponsControlPane.AlignTo(pWeaponsDisplayPane, App.TGUIObject.ALIGN_UL, App.TGUIObject.ALIGN_UR)
    pShipDisplayPane.AlignTo(pWeaponsControlPane, App.TGUIObject.ALIGN_UL, App.TGUIObject.ALIGN_UR)
    kInterfacePane.SetFocus(pTargetListPane)
    pTacticalWindow.AddChild(kInterfacePane, 0, 0)
    pTacticalWindow.AddChild(kBackgroundPane, 0, 0)
    pTacControlParent = pTopWindow.FindMainWindow(App.MWT_TACTICAL)
    if pTacControlParent:
        pTacControlParent.AddChild(pTacticalWindow, 0, 0)
    
    UpdateOrderMenus()
    import Tactical.Interface.TacticalControlWindow
    Tactical.Interface.TacticalControlWindow.ResizeUI()
    Tactical.Interface.TacticalControlWindow.RepositionUI()


def CreateTacticalMenu():
    global g_idTacticalMenu
    LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pTacticalMenu = App.STTopLevelMenu_CreateW(pDatabase.GetString('Tactical'))
    if pTacticalMenu:
        g_idTacticalMenu = pTacticalMenu.GetObjID()
    
    pTacticalMenuPane = App.STStylizedWindow_CreateW('StylizedWindow', 'NoMinimize', pDatabase.GetString('Tactical'), 0.0, 0.0)
    pTacticalMenuPane.SetMaximumSize(LCARS.TACTICAL_MENU_WIDTH + pTacticalMenuPane.GetBorderWidth(), LCARS.TACTICAL_MENU_HEIGHT + pTacticalMenuPane.GetBorderHeight())
    pTacticalMenuPane.AddChild(pTacticalMenu, 0.0, 0.0, 0)
    pTacticalMenu.SetNoSkipParent()
    pTacticalMenu.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, 'Bridge.BridgeMenus.ButtonClicked')
    import BridgeMenus
    pCommunicate = BridgeMenus.CreateCommunicateButton('Tactical', pTacticalMenu)
    pTacticalMenu.AddChild(pCommunicate)
    pAbilityButton = BridgeUtils.CreateBridgeMenuButton(App.TGString('...'), EST_USE_ABILITY, 0, pTacticalMenu)
    pTacticalMenu.AddPythonFuncHandlerForInstance(EST_USE_ABILITY, 'Custom.CrazyShipAbilities.UseAbilityButtonHandlers.UseAbility')
    pTacticalMenu.AddChild(pAbilityButton)
    Custom.CrazyShipAbilities.UseAbilityButtonHandlers.ButtonCreated(pAbilityButton)
    pFireButton = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Manual Aim'), App.ET_FIRE, 0, pTacticalMenu)
    pFireButton.SetAutoChoose(1)
    pFireButton.SetChosen(0)
    pFireButton.SetChoosable(1)
    pTacticalMenu.AddChild(pFireButton)
    pPhasersOnlyButton = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('PhasersOnly'), ET_PHASERS_ONLY, 0, pTacticalMenu)
    pPhasersOnlyButton.SetAutoChoose(1)
    pPhasersOnlyButton.SetChosen(0)
    pPhasersOnlyButton.SetChoosable(1)
    pTacticalMenu.AddChild(pPhasersOnlyButton)
    pTargetingButton = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Target At Will'), ET_TARGETING_TOGGLED, 0, pTacticalMenu)
    pTargetingButton.SetAutoChoose(1)
    pTargetingButton.SetChosen(1)
    pTargetingButton.SetChoosable(1)
    pTacticalMenu.AddChild(pTargetingButton)
    if App.g_kUtopiaModule.IsMultiplayer():
        pCommunicate.SetDisabled()
        pPhasersOnlyButton.SetDisabled()
        pFireButton.SetDisabled()
        pTargetingButton.SetDisabled()
    
    App.g_kLocalizationManager.Unload(pDatabase)
    pTacticalMenu.ForceUpdate()
    pTacticalMenu.AddPythonFuncHandlerForInstance(App.ET_MANEUVER, __name__ + '.Maneuver')
    pTacticalMenu.AddPythonFuncHandlerForInstance(App.ET_FIRE, __name__ + '.Fire')
    pTacticalMenu.AddPythonFuncHandlerForInstance(ET_PHASERS_ONLY, __name__ + '.PhasersOnlyToggled')
    pTacticalMenu.AddPythonFuncHandlerForInstance(ET_TARGETING_TOGGLED, __name__ + '.TargetingModeToggled')
    pTacticalMenu.AddPythonFuncHandlerForInstance(App.ET_COMMUNICATE, 'Bridge.Characters.CommonAnimations.NothingToAdd')
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TARGET_WAS_CHANGED, pTacticalMenu, __name__ + '.TargetChanged')
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_RESTORE_PERSISTENT_TARGET, pTacticalMenu, __name__ + '.PersistentTargetRestored')
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, pTacticalMenu, __name__ + '.SetPlayer')
    SetPlayer(None, None)
    pTopWindow = App.TopWindow_GetTopWindow()
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pTacWindow.SetTacticalMenu(pTacticalMenu)
    return pTacticalMenuPane


def SetPlayer(pObject, pEvent):
    pPlayer = MissionLib.GetPlayer()
    if pPlayer:
        pPlayer.AddPythonFuncHandlerForInstance(App.ET_CANT_FIRE, __name__ + '.PlayerCantFire')
        pPlayer.AddPythonFuncHandlerForInstance(App.ET_PLAYER_TORPEDO_TYPE_CHANGED, __name__ + '.PlayerTorpChanged')
    
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)
    


def CreateOrderMenu(sHeader, lInfo, pEventDest, sFocus):
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pMenu = App.STCharacterMenu_CreateW(pDatabase.GetString(sHeader))
    for (sString, eSubType) in lInfo:
        pButton = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString(sString), App.ET_MANEUVER, eSubType, pEventDest)
        pMenu.AddChild(pButton)
        if sString == sFocus:
            pMenu.SetFocus(pButton)
        
    
    App.g_kLocalizationManager.Unload(pDatabase)
    return pMenu


def CreateRadarDisplay(pTacticalWindow):
    pRadarDisplay = App.RadarDisplay_Create(0.0, 0.0)
    pRadarDisplay.SetUseScrolling(0)
    pTacticalWindow.SetRadarDisplay(pRadarDisplay)
    return pRadarDisplay


def CreateTargetList(pTacticalWindow):
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pTargetListMenu = App.STTargetMenu_CreateW(pDatabase.GetString('Targets'))
    App.g_kLocalizationManager.Unload(pDatabase)
    pTacticalWindow.SetTargetMenu(pTargetListMenu)
    pTargetMenuPane = App.STStylizedWindow_CreateW('StylizedWindow', 'NoMinimize', pDatabase.GetString('Targets'), 0.0, 0.0)
    pTargetMenuPane.AddChild(pTargetListMenu)
    pTargetMenuPane.SetUseFocusGlass(1)
    return pTargetMenuPane


def CreateShipDisplay(pTacticalWindow):
    pShipDisplay = App.ShipDisplay_Create()
    pShipDisplay.SetUseScrolling(0)
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pShipDisplay.SetName(pDatabase.GetString('Shields'))
    App.g_kLocalizationManager.Unload(pDatabase)
    pTacticalWindow.SetShipDisplay(pShipDisplay)
    pShipDisplay.InteriorChangedSize(1)
    return pShipDisplay


def CreateOrdersStatusDisplay(fWidth, pTacticalMenu):
    global g_idOrdersStatusDisplay, g_pOrdersStatusUIPane, g_pOrdersStatusUI, g_idOrdersStatusDisplay
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    lDisplays = [
        ('Tactics', 'TacticAtWill', g_lTactics, 'g_pTacticsStatusUI'),
        ('Maneuvers', 'ManeuverAtWill', g_lManeuvers, 'g_pManeuversStatusUI')]
    
    try:
        if g_idOrdersStatusDisplay != App.NULL_ID:
            pOrdersStatusDisplay = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(g_idOrdersStatusDisplay))
            if pOrdersStatusDisplay != None:
                pOrdersStatusDisplay.KillChildren()
            else:
                g_idOrdersStatusDisplay = App.NULL_ID
    except:
        pass

    lOrdersButtons = []
    fOrdersStatusPaneWidth = 0.0
    for lOrder in g_lOrders:
        (sString, eSubType) = lOrder
        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(App.ET_MANEUVER)
        pEvent.SetInt(eSubType)
        pEvent.SetDestination(pTacticalMenu)
        pButton = App.STButton_CreateW(pDatabase.GetString(sString), pEvent, App.STBSF_SIZE_TO_TEXT)
        pButton.SetChoosable(1)
        pButton.SetAutoChoose(1)
        pButton.SetUseEndCaps(0)
        if sString == 'OrderStop':
            pButton.SetChosen(1)
        else:
            pButton.SetChosen(0)
        lOrdersButtons.append(pButton)
        pButton.Layout()
        fOrdersStatusPaneWidth = fOrdersStatusPaneWidth + pButton.GetWidth() + App.globals.DEFAULT_ST_INDENT_HORIZ
    
    g_pOrdersStatusUIPane = App.TGPane_Create(fOrdersStatusPaneWidth / 2.0, (pButton.GetHeight() + 2.0 * App.globals.DEFAULT_ST_INDENT_VERT) * 2.0)
    g_pOrdersStatusUI = App.STStylizedWindow_CreateW('StylizedWindow', 'NoMinimize', pDatabase.GetString('Orders'), 0.0, 0.0, g_pOrdersStatusUIPane)
    g_pOrdersStatusUI.SetUseScrolling(0)
    g_pOrdersStatusUI.SetUseFocusGlass(1)
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    pTCW.RemoveHandlerForInstance(App.ET_INPUT_SELECT_OPTION, __name__ + '.HandleOrdersStatusKeyboard')
    pTCW.RemoveHandlerForInstance(App.ET_INPUT_CLOSE_MENU, __name__ + '.HandleOrdersStatusKeyboard')
    pTCW.AddPythonFuncHandlerForInstance(App.ET_INPUT_SELECT_OPTION, __name__ + '.HandleOrdersStatusKeyboard')
    pTCW.AddPythonFuncHandlerForInstance(App.ET_INPUT_CLOSE_MENU, __name__ + '.HandleOrdersStatusKeyboard')
    fXPos = 0.0
    fYPos = App.globals.DEFAULT_ST_INDENT_VERT
    bSecond = 0
    bHasSecondPos = 0
    for pButton in lOrdersButtons:
        if bSecond == 1 and bHasSecondPos == 1:
            g_pOrdersStatusUIPane.AddChild(pButton, fSecondPos, fYPos, 0)
        else:
            g_pOrdersStatusUIPane.AddChild(pButton, fXPos, fYPos, 0)
        if bSecond == 1:
            fXPos = 0.0
            fYPos = fYPos + pButton.GetHeight() + App.globals.DEFAULT_ST_INDENT_VERT
            bSecond = 0
        else:
            fXPos = fXPos + pButton.GetWidth() + App.globals.DEFAULT_ST_INDENT_HORIZ
            bSecond = 1
            if bHasSecondPos == 0:
                bHasSecondPos = 1
                fSecondPos = fXPos
            
    
    g_pOrdersStatusUIPane.SetEnabled()
    g_pOrdersStatusUI.SetEnabled()
    g_pOrdersStatusUI.InteriorChangedSize()
    g_pOrdersStatusUI.Layout()
    fNumDisplays = float(len(lDisplays))
    fPaneWidth = (fWidth - g_pOrdersStatusUI.GetWidth()) / fNumDisplays - g_pOrdersStatusUI.GetWidth() - g_pOrdersStatusUIPane.GetWidth()
    fMaxHeight = 0.0
    lOrdersPanes = []
    for (sHeader, sDetail, lInfo, sUIVar) in lDisplays:
        pPane = App.STSubPane_Create(0.0, 0.0, 0)
        globals()[sUIVar + 'Pane'] = pPane
        pPopupMenu = CreateOrderMenu(sHeader, lInfo, pTacticalMenu, None)
        globals()[sUIVar + 'Menu'] = pPopupMenu
        App.STSubPane_Cast(pPopupMenu.GetSubPane()).SetExpandToFillParent(0)
        pPane.AddChild(pPopupMenu)
        lOrdersPanes.append(pPane)
    
    if g_idOrdersStatusDisplay == App.NULL_ID:
        pOrdersDisplay = App.TGPane_Create(fWidth, 1.0)
        g_idOrdersStatusDisplay = pOrdersDisplay.GetObjID()
    else:
        pOrdersDisplay = App.TGPane_Cast(App.TGObject_GetTGObjectPtr(g_idOrdersStatusDisplay))
        if pOrdersDisplay != None:
            pOrdersDisplay.Resize(fWidth, 1.0)
        else:
            pOrdersDisplay = App.TGPane_Create(fWidth, 1.0)
            g_idOrdersStatusDisplay = pOrdersDisplay.GetObjID()
    fLeft = 0.0
    pOrdersDisplay.AddChild(g_pOrdersStatusUI, 0.0, 0.0, 0)
    fLeft = fLeft + fOrdersStatusPaneWidth
    pManeuversPane = App.STStylizedWindow_CreateW('StylizedWindow', 'NoMinimize', pDatabase.GetString('Maneuvers'))
    pManeuversPane.SetUseScrolling(0)
    pManeuversPane.SetUseFocusGlass(1)
    pManeuversPane.AddChild(g_pManeuversStatusUIPane)
    g_pManeuversStatusUIMenu.Open()
    kSize = App.NiPoint2(0.0, 0.0)
    g_pManeuversStatusUIMenu.GetDesiredSize(kSize)
    g_pManeuversStatusUIPane.Resize(kSize.x, g_pManeuversStatusUIPane.GetHeight())
    pManeuversPane.SetMaximumSize(kSize.x + pManeuversPane.GetBorderWidth(), 1.0)
    g_pManeuversStatusUIMenu.Close()
    pManeuversPane.InteriorChangedSize()
    pManeuversPane.Layout()
    pTacticsPane = App.STStylizedWindow_CreateW('StylizedWindow', 'NoMinimize', pDatabase.GetString('Tactics'))
    pTacticsPane.SetUseScrolling(0)
    pTacticsPane.SetUseFocusGlass(1)
    pTacticsPane.SetMaximumSize(fPaneWidth + pTacticsPane.GetBorderWidth(), 1.0)
    pTacticsPane.AddChild(g_pTacticsStatusUIPane, 0.0, 0.0, 0)
    g_pTacticsStatusUIMenu.Open()
    kSize = App.NiPoint2(0.0, 0.0)
    g_pTacticsStatusUIMenu.GetDesiredSize(kSize)
    g_pTacticsStatusUIPane.Resize(kSize.x, g_pTacticsStatusUIPane.GetHeight())
    pTacticsPane.SetMaximumSize(kSize.x + pTacticsPane.GetBorderWidth(), 1.0)
    g_pTacticsStatusUIMenu.Close()
    pTacticsPane.InteriorChangedSize()
    pOrdersDisplay.AddChild(pTacticsPane, pOrdersDisplay.GetWidth() - pTacticsPane.GetWidth(), 0.0, 0)
    pOrdersDisplay.AddChild(pManeuversPane, pTacticsPane.GetLeft() - pManeuversPane.GetWidth(), 0.0, 0)
    App.g_kLocalizationManager.Unload(pDatabase)
    return pOrdersDisplay


def CreateEnemyShipDisplay(pWindow):
    pShipDisplay = App.ShipDisplay_Create()
    pShipDisplay.SetUseScrolling(0)
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pShipDisplay.SetName(pDatabase.GetString('TargetShields'))
    App.g_kLocalizationManager.Unload(pDatabase)
    pWindow.SetEnemyShipDisplay(pShipDisplay)
    pShipDisplay.InteriorChangedSize(1)
    return pShipDisplay


def CreateRadarToggle(pWindow):
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
    pEvent = App.TGEvent_Create()
    pEvent.SetDestination(pWindow)
    pEvent.SetEventType(App.ET_RADAR_TOGGLE_CLICKED)
    pRadarToggleButton = App.STButton_CreateW(pDatabase.GetString('Target'), pEvent, 0)
    pRadarToggleButton.Resize(LCARS.RADAR_TOGGLE_WIDTH, LCARS.RADAR_TOGGLE_HEIGHT)
    pRadarToggleButton.SetUseEndCaps(0, 0)
    App.g_kLocalizationManager.Unload(pDatabase)
    pWindow.SetRadarToggle(pRadarToggleButton)
    return pRadarToggleButton


def CreateWeaponsDisplay(pTacticalWindow):
    LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
    pWeaponsDisplay = App.WeaponsDisplay_Create(LCARS.WEAPONS_PANE_WIDTH, LCARS.WEAPONS_PANE_HEIGHT)
    pWeaponsDisplay.SetUseScrolling(0)
    pTacticalWindow.SetWeaponsDisplay(pWeaponsDisplay)
    import Tactical.Interface.WeaponsDisplay
    Tactical.Interface.WeaponsDisplay.ResizeUI(pWeaponsDisplay)
    return pWeaponsDisplay


def OverrideButtonColors(pButton):
    pButton.SetUseUIHeight(0)
    pButton.SetNormalColor(App.g_kSTMenu2NormalBase)
    kDimColor = App.NiColorA()
    kDimColor.r = App.g_kSTMenu2NormalBase.r * 0.5
    kDimColor.g = App.g_kSTMenu2NormalBase.g * 0.5
    kDimColor.b = App.g_kSTMenu2NormalBase.b * 0.5
    pButton.SetSelectedColor(kDimColor)
    pButton.SetHighlightedColor(App.g_kSTMenu2HighlightedBase)
    pButton.SetDisabledColor(App.g_kSTMenu2Disabled)
    pButton.SetColorBasedOnFlags(0)


def CreateWeaponsControl(pTopWindow, pTacticalWindow):
    LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
    pWeaponsControl = App.TacWeaponsCtrl_Create(LCARS.WEAPONS_CTRL_PANE_WIDTH, LCARS.WEAPONS_CTRL_PANE_HEIGHT)
    pWeaponsControl.SetUseScrolling(0)
    pWeaponsControl.SetFixedSize(LCARS.WEAPONS_CTRL_PANE_WIDTH + pWeaponsControl.GetBorderWidth(), LCARS.WEAPONS_CTRL_PANE_HEIGHT + pWeaponsControl.GetBorderHeight())
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pWeaponsControl.SetName(pDatabase.GetString('Weapons'))
    pWeaponsControl.InteriorChangedSize(1)
    App.g_kLocalizationManager.Unload(pDatabase)
    pTacticalWindow.SetWeaponsControl(pWeaponsControl)
    pWeaponsControl.RefreshPhaserSettings()
    pWeaponsControl.RefreshTorpedoSettings()
    pWeaponsControl.SetNotHighlighted(0)
    return pWeaponsControl


def TargetingModeToggled(pMenu, pEvent):
    pMenu.CallNextHandler(pEvent)
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pMenu = pTacWindow.GetTacticalMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pTargetingButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Target At Will')))
    App.g_kLocalizationManager.Unload(pDatabase)
    if pTargetingButton.IsChosen() == 1:
        UpdateOrders(0)
    
    CheckSubsystemTargeting()


def TargetChanged(pObject, pEvent):
    global g_iAutoTargetChange
    pPlayer = App.Game_GetCurrentGame().GetPlayer()
    if not pPlayer or pEvent.GetDestination() == None or pPlayer.GetObjID() != pEvent.GetDestination().GetObjID():
        return None
    
    if not pPlayer.GetTarget():
        if GetHighLevelOrder() in g_lAttackOrders:
            if MissionLib.GetPlayerShipController() == 'Tactical':
                StartAI(1)
            
        
        return None
    
    pTopWindow = App.TopWindow_GetTopWindow()
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pMenu = pTacWindow.GetTacticalMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pTargetingButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Target At Will')))
    App.g_kLocalizationManager.Unload(pDatabase)
    if pTargetingButton is None:
        return None
    
    if g_iAutoTargetChange == 0:
        if MissionLib.GetPlayerShipController() == 'Tactical':
            pTargetingButton.SetChosen(0)
        
    else:
        g_iAutoTargetChange = g_iAutoTargetChange - 1
    pSet = App.g_kSetManager.GetSet('bridge')
    pTactical = App.CharacterClass_GetObject(pSet, 'Tactical')
    UpdateOrders(0)


def PersistentTargetRestored(pObject, pEvent):
    global g_iAutoTargetChange
    g_iAutoTargetChange = g_iAutoTargetChange + 1


def AutoTargetChange(sTarget):
    global g_iAutoTargetChange
    pPlayer = App.Game_GetCurrentPlayer()
    if not pPlayer:
        return None
    
    if not sTarget:
        return None
    
    pTarget = pPlayer.GetTarget()
    if pTarget and pTarget.GetName() == sTarget:
        return None
    
    pTopWindow = App.TopWindow_GetTopWindow()
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pMenu = pTacWindow.GetTacticalMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pTargetingButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Target At Will')))
    App.g_kLocalizationManager.Unload(pDatabase)
    if pTargetingButton.IsChosen() == 1:
        pPlayer.SetTarget(sTarget)
        g_iAutoTargetChange = g_iAutoTargetChange + 1
    


def Fire(pObject, pEvent):
    pPlayer = MissionLib.GetPlayer()
    if pPlayer == None:
        return None
    
    pObject.CallNextHandler(pEvent)
    UpdateManualAim()
    CheckFiring(pPlayer)
    UpdateOrderMenus()


def ResetPickFireButton():
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pMenu = pTacWindow.GetTacticalMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pFireButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Manual Aim')))
    App.g_kLocalizationManager.Unload(pDatabase)
    if pFireButton:
        pFireButton.SetChosen(pTacWindow.GetMousePickFire())
    


def UpdateManualAim():
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pMenu = pTacWindow.GetTacticalMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pFireButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Manual Aim')))
    App.g_kLocalizationManager.Unload(pDatabase)
    if pFireButton.IsChosen():
        pTacWindow.SetMousePickFire(1)
    else:
        pTacWindow.SetMousePickFire(0)


def PhasersOnlyToggled(pObject, pEvent):
    pPlayer = MissionLib.GetPlayer()
    if pPlayer == None:
        return None
    
    pTarget = pPlayer.GetTarget()
    if pTarget == None:
        return None
    
    pObject.CallNextHandler(pEvent)
    CheckFiring(pPlayer)


def Maneuver(pObject, pEvent):
    global g_iOrderState, g_iTacticState, g_iManeuverState
    MissionLib.SetPlayerAI('Tactical', None)
    bAcknowledge = 1
    iSubType = pEvent.GetInt()
    if iSubType <= EST_LAST_ORDER:
        iNewOrderState = iSubType - EST_FIRST_ORDER
        if iNewOrderState != g_iOrderState:
            g_iOrderState = iNewOrderState
            bAcknowledge = 1
        else:
            bAcknowledge = 0
    elif iSubType <= EST_LAST_TACTIC:
        bAcknowledge = 2
        g_iTacticState = iSubType - EST_FIRST_TACTIC
    elif iSubType <= EST_LAST_MANEUVER:
        bAcknowledge = 2
        g_iManeuverState = iSubType - EST_FIRST_MANEUVER
    else:
        return None
    UpdateOrders(bAcknowledge)
    pObject.CallNextHandler(pEvent)


def UpdateOrders(bAcknowledge = 1):
    global g_iOrderState, g_bIgnoreNextAIDone
    if MissionLib.GetPlayerShipController() not in (None, 'Tactical'):
        g_iOrderState = -1
    
    if g_iOrderState != -1:
        if MissionLib.IsPlayerInsideStarbase12():
            g_iOrderState = -1
        
    
    UpdateOrderMenus()
    pTopWindow = App.TopWindow_GetTopWindow()
    pTactical = None
    pSet = App.g_kSetManager.GetSet('bridge')
    if pSet:
        pTactical = App.CharacterClass_GetObject(pSet, 'Tactical')
    
    if MissionLib.GetPlayerShipController() in (None, 'Tactical'):
        pSequence = App.TGSequence_Create()
        bNoAttack = 0
        if GetHighLevelOrder() in g_lAttackOrders:
            pPlayer = App.Game_GetCurrentPlayer()
            if pPlayer:
                pTarget = pPlayer.GetTarget()
                if pTarget:
                    if not App.ShipClass_Cast(pTarget):
                        bNoAttack = 1
                    
                    pMission = MissionLib.GetMission()
                    if pMission:
                        if pMission.GetFriendlyGroup().IsNameInGroup(pTarget.GetName()):
                            pWontFireLine = App.TGScriptAction_Create(__name__, 'FelixWontFire', pTarget.GetName())
                            pSequence.AddAction(pWontFireLine, None, 5.0)
                            bAcknowledge = 0
                            bNoAttack = 1
                        
                    
                
            
        
        if bAcknowledge and pTactical:
            pDatabase = pTactical.GetDatabase()
            pPlayer = App.Game_GetCurrentPlayer()
            if pPlayer and not pPlayer.GetAI():
                sHighOrder = GetHighLevelOrder()
                pTorps = pPlayer.GetTorpedoSystem()
                bTorpsOn = 0
                if pTorps:
                    bTorpsOn = pTorps.IsOn()
                
                pPhasers = pPlayer.GetPhaserSystem()
                bPhasersOn = 0
                if pPhasers:
                    pPhasersOn = pPhasers.IsOn()
                
                if bAcknowledge == 2:
                    pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, pTactical.GetCharacterName() + 'Yes%d' % (App.g_kSystemWrapper.GetRandomNumber(4) + 1), None, 1, pDatabase, App.CSP_SPONTANEOUS))
                elif sHighOrder == 'OrderStop':
                    pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'Disengaging', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                    pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, pTactical.GetCharacterName() + 'Yes%d' % (App.g_kSystemWrapper.GetRandomNumber(4) + 1), None, 1, pDatabase, App.CSP_SPONTANEOUS))
                elif sHighOrder == 'OrderDefense':
                    pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'EvasiveManuvers', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                elif sHighOrder == 'OrderDestroy':
                    if not bTorpsOn and not bPhasersOn:
                        g_iOrderState = -1
                        UpdateOrders()
                        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'NeedPower', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                    elif not pPlayer.GetTarget():
                        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'AdjustTactic', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                    else:
                        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'gt213', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                elif sHighOrder == 'OrderDisable':
                    if not bTorpsOn and not bPhasersOn:
                        g_iOrderState = -1
                        UpdateOrders()
                        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'NeedPower', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                    elif not pPlayer.GetTarget():
                        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'AdjustTactic', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                    else:
                        pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'gt212', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                else:
                    pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'TacticalManuver', None, 1, pDatabase, App.CSP_SPONTANEOUS))
                    pSequence.AppendAction(App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, pTactical.GetCharacterName() + 'Yes%d' % (App.g_kSystemWrapper.GetRandomNumber(4) + 1), None, 1, pDatabase, App.CSP_SPONTANEOUS))
            
        
        pSequence.Play()
        bActive = StartAI(bNoAttack)
        if pTactical:
            pTactical.SetActive(bActive)
            if bActive:
                pDatabase = App.g_kLocalizationManager.Load('data/TGL/CharacterStatus.tgl')
                pcHighLevelOrder = GetHighLevelOrder()
                if pcHighLevelOrder == 'OrderDestroy':
                    pTactical.SetStatus(pDatabase.GetString('Attacking'))
                elif pcHighLevelOrder == 'OrderDisable':
                    pTactical.SetStatus(pDatabase.GetString('Disabling'))
                elif pcHighLevelOrder == 'OrderDefense':
                    pTactical.SetStatus(pDatabase.GetString('Defending'))
                
                App.g_kLocalizationManager.Unload(pDatabase)
                g_bIgnoreNextAIDone = 1
            
        
    elif pTactical:
        pTactical.SetActive(0)
    


def FelixWontFire(pAction, sOldTargetName):
    if not (GetHighLevelOrder() in g_lAttackOrders):
        return 0
    
    pPlayer = App.Game_GetCurrentPlayer()
    if pPlayer:
        pTarget = pPlayer.GetTarget()
        if pTarget and pTarget.GetName() == sOldTargetName:
            pMission = MissionLib.GetMission()
            if pMission:
                if pMission.GetFriendlyGroup().IsNameInGroup(pTarget.GetName()):
                    pBridgeSet = App.g_kSetManager.GetSet('bridge')
                    pTactical = App.CharacterClass_GetObject(pBridgeSet, 'Tactical')
                    if pTactical:
                        pDatabase = pTactical.GetDatabase()
                        pWontFireLine = App.CharacterAction_Create(pTactical, App.CharacterAction.AT_SAY_LINE, 'BadTarget%d' % (App.g_kSystemWrapper.GetRandomNumber(2) + 1), None, 1, pDatabase, App.CSP_SPONTANEOUS)
                        pWontFireLine.Play()
                    
                
            
        
    
    return 0


def ClearOrderMenus():
    global g_iOrderState, g_iTacticState, g_iManeuverState
    g_iOrderState = 2
    g_iTacticState = 0
    g_iManeuverState = 0
    sTactic = GetTactic()
    sManeuver = GetManeuver()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    g_pTacticsStatusUIMenu.SetName(pDatabase.GetString(sTactic))
    g_pManeuversStatusUIMenu.SetName(pDatabase.GetString(sManeuver))
    App.g_kLocalizationManager.Unload(pDatabase)
    g_pTacticsStatusUIMenu.Close()
    g_pManeuversStatusUIMenu.Close()
    UpdateOrderMenus()


def UpdateOrderMenus():
    sCurrentOrder = GetHighLevelOrder()
    sCurrentTactic = GetTactic()
    sCurrentManeuver = GetManeuver()
    bNotDisable = 0
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        CallFuncOnMenuAndChildren('SetDisabled', g_pTacticsStatusUIMenu, len(g_lTactics))
        CallFuncOnMenuAndChildren('SetDisabled', g_pManeuversStatusUIMenu, len(g_lManeuvers))
    else:
        CallFuncOnMenuAndChildren('SetEnabled', g_pOrdersStatusUIPane, len(g_lOrders))
        CallFuncOnMenuAndChildren('SetEnabled', g_pTacticsStatusUIMenu, len(g_lTactics))
        CallFuncOnMenuAndChildren('SetEnabled', g_pManeuversStatusUIMenu, len(g_lManeuvers))
        pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pMenu = pTacWindow.GetTacticalMenu()
        pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
        pFireButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Manual Aim')))
        bAttackToggle = pFireButton.IsChosen()
        pDestroyButton = App.STButton_Cast(g_pOrdersStatusUIPane.GetNthChild(0))
        pDisableButton = App.STButton_Cast(g_pOrdersStatusUIPane.GetNthChild(1))
        kString = App.TGString()
        pDestroyButton.GetName(kString)
        sHighOrder = GetHighLevelOrder()
        if bAttackToggle == 0:
            pDisableButton.SetVisible(0)
            if kString.Compare(pDatabase.GetString('OrderDestroy'), 1) != 0:
                if sHighOrder == 'OrderDestroy':
                    pDisableButton.SetChosen(0)
                    pDestroyButton.SetChosen(1)
                elif sHighOrder == 'OrderDisable':
                    pDestroyButton.SetChosen(0)
                    pDisableButton.SetChosen(1)
                else:
                    pDestroyButton.SetChosen(0)
                    pDisableButton.SetChosen(0)
                pDestroyButton.SetName(pDatabase.GetString('OrderDestroy'))
            
        else:
            pDisableButton.SetNotVisible(0)
            bNotDisable = 1
            if kString.Compare(pDatabase.GetString('OrderAttackManeuver'), 1) != 0:
                if sHighOrder == 'OrderDestroy' or sHighOrder == 'OrderDisable':
                    pDisableButton.SetChosen(0)
                    pDestroyButton.SetChosen(1)
                else:
                    pDestroyButton.SetChosen(0, 0)
                    pDisableButton.SetChosen(0, 0)
                pDestroyButton.SetName(pDatabase.GetString('OrderAttackManeuver'))
            
        App.g_kLocalizationManager.Unload(pDatabase)
        pStatusButton = g_pOrdersStatusUIPane.GetFirstChild()
        for iButton in range(len(g_lOrders)):
            pStatusButton.SetEnabled()
            pStatusButton = g_pOrdersStatusUIPane.GetNextChild(pStatusButton)
        
        sCurrentOrder = GetHighLevelOrder()
        lEnabledTactics = []
        for (sOrder, sTactic, sManeuver) in g_dAIs.keys():
            if sOrder == sCurrentOrder:
                if not (sTactic in lEnabledTactics):
                    lEnabledTactics.append(sTactic)
                
            
        
        pStatusButton = g_pTacticsStatusUIMenu.GetFirstChild()
        bOneAvailable = 0
        for (sTactic, eEvent) in g_lTactics:
            if sTactic in lEnabledTactics:
                bOneAvailable = 1
                pStatusButton.SetEnabled()
            else:
                pStatusButton.SetDisabled()
            pStatusButton = g_pTacticsStatusUIMenu.GetNextChild(pStatusButton)
        
        if not bOneAvailable:
            pass
        1
        sCurrentTactic = GetTactic()
        lEnabledManeuvers = []
        for (sOrder, sTactic, sManeuver) in g_dAIs.keys():
            if sOrder == sCurrentOrder and sTactic == sCurrentTactic:
                if not (sManeuver in lEnabledManeuvers):
                    lEnabledManeuvers.append(sManeuver)
                
            
        
        pStatusButton = g_pManeuversStatusUIMenu.GetFirstChild()
        bOneAvailable = 0
        for (sManeuver, eEvent) in g_lManeuvers:
            if sManeuver in lEnabledManeuvers:
                bOneAvailable = 1
                pStatusButton.SetEnabled()
            else:
                pStatusButton.SetDisabled()
            pStatusButton = g_pManeuversStatusUIMenu.GetNextChild(pStatusButton)
        
        if not bOneAvailable:
            pass
        1
        sCurrentManeuver = GetManeuver()
    pStatusButton = App.STButton_Cast(g_pOrdersStatusUIPane.GetFirstChild())
    for (sOrder, eEvent) in g_lOrders:
        if sOrder == sCurrentOrder:
            if sOrder == 'OrderDisable' and bNotDisable == 1:
                pStatusButton.SetChosen(0)
            else:
                pStatusButton.SetChosen(1)
        elif sOrder == 'OrderDestroy' and bNotDisable == 1 and sCurrentOrder == 'OrderDisable':
            pStatusButton.SetChosen(1)
        else:
            pStatusButton.SetChosen(0)
        pStatusButton = App.STButton_Cast(g_pOrdersStatusUIPane.GetNextChild(pStatusButton))
    
    UpdateOrderStatusButtons(sCurrentOrder, sCurrentTactic, sCurrentManeuver, g_pOrdersStatusUIPane.IsEnabled(), g_pTacticsStatusUIMenu.IsEnabled(), g_pManeuversStatusUIMenu.IsEnabled())


def CallFuncOnMenuAndChildren(sFunc, pMenu, iNumChildren):
    pFunc = getattr(pMenu, sFunc)
    pFunc()
    pChild = pMenu.GetFirstChild()
    for iChild in range(iNumChildren):
        pFunc = getattr(pChild, sFunc)
        pFunc()
        pChild = pMenu.GetNextChild(pChild)
    


def UpdateOrderStatusButtons(sOrder, sTactic, sManeuver, bOrderEnabled, bTacticEnabled, bManeuverEnabled):
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    if bTacticEnabled and sTactic:
        g_pTacticsStatusUIMenu.SetEnabled()
        g_pTacticsStatusUIMenu.SetName(pDatabase.GetString(sTactic))
    elif sTactic:
        g_pTacticsStatusUIMenu.SetName(pDatabase.GetString(sTactic))
    else:
        g_pTacticsStatusUIMenu.SetName(pDatabase.GetString(g_lTactics[0][0]))
    if bManeuverEnabled and sManeuver:
        g_pManeuversStatusUIMenu.SetEnabled()
        g_pManeuversStatusUIMenu.SetName(pDatabase.GetString(sManeuver))
    elif sManeuver:
        g_pManeuversStatusUIMenu.SetName(pDatabase.GetString(sManeuver))
    else:
        g_pManeuversStatusUIMenu.SetName(pDatabase.GetString(g_lManeuvers[0][0]))
    App.g_kLocalizationManager.Unload(pDatabase)


def CheckFiring(pPlayer):
    lAIScripts = GetPlayerFiringAIScripts()
    pTopWindow = App.TopWindow_GetTopWindow()
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pMenu = pTacWindow.GetTacticalMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pFireButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Manual Aim')))
    bAttackToggle = not pFireButton.IsChosen()
    pPhasersOnlyButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('PhasersOnly')))
    bPhasersOnly = pPhasersOnlyButton.IsChosen()
    App.g_kLocalizationManager.Unload(pDatabase)
    for pScript in lAIScripts:
        pScript.SetEnabled(bAttackToggle)
        if bPhasersOnly:
            lWeaponSystems = [
                pPlayer.GetPhaserSystem()]
        else:
            lWeaponSystems = [
                pPlayer.GetPhaserSystem(),
                pPlayer.GetTorpedoSystem(),
                pPlayer.GetPulseWeaponSystem()]
        bDifferent = 0
        lScriptWeapons = pScript.GetWeapons()
        if len(lScriptWeapons) != len(lWeaponSystems):
            bDifferent = 1
        else:
            for iIndex in range(len(lWeaponSystems)):
                if lScriptWeapons[iIndex].GetObjID() != lWeaponSystems[iIndex].GetObjID():
                    bDifferent = 1
                    break
                
            
        if bDifferent:
            pScript.RemoveAllWeaponSystems()
            for pSystem in lWeaponSystems:
                if pSystem:
                    pScript.AddWeaponSystem(pSystem)
                
            
        
    


def CheckSubsystemTargeting():
    lFireScripts = GetPlayerFiringAIScripts()
    if not lFireScripts:
        return None
    
    pTacWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pMenu = pTacWindow.GetTacticalMenu()
    pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
    pTargetingButton = App.STButton_Cast(pMenu.GetButtonW(pDatabase.GetString('Target At Will')))
    App.g_kLocalizationManager.Unload(pDatabase)
    if pTargetingButton.IsChosen() == 1:
        iRestored = 0
        for pScript in lFireScripts:
            if not pScript.HasSubsystemTargets():
                pScript.RestoreSubsystemTargets()
                iRestored = iRestored + 1
            
        
    else:
        iIgnored = 0
        for pScript in lFireScripts:
            if pScript.HasSubsystemTargets():
                pScript.IgnoreSubsystemTargets()
                iIgnored = iIgnored + 1
            
        


def GetPlayerFiringAIScripts():
    lFireScripts = []
    for idAI in g_lPlayerFireAIs:
        pAI = App.PreprocessingAI_Cast(App.ArtificialIntelligence_GetAIByID(idAI))
        if pAI:
            pScript = pAI.GetPreprocessingInstance()
            if pScript:
                lFireScripts.append(pScript)
            
        
    
    return lFireScripts


def StartAI(bNoAttack):
    global g_lPlayerFireAIs, g_idCurrentAI
    pGame = App.Game_GetCurrentGame()
    if not pGame:
        return 0
    
    pPlayer = pGame.GetPlayer()
    if not pPlayer:
        return 0
    
    pPlayer.ClearAI()
    pTarget = pPlayer.GetTarget()
    if bNoAttack and GetHighLevelOrder() in g_lAttackOrders:
        (sModule, lParams) = ChooseAIFromOrders('OrderStopSelect', None, None)
    else:
        (sModule, lParams) = ChooseAIFromOrders(GetHighLevelOrder(), GetTactic(), GetManeuver())
    if sModule is None or lParams is None:
        return 0
    
    pAIModule = __import__(sModule)
    lFullParams = (pPlayer, pTarget) + lParams
    pPlayerAI = apply(pAIModule.CreateAI, lFullParams)
    g_lPlayerFireAIs = []
    lAIs = pPlayerAI.GetAllAIsInTree()
    for pAI in lAIs:
        pPreAI = App.PreprocessingAI_Cast(pAI)
        if pPreAI:
            pScript = pPreAI.GetPreprocessingInstance()
            import AI.Preprocessors
            if isinstance(pScript, App.OptimizedFireScript):
                g_lPlayerFireAIs.append(pAI.GetID())
            
        
    
    CheckFiring(pPlayer)
    CheckSubsystemTargeting()
    MissionLib.SetPlayerAI('Tactical', pPlayerAI)
    g_idCurrentAI = pPlayerAI.GetID()
    if sModule == g_dAIs[('OrderStop', None, None)]:
        return 0
    
    return 1


def GetHighLevelOrder():
    return GetOrderString(g_pOrdersStatusUIPane, g_iOrderState, g_lOrders)


def GetOrderString(pMenu, iIndex, lOrders):
    if MissionLib.GetPlayerShipController() not in (None, 'Tactical'):
        return None
    
    if iIndex == -1:
        return None
    
    if pMenu and pMenu.IsEnabled():
        pButton = pMenu.GetNthChild(iIndex)
        if not pButton.IsEnabled():
            pButton = pMenu.GetFirstChild()
            for (sOrder, eEvent) in lOrders:
                if pButton.IsEnabled():
                    return sOrder
                
                pButton = pMenu.GetNextChild(pButton)
            
        
        return lOrders[iIndex][0]
    
    return None


def GetTactic():
    return GetOrderString(g_pTacticsStatusUIMenu, g_iTacticState, g_lTactics)


def GetManeuver():
    return GetOrderString(g_pManeuversStatusUIMenu, g_iManeuverState, g_lManeuvers)


def ChooseAIFromOrders(sOrder, sTactic, sManeuver):
    if not g_dAIs.has_key((sOrder, sTactic, sManeuver)):
        if not g_dAIs.has_key((sOrder, None, None)):
            return (None, None)
        else:
            sTactic = None
            sManeuver = None
    
    (sModule, lParams) = g_dAIs[(sOrder, sTactic, sManeuver)]
    sModule = 'AI.Player.' + sModule
    return (sModule, lParams)


def PlayerCantFire(pObject, pEvent):
    global g_fLastWarnTime
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        pObject.CallNextHandler(pEvent)
        return None
    
    pTorps = App.TorpedoSystem_Cast(pEvent.GetSource())
    pPhasers = App.PhaserSystem_Cast(pEvent.GetSource())
    pTractors = App.TractorBeamSystem_Cast(pEvent.GetSource())
    if App.g_kUtopiaModule.GetGameTime() - g_fLastWarnTime < 2:
        pObject.CallNextHandler(pEvent)
        return None
    
    if pTorps:
        if pTorps.GetNumReady() > 0:
            pObject.CallNextHandler(pEvent)
            return None
        
        if pTorps.GetNumAvailableTorpsToType(pTorps.GetAmmoTypeNumber()) <= 0:
            App.g_kSoundManager.PlaySound('UITorpsNoAmmo')
            g_fLastWarnTime = App.g_kUtopiaModule.GetGameTime()
        else:
            App.g_kSoundManager.PlaySound('UITorpsNotLoaded')
            g_fLastWarnTime = App.g_kUtopiaModule.GetGameTime()
    
    pObject.CallNextHandler(pEvent)


def PlayerTorpChanged(pObject, pEvent):
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        pObject.CallNextHandler(pEvent)
        return None
    
    pTorps = App.TorpedoSystem_Cast(pEvent.GetSource())
    if not pTorps:
        pObject.CallNextHandler(pEvent)
        return None
    
    pObject.CallNextHandler(pEvent)


def HandleOrdersStatusKeyboard(pTCW, pEvent):
    pOrdersPane = g_pOrdersStatusUIPane
    if pOrdersPane.IsInTrueFocusPath() == 0:
        pTCW.CallNextHandler(pEvent)
        return None
    
    iFocus = pOrdersPane.FindPos(pOrdersPane.GetFocus())
    if pEvent.GetEventType() == App.ET_INPUT_SELECT_OPTION:
        iMove = pEvent.GetInt()
        if iMove == 0:
            if iFocus == -1:
                pOrdersPane.SetFocus(pOrdersPane.GetFirstChild())
            elif iFocus % 2 == 0:
                pOrdersPane.SetFocus(pOrdersPane.GetNextChild(pOrdersPane.GetFocus()))
            
        elif iMove == 1:
            if iFocus == -1:
                pOrdersPane.SetFocus(pOrdersPane.GetFirstChild())
            elif iFocus < 2:
                pOrdersPane.SetFocus(pOrdersPane.GetNthChild(iFocus + 2))
            
        elif iMove == -1:
            if iFocus == -1:
                pOrdersPane.SetFocus(pOrdersPane.GetFirstChild())
            elif iFocus > 1:
                pOrdersPane.SetFocus(pOrdersPane.GetNthChild(iFocus - 2))
            
        
    elif pEvent.GetEventType() == App.ET_INPUT_CLOSE_MENU:
        if iFocus == -1:
            pOrdersPane.SetFocus(pOrdersPane.GetFirstChild())
        elif iFocus % 2 == 1:
            pOrdersPane.SetFocus(pOrdersPane.GetNthChild(iFocus - 1))
        
    
    pOrdersPane.CallNextHandler(pEvent)

