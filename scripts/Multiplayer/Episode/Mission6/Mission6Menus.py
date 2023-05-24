###############################################################################
#	Filename:	Mission6Menus.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script to build the UI for the Defend the starbase! mission
#	
#	Created:	Jun 12, '01 - Yossi Horowitz
###############################################################################


import App	
import UIHelpers
import MissionLib
import Mission6

# UI positioning info
TEAM_PARA_X_POS				= 0.0925

TEAM_TOGGLE_Y_POS				= 0.8666666
TEAM_TOGGLE_WIDTH				= 0.140625
TEAM_TOGGLE_HEIGHT			= 0.0416667

FRAG_LIMIT_PARA_X_POS				= 0.463125
FRAG_LIMIT_TOGGLE_Y_POS				= 0.9183333
FRAG_LIMIT_TOGGLE_WIDTH				= 0.140625
FRAG_LIMIT_TOGGLE_HEIGHT			= 0.0416667

# globals
NonSerializedObjects = (
"g_pTeamButton",
"g_pOptionsWindowBootButton",
"g_pOptionsWindowBanButton",
"g_pOptionsWindowPlayerMenu",
"g_pFragLimitText",
"g_pFragLimitButton",
)

MAX_FRAG_LIMIT						= 250
FRAG_LIMIT_INCRIMENT				= 25

g_iFragLimit = 150
#print "Menu Frag Data"

g_iUseScoreLimit = 0
g_fYPixelOffset = 0.0
g_fXPixelOffset = 0.0

g_iTeam = 1
g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

# Global pointers to user interface items
g_pTeamButton = None
g_pOptionsWindowBootButton = None
g_pOptionsWindowBanButton  = None
g_pOptionsWindowPlayerMenu = None
g_pFragLimitText = None
g_pFragLimitButton = None

# Mission specific events.  Start at 105
ET_BOOT_BUTTON_CLICKED = App.g_kVarManager.MakeEpisodeEventType(105)
ET_PLAYER_BUTTON_CLICKED = App.g_kVarManager.MakeEpisodeEventType(106)
ET_BAN_BUTTON_CLICKED = App.g_kVarManager.MakeEpisodeEventType(107)
ET_FRAG_LIMIT_CLICKED	= App.g_kVarManager.MakeEpisodeEventType(108)
ET_SELECT_TEAM			= App.g_kVarManager.MakeEpisodeEventType(150)


kFrigateList = [
	"Sabre",
	"Miranda",
	"Nova",
	"BirdOfPrey",
	"Talon",
	"Hideki",
	"Bug",
	"KazonRaider",
	"KrenimPatrol"]
	
kDestroyerList = [
	"Norway",
	"Steamrunner",
	"Constellation",
	"Kvort",
	"Falcon",
	"Rectangle",
	"HirogenHunter"]

kLightCruiserList = [
	"Centaur",
	"Defiant",
	"Intrepid",
	"KTinga",
	"Galor",
	"SonaCruiser",
	"HirogenHoloship",
	"KazonPredator",
	"KrenimWarship"]

kHeavyCruiserList = [
	"Excelsior",
	"ExcelsiorR",
	"Ambassador",
	"Keldon",
	"Breen",
	"Diamond",
	"Marauder",
	"KessokLight",
	"VidiianCruiser"]

kBattleCruiserList = [
	"Luna",
	"Akira",
	"Nebula",
	"Vorcha",
	"ObsidianKeldon",
	"SonaBattleship",
	"MalonFreighter"]

kDreadnoughtList = [
	"Galaxy",
	"Sovereign",
	"Valdore",
	"Sphere",
	"KessokHeavy",
	"HirogenVenatic"]

kBattleshipList = [
	"Prometheus",
	"SovereignR",
	"Neghvar",
	"Warbird",
	"CardHybrid",
	"Vorta"]

###############################################################################
#	BuildShipSelectWindow()	
#	
#	Build the stylized window from which the system can be selected
#	
#	Args:	TGPane					pMissionPane	- The pane to which our
#													events should be sent
#			TGLocalizationDatabase	pDatabase		- the database with our
#													text in it		
#	
#	Return:	A TGStylized window with a SubPane inside of it serving as a menu
###############################################################################
def RebuildShipSelectWindow():
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared
	import Multiplayer.SpeciesToShip

	import MainMenu.mainmenu
	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	# Find the Multiplayer window
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	# Get the mission pane
	pMissionPane = pMultWindow.GetMissionPane ()

	pDatabase = Multiplayer.MissionShared.g_pDatabase
	pWindow = Multiplayer.MissionMenusShared.g_pShipSelectWindow
	pSubPane = App.STSubPane_Cast (pWindow.GetNthChild (0))

	# Delete everything so we can readd the buttons.
	pSubPane.KillChildren ()

	pTier1Ships = App.STCharacterMenu_Create("4 Frag Points")
	pSubPane.AddChild (pTier1Ships, 0, 0, 0)
	pTier2Ships = App.STCharacterMenu_Create("6 Frag Points")
	pSubPane.AddChild (pTier2Ships, 0, 0, 0)
	pTier3Ships = App.STCharacterMenu_Create("9 Frag Points")
	pSubPane.AddChild (pTier3Ships, 0, 0, 0)
	pTier4Ships = App.STCharacterMenu_Create("13 Frag Points")
	pSubPane.AddChild (pTier4Ships, 0, 0, 0)
	pTier5Ships = App.STCharacterMenu_Create("18 Frag Points")
	pSubPane.AddChild (pTier5Ships, 0, 0, 0)
	pTier6Ships = App.STCharacterMenu_Create("24 Frag Points")
	pSubPane.AddChild (pTier6Ships, 0, 0, 0)
	pTier7Ships = App.STCharacterMenu_Create("31 Frag Points")
	pSubPane.AddChild (pTier7Ships, 0, 0, 0)


	#########################################
	# Create the buttons
	for iIndex in range(1, Multiplayer.SpeciesToShip.MAX_FLYABLE_SHIPS):
		# Setup the event for when this button is clicked
		pEvent = App.TGIntEvent_Create ()
		pEvent.SetEventType(Multiplayer.MissionMenusShared.ET_SELECT_SHIP_SPECIES)
		pEvent.SetInt(iIndex)		# store the index so we know which button was clicked.
		pEvent.SetDestination(pMissionPane)
	
		# Create the button.	
		pcName = Multiplayer.SpeciesToShip.GetNameFromSpecies (iIndex)
		pButton = App.STButton_CreateW (Multiplayer.MissionShared.g_pShipDatabase.GetString (pcName), pEvent)
		pEvent.SetSource (pButton)
		if (pcName in kFrigateList):
			pTier1Ships.AddChild(pButton, 0, 0, 0)		
		elif (pcName in kDestroyerList):
			pTier2Ships.AddChild(pButton, 0, 0, 0)		
		elif (pcName in kLightCruiserList):
			pTier3Ships.AddChild(pButton, 0, 0, 0)		
		elif (pcName in kHeavyCruiserList):
			pTier4Ships.AddChild(pButton, 0, 0, 0)		
		elif (pcName in kBattleCruiserList):
			pTier5Ships.AddChild(pButton, 0, 0, 0)		
		elif (pcName in kDreadnoughtList):
			pTier6Ships.AddChild(pButton, 0, 0, 0)		
		elif (pcName in kBattleshipList):
			pTier7Ships.AddChild(pButton, 0, 0, 0)		


	pSubPane.Resize(pSubPane.GetWidth(), pSubPane.GetTotalHeightOfChildren(), 0)
	pWindow.Layout()
	pWindow.InteriorChangedSize ()

	# Set the font back to normal
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	# clear the previously selected button
	Multiplayer.MissionMenusShared.g_pChosenSpecies = None

###############################################################################
#	BuildMission6Menu()
#	
#	Builds the Mission 5 options menu.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def BuildMission6Menus(bRebuild = 0):
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared

	# Find the Multiplayer window
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

	# Hide all the children so that only we will be visible.
	pMultWindow.HideAllChildren()

	pDatabase = Multiplayer.MissionShared.g_pDatabase
	
	# Create the mission menu
	pMissionPane = BuildMissionMenu (pMultWindow, pDatabase)
	pMultWindow.AddChild(pMissionPane)

	#Build the mission-specific pane that will get put inside of the options menu
	BuildMissionSpecificOptionsMenuPane(pMissionPane)

	# Build end game window.
	pMenu = Multiplayer.MissionMenusShared.BuildEndWindow(pMultWindow, pDatabase, 0)
	pMultWindow.AddChild(pMenu)
	pMenu.SetNotVisible();

	# Build the initial player list
	RebuildPlayerList()

	if (not bRebuild):
		# Make multiplayer window visible.
		pTopWindow.MoveToFront(pMultWindow)
		pMultWindow.SetVisible()

		# Hide the tactical menu
		pTactWindow = App.TacticalWindow_Cast(pTopWindow.FindMainWindow(App.MWT_TACTICAL))
		pTactWindow.SetNotVisible()

		pOptionsWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS);
		if pOptionsWindow.IsVisible():
			App.TopWindow_GetTopWindow().ToggleOptionsMenu()

	RebuildShipSelectWindow ()

###############################################################################
#	BuildMissionMenu()
#	
#	Builds the Mission menu.
#	
#	Args:	none
#	
#	Return:	none
###############################################################################
def BuildMissionMenu(pMultWindow, pDatabase):
	import MainMenu.mainmenu
	import Multiplayer.MissionMenusShared
	pMissionPane = Multiplayer.MissionMenusShared.BuildMissionMenu(pMultWindow, pDatabase,
		"Defend the Starbase Host", "Defend the Starbase Client", "Defend the Starbase Direct Host", 0)

	# We don't have frag limits in "Defend the Starbase"
#	Multiplayer.MissionMenusShared.g_pFragLimitText.SetDisabled(0)
#	Multiplayer.MissionMenusShared.g_pFragLimitButton.SetDisabled(0)
	
	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes] + 1)

	#########################################
	# Create team button

	# Get length of text for select team and time limit to determine which is longer.
	# we do this so we can position the buttons properly, with the proper alignment.

	pText = App.TGParagraph_CreateW(pDatabase.GetString("Select Team"))
	pText2 = App.TGParagraph_CreateW(pDatabase.GetString("Time Limit"))
	fWidth = pText.GetWidth()
	fWidth2 = pText2.GetWidth()
	if (fWidth2 > fWidth):
		fWidth = fWidth2

	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(ET_SELECT_TEAM)
	pEvent.SetDestination (pMissionPane)

	# The team caption
	pText.SetColor(App.g_kTitleColor)

	# The team button
	global g_pTeamButton
	g_pTeamButton = App.STRoundedButton_CreateW(pDatabase.GetString("Defenders"), pEvent, TEAM_TOGGLE_WIDTH, TEAM_TOGGLE_HEIGHT, 1)

	g_pTeamButton.SetColor(App.g_kTextEntryColor)
	g_pTeamButton.SetNormalColor(App.g_kMultiplayerButtonPurple)
	g_pTeamButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pTeamButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pTeamButton.SetTextColor(App.g_kSTMenuTextHighlightColor)
	g_pTeamButton.SetDisabledColor(App.g_kSTMenu1Disabled)
	g_pTeamButton.SetColorBasedOnFlags()
	pMissionPane.AddChild(g_pTeamButton, TEAM_PARA_X_POS + fWidth + 0.005, TEAM_TOGGLE_Y_POS, 0)
	App.g_kFocusManager.AddObjectToTabOrder(g_pTeamButton)


	if (App.g_kUtopiaModule.IsHost () and not App.g_kUtopiaModule.IsClient ()):
		# dedicated servers do not chose teams.
		g_pTeamButton.SetNotVisible ()	
	
	fPosDelta = (pText.GetHeight() - g_pTeamButton.GetHeight()) / 2.0
	pMissionPane.AddChild(pText, TEAM_PARA_X_POS + (fWidth - pText.GetWidth ()), TEAM_TOGGLE_Y_POS - fPosDelta, 0)
	
	# reposition the time limit button.
	pText = Multiplayer.MissionMenusShared.g_pTimeLimitText
	pButton = Multiplayer.MissionMenusShared.g_pTimeLimitButton

	pText.SetPosition(Multiplayer.MissionMenusShared.TIME_LIMIT_PARA_X_POS + (fWidth - pText.GetWidth ()), pText.GetTop (), 0)
	pButton.SetPosition(Multiplayer.MissionMenusShared.TIME_LIMIT_PARA_X_POS + fWidth + 0.005, pButton.GetTop (), 0)



	pEvent = App.TGEvent_Create ()
	pEvent.SetEventType(ET_FRAG_LIMIT_CLICKED)
	pEvent.SetDestination(pMissionPane)

	# The frag limit caption
	global g_pFragLimitText
	pText = None
	if (g_iUseScoreLimit):
		pText = App.TGParagraph_CreateW(pDatabase.GetString("Score Limit"))
	else:
		pText = App.TGParagraph_CreateW(pDatabase.GetString("Frag Limit"))
	pText.SetColor(App.g_kTitleColor)
	g_pFragLimitText = pText

	# The frag limit button
	global g_pFragLimitButton


	g_pFragLimitButton = App.STRoundedButton_CreateW(pDatabase.GetString("None"),
					 pEvent, FRAG_LIMIT_TOGGLE_WIDTH, FRAG_LIMIT_TOGGLE_HEIGHT, 1)
	g_pFragLimitButton.SetNormalColor(App.g_kSTMenu2NormalBase)          
	g_pFragLimitButton.SetHighlightedColor(App.g_kSTMenu2HighlightedBase)
	g_pFragLimitButton.SetSelectedColor(App.g_kSTMenu2Selected)          
	g_pFragLimitButton.SetTextColor(App.g_kSTMenuTextHighlightColor)
	g_pFragLimitButton.SetDisabledColor(App.g_kSTMenu1Disabled)
	g_pFragLimitButton.SetColorBasedOnFlags()
	pMissionPane.AddChild(g_pFragLimitButton, FRAG_LIMIT_PARA_X_POS + pText.GetWidth () + 0.005, FRAG_LIMIT_TOGGLE_Y_POS, 0)

	fPosDelta = (pText.GetHeight() - g_pFragLimitButton.GetHeight()) / 2.0
	pMissionPane.AddChild(pText, FRAG_LIMIT_PARA_X_POS, FRAG_LIMIT_TOGGLE_Y_POS - fPosDelta, 0) 

	if (not App.g_kUtopiaModule.IsHost ()):
		g_pFragLimitButton.SetDisabled ()

	global g_iFragLimit

	pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Frags")
	pcString = pString.GetCString ()
	pcSubString = pcString % str (g_iFragLimit)
	pString = App.TGString ()
	pString.SetString (pcSubString)
	g_pFragLimitButton.SetName(pString)
	Multiplayer.MissionMenusShared.g_pFragLimitButton.SetName(pString)

	# Add some mission specific handlers for the mission pane
	pMissionPane.AddPythonFuncHandlerForInstance(Multiplayer.MissionMenusShared.ET_FINISHED_SELECT, __name__ + ".FinishedSelectHandler")
	pMissionPane.AddPythonFuncHandlerForInstance(Multiplayer.MissionMenusShared.ET_SELECT_SHIP_SPECIES, __name__ + ".SelectSpeciesHandler")
	pMissionPane.AddPythonFuncHandlerForInstance(Multiplayer.MissionMenusShared.ET_SELECT_SYSTEM, __name__ + ".SelectSystemHandler")
	pMissionPane.AddPythonFuncHandlerForInstance(ET_SELECT_TEAM, __name__ + ".SelectTeamHandler")
	pMissionPane.AddPythonFuncHandlerForInstance(Multiplayer.MissionMenusShared.ET_FRAG_LIMIT_CLICKED, __name__ + ".HandleFragLimitClicked")
	pMissionPane.AddPythonFuncHandlerForInstance(ET_BOOT_BUTTON_CLICKED, __name__ + ".HandleBootButtonClicked")
	pMissionPane.AddPythonFuncHandlerForInstance(ET_BAN_BUTTON_CLICKED, __name__ + ".HandleBanButtonClicked")
	pMissionPane.AddPythonFuncHandlerForInstance(ET_PLAYER_BUTTON_CLICKED, __name__ + ".HandlePlayerButtonClicked")

	# Set the font back to normal small size
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])


	return pMissionPane



###############################################################################
#	HandleFragLimitClicked()
#	
#	Handle events for selection of a new system
#	
#	Args:	TGObject	pObject - Destination object for the event
#			TGEvent		pEvent  - Our event
#	
#	Return:	None
###############################################################################
def HandleFragLimitClicked(pObject, pEvent):
	import Multiplayer.MissionShared
	global g_iFragLimit
	
	pString = None
	pcSubString = None

	if g_iFragLimit >= MAX_FRAG_LIMIT:
		g_iFragLimit = 25
		pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Frags")
		pcString = pString.GetCString ()
		pcSubString = pcString % str (g_iFragLimit)
		g_pFragLimitButton.SetName(pString)
		pObject.CallNextHandler(pEvent)
	else:
		g_iFragLimit = g_iFragLimit + FRAG_LIMIT_INCRIMENT
		pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Frags")
		pcString = pString.GetCString ()
		pcSubString = pcString % str (g_iFragLimit)
		g_pFragLimitButton.SetName(pString)
		pObject.CallNextHandler(pEvent)

	pString = App.TGString ()
	pString.SetString (pcSubString)
	g_pFragLimitButton.SetName(pString)
	Multiplayer.MissionMenusShared.g_pFragLimitButton.SetName(pString)
		
	#print "Update Frag Limit"
	#print g_iFragLimit
	#print pcSubString


###############################################################################
#	HandlePlayerButtonClicked()
#	
#	A button on the scoreboard has been clicked. We must activate the boot
#	button (if the player is the host).
#	
#	Args:	TGObject*	pObject	- the mission pane
#			TGEvent*	pEvent	- our ET_PLAYER_BUTTON_CLICKED event
#	
#	Return:	None
###############################################################################
def HandlePlayerButtonClicked(pObject, pEvent):
	if App.g_kUtopiaModule.IsHost():
		g_pOptionsWindowBootButton.SetEnabled()
		g_pOptionsWindowBanButton.SetEnabled()

	global g_iIdOfCurrentlySelectedPlayer
	g_iIdOfCurrentlySelectedPlayer = pEvent.GetPlayerID()

	pObject.CallNextHandler(pEvent)


###############################################################################
#	HandleBootButtonClicked()
#	
#	The boot button has been clicked. Let the multiplayer window know, and set
#	the UI back up the way it was
#	
#	Args:	TGObject*	pObject	- the mission pane
#			TGEvent*	pEvent	- our ET_BOOT_BUTTON_CLICKED event
#	
#	Return:	None
###############################################################################
def HandleBootButtonClicked(pObject, pEvent):
	g_pOptionsWindowBootButton.SetDisabled()
	g_pOptionsWindowBanButton.SetDisabled()

	global g_iIdOfCurrentlySelectedPlayer
	
	if g_iIdOfCurrentlySelectedPlayer != App.TGNetwork.TGNETWORK_INVALID_ID:
		pTopWindow = App.TopWindow_GetTopWindow()
		pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
		pEvent = App.TGPlayerEvent_Create()
		pEvent.SetEventType(App.ET_PLAYER_BOOT_EVENT)
		pEvent.SetDestination(pMultWindow)
		pEvent.SetPlayerID(g_iIdOfCurrentlySelectedPlayer)
		App.g_kEventManager.AddEvent(pEvent)
	
	g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

	pObject.CallNextHandler(pEvent)

###############################################################################
#	HandleBanButtonClicked(pObject, pEvent)
#	
#	The ban button has been clicked. Do a normal boot, but also add the
#	player's IP to the ban list.
#	
#	Args:	pObject	- the mission pane
#			pEvent	- the ET_BAN_BUTTON_CLICKED event
#	
#	Return:	none
###############################################################################
def HandleBanButtonClicked(pObject, pEvent):
	g_pOptionsWindowBootButton.SetDisabled()
	g_pOptionsWindowBanButton.SetDisabled()

	global g_iIdOfCurrentlySelectedPlayer
	pNetwork = App.g_kUtopiaModule.GetNetwork()

	# Make sure we're valid, and that the selection is not the host/local player.
	if ((pNetwork == None) or 
		(g_iIdOfCurrentlySelectedPlayer == pNetwork.GetHostID()) or
	    (g_iIdOfCurrentlySelectedPlayer == pNetwork.GetLocalID())):
		g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID
		pObject.CallNextHandler(pEvent)
		return

	if g_iIdOfCurrentlySelectedPlayer != App.TGNetwork.TGNETWORK_INVALID_ID:
		pPlayerList = pNetwork.GetPlayerList()
		pPlayer = pPlayerList.GetPlayer(g_iIdOfCurrentlySelectedPlayer)

		if pPlayer:
			# Add them to the ban list.
			App.TGWinsockNetwork_BanPlayerByIP(pPlayer.GetNetAddress())

		# Now do a normal boot.
		pTopWindow = App.TopWindow_GetTopWindow()
		pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
		pEvent = App.TGPlayerEvent_Create()
		pEvent.SetEventType(App.ET_PLAYER_BOOT_EVENT)
		pEvent.SetDestination(pMultWindow)
		pEvent.SetPlayerID(g_iIdOfCurrentlySelectedPlayer)
		App.g_kEventManager.AddEvent(pEvent)

	g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

	pObject.CallNextHandler(pEvent)
		
###############################################################################
#	RebuildPlayerList()
#	
#	Update the scoreboard with the latest data
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def RebuildPlayerList():
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared

	# We don't want to refresh the player list when the Game Over screen is up
	# 'cuz that can sometimes break the game over screen
	if Multiplayer.MissionShared.g_bGameOver:
		return

	import Mission6
	import Multiplayer.MissionShared
	import MainMenu.mainmenu
	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if (not pNetwork):
		# Don't rebuild the list since you can't
		return

	pGame = App.Game_GetCurrentGame ()
	if (not pGame):
		# Game over.  Can't rebuild list.
		return

	pDatabase = Multiplayer.MissionShared.g_pDatabase

	pMultGame = App.MultiplayerGame_Cast (pGame)

	# Find the Multiplayer window
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	
	pEndPane = App.TGPane_Cast (pMultWindow.GetEndWindow ())
	pSortList = []
	pTeamScoresList = []

	pTeamScoresDict = Mission6.g_kTeamScoreDictionary
	pTeamKillsDict = Mission6.g_kTeamKillsDictionary

	if (pEndPane):
		# Get the menu
		import Multiplayer.MissionMenusShared
		pPane = Multiplayer.MissionMenusShared.g_pEndPlayerListPane
		pStyleWindow = Multiplayer.MissionMenusShared.g_pEndPlayerListWindow
		pMenu = Multiplayer.MissionMenusShared.g_pEndPlayerListMenu

#		print ("Rebuilding player list.got menu")

		# Kill all the children.		
		pMenu.KillChildren ()

		# Reconstruct the menu, first storing it in a python list.
		pDict = Mission6.g_kKillsDictionary

		pPlayerList = pNetwork.GetPlayerList ()
		iNumPlayers = pPlayerList.GetNumPlayers ()
		i = 0
		while (i < iNumPlayers):
			pPlayer = pPlayerList.GetPlayerAtIndex (i)
			
			if (pMultGame):
				if (pDict.has_key (pPlayer.GetNetID ()) and pPlayer.IsDisconnected () == 0):
					# This is an actual player in the game.  Add him to the sort list for
					# later sorting/
					pSortList.append (pPlayer)

			# Increment the index to look at the next player.				
			i = i + 1

		# Okay, now we have a list of all the players in the game.  Sort it
		# using the ComparePlayer function to do comparisons.
		pSortList.sort (ComparePlayer)

		# Sort the team scores
		for iTeam in pTeamScoresDict.keys ():
			pTeamScoresList.append (iTeam)
		pTeamScoresList.sort (CompareTeams)

		pTeamDict = Mission6.g_kTeamDictionary 

		# Find out how many players are on each team
		pNumPlayersOnTeam = {}
		for iTeam in pTeamScoresList:
			pNumPlayersOnTeam[iTeam] = 0
			for pPlayer in pSortList:
				if pTeamDict.has_key(pPlayer.GetNetID()):
					iPlayerTeam = pTeamDict[pPlayer.GetNetID()]
					if (iPlayerTeam == iTeam):
						pNumPlayersOnTeam[iTeam] = pNumPlayersOnTeam[iTeam] + 1
						
		# Okay, now build the team scores
		for iTeam in pTeamScoresList:
			if pNumPlayersOnTeam[iTeam] < 1:
				continue
			
			if (iTeam == 1):
				pcTeamName = "Defenders"
				pcTeamName = pDatabase.GetString(pcTeamName).GetCString()

				if (g_iFragLimit != -1):

					iShipsLeft = g_iFragLimit

					pcShipsLeft = pDatabase.GetString ("Ships Left").GetCString ()
					pcNewString = pcShipsLeft % (str (iShipsLeft))
					pcTeamName = pcTeamName + " - " + pcNewString
			else:
				pcTeamName = "Attackers"
				pcTeamName = pDatabase.GetString(pcTeamName).GetCString()

			pPane = CreateTeamScoreEntry(pcTeamName)
			pMenu.AddChild (pPane, 0, 0, 0)

			# Add the top 3 performers for that team.
			iCount = 0
			for pPlayer in pSortList:
				iPlayerTeam = Mission6.INVALID_TEAM
				if (pTeamDict.has_key (pPlayer.GetNetID ())):
					iPlayerTeam = pTeamDict [pPlayer.GetNetID ()]

				if (iPlayerTeam == iTeam):
					# This is a top performer on this team.
					pTeamAcePane = App.TGPane_Create (0.4, 0.1)

					pPane = CreateTeamAceEntry (pPlayer)
					pTeamAcePane.AddChild (pPane, 0.02, 0, 0)
					pTeamAcePane.Resize (pTeamAcePane.GetWidth (), pPane.GetHeight (), 0)

					pMenu.AddChild (pTeamAcePane, 0, 0, 0)

					iCount = iCount + 1

					if (iCount == 3):
						# Only show the top two performers
						break;

		# Now add in your own performance.
		pPlayer = pPlayerList.GetPlayer (pNetwork.GetLocalID ())
		if (pPlayer):
			pPane = CreatePlayerScoreEntry (pPlayer)
			pMenu.AddChild (pPane, 0.0, 0.0)

		# Now call layout on the entire menu.
		pMenu.Layout ()
		pStyleWindow.InteriorChangedSize ()

	# Also rebuild the scoreboard in the Options Window

	if g_pOptionsWindowPlayerMenu:

		# Set the font larger
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
					MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

		g_pOptionsWindowPlayerMenu.KillChildren()
		
		# First add an empty pane the height of an entry to push the other entries
		# down so that the top of the list is not covered by the headers
		g_pOptionsWindowPlayerMenu.AddChild(App.TGPane_Create(0.4, 0.04), 0.0, 0.0, 0)
		
		# Build the scoreboard that goes in the options window
		for iTeam in pTeamScoresList:
			if pNumPlayersOnTeam[iTeam] < 1:
				continue
#			print "Rebuilding the scoreboard in the Options Window. Creating team score entry."
			
			if (iTeam == 1):
				pcTeamName = "Defenders"
				pcTeamName = pDatabase.GetString(pcTeamName).GetCString()

				if (g_iFragLimit != -1):
					# there is a frag limit.  Append string that tells how
					# many ships left.
					iKilled = 0
					if (pTeamKillsDict.has_key (0)):
						iKilled = pTeamKillsDict [0]
					iShipsLeft = g_iFragLimit

					pcShipsLeft = pDatabase.GetString ("Ships Left").GetCString ()
					pcNewString = pcShipsLeft % (str (iShipsLeft))
					pcTeamName = pcTeamName + " - " + pcNewString
			else:
				pcTeamName = "Attackers"
				pcTeamName = pDatabase.GetString(pcTeamName).GetCString()

			pPane = CreateScoreboardTeamScoreEntry(pcTeamName)
			g_pOptionsWindowPlayerMenu.AddChild(pPane, 0, 0, 0)
			
			for pPlayer in pSortList:
				if pTeamDict.has_key(pPlayer.GetNetID()):
					iPlayerTeam = pTeamDict[pPlayer.GetNetID()]
					if (iPlayerTeam == iTeam):
#						print "Rebuilding the scoreboard in the Options Window. Creating player score entry."
						pPane = CreateScoreboardPlayerScoreEntry(pPlayer)
						g_pOptionsWindowPlayerMenu.AddChild(pPane, 0.0, 0.0, 0)

		# Now layout the menu. No need to call InteriorChangedSize on its parent because
		# it's an STSubPane and knows to handle that on its own.
		g_pOptionsWindowPlayerMenu.Layout()

		# Set the font back to the flight size
		App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Disable the boot button, since the player it's set to boot may no longer be
	# around
	if g_pOptionsWindowBootButton:
		g_pOptionsWindowBootButton.SetDisabled()
	if g_pOptionsWindowBanButton:
		g_pOptionsWindowBanButton.SetDisabled()

	# Now rebuild the info pane
	RebuildInfoPane ()

	# Close and open the score window so it'll properly re-lay itself out
	DoScoreWindow()
	DoScoreWindow()

###############################################################################
#	CreateScoreboardPlayerScoreEntry()
#	
#	Create a player info entry for the scoreboard that's in the options window
#	
#	Args:	pPlayer		- the player
#	
#	Return:	A TGPane* containing a player info entry
###############################################################################
def CreateScoreboardPlayerScoreEntry(pPlayer):
	import Mission6
	import MainMenu.mainmenu
	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Initialize some globals
	# create a pane to hold everything.
	pPlayerEntryPane = App.TGPane_Create(0.5, 0.04)

	# Create the event that gets sent that can be used for booting a player
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	pEvent = App.TGPlayerEvent_Create()
	pEvent.SetEventType(ET_PLAYER_BUTTON_CLICKED)
	pEvent.SetDestination(pMultWindow.GetMissionPane())
	iPlayerID = pPlayer.GetNetID()
	pEvent.SetPlayerID(iPlayerID)

	# Create the player name text
	pButton = App.STButton_CreateW(pPlayer.GetName(), pEvent, 0,
								0.185, 0.04)
	pButton.SetNormalColor(App.g_kSTMenu4NormalBase)
	pButton.SetHighlightedColor(App.g_kSTMenu4HighlightedBase)
	pButton.SetSelectedColor(App.g_kSTMenu4Selected)
	pButton.SetColorBasedOnFlags()
	pPlayerEntryPane.PrependChild(pButton, 0.03, 0.0, 0)
	
	# create kills
	# Get the kill total from the score dictionaries
	pDict = Mission6.g_kKillsDictionary

	iKills = 0
	if (pDict.has_key (iPlayerID)):
		iKills = pDict [iPlayerID]

	pText = App.TGTextButton_Create(str(iKills))
	pText.AlignTextHorizontal(App.TGTextButton.ALIGN_CENTER, 0)
	pText.AlignTextVertical(App.TGTextButton.ALIGN_MIDDLE, 0)
	pText.Resize(0.065, 0.04, 0)
	pPlayerEntryPane.PrependChild(pText, 0.25, 0.0, 0)

	# Create death total
	# Get the death total from the score dictionaries
	pDict = Mission6.g_kDeathsDictionary

	iDeaths = 0
	if (pDict.has_key (iPlayerID)):
		iDeaths = pDict [iPlayerID]

	pText = App.TGTextButton_Create(str(iDeaths))
	pText.AlignTextHorizontal(App.TGTextButton.ALIGN_CENTER, 0)
	pText.AlignTextVertical(App.TGTextButton.ALIGN_MIDDLE, 0)
	pText.Resize(0.065, 0.04, 0)
	pPlayerEntryPane.PrependChild(pText, 0.325, 0.0, 0)

	return pPlayerEntryPane

def CreateScoreboardTeamScoreEntry(pcString):
	import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# create a pane to hold everything.
	pTeamEntryPane = App.TGPane_Create(0.4, 0.1)

	pText = App.TGParagraph_Create(pcString)
	pText.SetColor(App.g_kTitleColor)
	pTeamEntryPane.AddChild(pText, 0, 0, 0)

	# Resize the team entry pane
	fHeight = pText.GetHeight ()
	pTeamEntryPane.Resize (0.4, fHeight, 0)

	return pTeamEntryPane

def CreateTeamScoreEntry (pcString):
	import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# create a pane to hold everything.
	pTeamEntryPane = App.TGPane_Create (0.4, 0.1)

	pText = App.TGParagraph_Create(pcString)
	pTeamEntryPane.AddChild(pText, 0, 0, 0)

	# Resize the team entry pane
	fHeight = pText.GetHeight ()
	pTeamEntryPane.Resize (0.4, fHeight * 2.0, 0)

	# Create the top performer entry
	pText = App.TGParagraph_CreateW(pDatabase.GetString ("Team Ace"))
	pTeamEntryPane.AddChild(pText, 0.01, fHeight, 0)

	return pTeamEntryPane

def CreateTeamAceEntry (pPlayer):
	import Mission6
	import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Create the player name text
	pPane = App.TGPane_Create (0.38, 0.1)

	pString = pDatabase.GetString ("Starbase Team Player")
	pcString = pString.GetCString ()

	pName = pPlayer.GetName ()
	pcName = pName.GetCString ()

	iPlayerID = pPlayer.GetNetID ()

	# Get the kill total from the score dictionaries
	pDict = Multiplayer.Episode.Mission6.Mission6.g_kKillsDictionary

	iKills = 0
	if (pDict.has_key (iPlayerID)):
		iKills = pDict [iPlayerID]

	pcKills = str (iKills)

	# Create the death count
	# Get the death total from the score dictionaries
	pDict = Multiplayer.Episode.Mission6.Mission6.g_kDeathsDictionary

	iDeaths = 0
	if (pDict.has_key (iPlayerID)):
		iDeaths = pDict [iPlayerID]

	pcDeaths = str (iDeaths)

	pcSubString = pcString % (pcName, pcKills, pcDeaths)

	pText = App.TGParagraph_Create (pcSubString)

	pPane.AddChild (pText, 0, 0, 0)
	fHeight = pText.GetHeight ()
	pPane.Resize (0.38, fHeight, 0)

	return pPane
					
def CreatePlayerScoreEntry (pPlayer):
	import Mission6
	import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Create the player name text
	pPane = App.TGPane_Create (0.40, 0.1)

	pString = pDatabase.GetString ("Starbase Your Stats")
	pcString = pString.GetCString ()

	iPlayerID = pPlayer.GetNetID ()

	# Get the kill total from the score dictionaries
	pDict = Multiplayer.Episode.Mission6.Mission6.g_kKillsDictionary

	iKills = 0
	if (pDict.has_key (iPlayerID)):
		iKills = pDict [iPlayerID]

	pcKills = str (iKills)

	# Create the death count
	# Get the death total from the score dictionaries
	pDict = Multiplayer.Episode.Mission6.Mission6.g_kDeathsDictionary

	iDeaths = 0
	if (pDict.has_key (iPlayerID)):
		iDeaths = pDict [iPlayerID]

	pcDeaths = str (iDeaths)

	pcSubString = pcString % (pcKills, pcDeaths)

	pText = App.TGParagraph_Create (pcSubString)

	pPane.AddChild (pText, 0, 0, 0)
	fHeight = pText.GetHeight ()
	pPane.Resize (0.4, fHeight, 0)

	return pPane
					


def ComparePlayer (pThisPlayer, pOtherPlayer):
	import Mission6
	# Get the kills of this player and the other player.
	iThisID = pThisPlayer.GetNetID ()
	iOtherID = pOtherPlayer.GetNetID ()

	# Get the kill total from the score dictionaries
	pDict = Mission6.g_kScoresDictionary

	iThisScore = 0
	iOtherScore = 0

	if (pDict.has_key (iThisID)):
		iThisScore = pDict [iThisID]

	if (pDict.has_key (iOtherID)):
		iOtherScore = pDict [iOtherID]
	
	# reverse sort.  Higher kills get sorted higher.
	if (iThisScore < iOtherScore):
		return 1
	elif (iThisScore == iOtherScore):
		pKillsDict = Mission6.g_kKillsDictionary

		iThisKills = 0
		iOtherKills = 0
		if (pKillsDict.has_key (iThisID)):
			iThisKills = pKillsDict [iThisID]

		if (pKillsDict.has_key (iOtherID)):
			iOtherKills = pKillsDict [iOtherID]
		
		# We want lower deaths to get sorted higher
		if (iThisKills < iOtherKills):
			return -1
		elif (iThisKills > iOtherKills):
			return 1
		else:
			return 0
	else:
		return -1


def CompareTeams (iThisTeam, iOtherTeam):
	import Mission6
	# Get the score total from the teamscore dictionaries
	pDict = Mission6.g_kTeamScoreDictionary

	iThisScore = 0
	iOtherScore = 0

	if (pDict.has_key (iThisTeam)):
		iThisScore = pDict [iThisTeam]

	if (pDict.has_key (iOtherTeam)):
		iOtherScore = pDict [iOtherTeam]
	
	# reverse sort.  Higher kills get sorted higher.
	if (iThisScore < iOtherScore):
		return 1
	elif (iThisScore == iOtherScore):
		if iThisTeam < iOtherTeam:
			return -1
		else:
			return 1
	else:
		return -1

# These must be here cause they are called by other scripts and by code.
def DoScoreWindow ():
	import Multiplayer.MissionMenusShared
	Multiplayer.MissionMenusShared.DoScoreWindow ()
	return 0

def DoEndGameDialog (bRestartable = 0):
	import Multiplayer.MissionMenusShared
	Multiplayer.MissionMenusShared.DoEndGameDialog (bRestartable)
	return 1

###############################################################################
#	SelectSpeciesHandler()
#	
#	Handle events for selection of a new system
#	
#	Args:	TGObject	pObject - destination object for the event
#			TGIntEvent	pEvent  - The Int in this event is the index of our new
#									species
#	
#	Return:	None
###############################################################################
def SelectSpeciesHandler (TGObject, pEvent):
	import Multiplayer.MissionMenusShared
	# Set the global species selected number.
	Multiplayer.MissionMenusShared.SelectSpecies (pEvent.GetInt ())

	# make the previously select button not chosen
	if (Multiplayer.MissionMenusShared.g_pChosenSpecies):
		Multiplayer.MissionMenusShared.g_pChosenSpecies.SetChosen (0)

	# Set the button that was clicked chosen, so it will have a different color.
	pButton = App.STButton_Cast (pEvent.GetSource ())
	pButton.SetChosen (1)
	Multiplayer.MissionMenusShared.g_pChosenSpecies = pButton

	# Make the start button visible if system and ship selected
	UpdateStartButton()

	TGObject.CallNextHandler(pEvent)

###############################################################################
#	SelectSystemHandler()
#	
#	Handle events for selection of a new system
#	
#	Args:	TGObject	pObject - destination object for the event
#			TGIntEvent	pEvent  - The Int in this event is the index of our new
#									system
#	
#	Return:	None
###############################################################################
def SelectSystemHandler(pObject, pEvent):
	import Multiplayer.MissionMenusShared
	# Set the global species selected number.
	Multiplayer.MissionMenusShared.SelectSystem (pEvent.GetInt ())

	# make the previously select button not chosen
	if (Multiplayer.MissionMenusShared.g_pChosenSystem):
		Multiplayer.MissionMenusShared.g_pChosenSystem.SetChosen (0)

	# Set the button that was clicked chosen, so it will have a different color.
	pButton = App.STButton_Cast (pEvent.GetSource ())
	pButton.SetChosen (1)
	Multiplayer.MissionMenusShared.g_pChosenSystem = pButton

	# Make the start button visible if system and ship selected
	UpdateStartButton()

	pObject.CallNextHandler(pEvent)

def FinishedSelectHandler (TGObject, pEvent):
	# Allow the Options Window to come up
#	App.TopWindow_GetTopWindow().AllowShowOptionsWindow(1)

	import Multiplayer.MissionMenusShared
	import Mission6
	# Find the Multiplayer window
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

	# Get the mission pane and hide it.
	pMissionPane = pMultWindow.GetMissionPane ()
	pMissionPane.SetNotVisible ()

	# Send event to host telling him what team we've selected
	if (App.g_kUtopiaModule.IsClient ()):
		pNetwork = App.g_kUtopiaModule.GetNetwork ()
		if (pNetwork):
			pMessage = App.TGMessage_Create ()
			pMessage.SetGuaranteed (1)		# Yes, this is a guaranteed packet
			
			# Setup the stream.
			kStream = App.TGBufferStream ()		# Allocate a local buffer stream.
			kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
			
			# Write relevant data to the stream.
			# First write message type.
			kStream.WriteChar (chr (Mission6.TEAM_MESSAGE))

			# Write this player's id
			kStream.WriteLong (pNetwork.GetLocalID ())

			# Write the team selected
			kStream.WriteChar (chr (g_iTeam))

			# Okay, now set the data from the buffer stream to the message
			pMessage.SetDataFromStream (kStream)

			# Send the message.
			pNetwork.SendTGMessage (pNetwork.GetHostID (), pMessage)

			# We're done.  Close the buffer.
			kStream.CloseBuffer ()

	# Start the mission
	StartMission (Multiplayer.MissionMenusShared.g_iSpecies, Multiplayer.MissionMenusShared.g_iSystem)

	# If we're dedicated server, bring up the options window
	if (App.g_kUtopiaModule.IsHost () and (not App.g_kUtopiaModule.IsClient ())):
		# Bring up options again.
		# Find the multiplayer window
		pTopWindow = App.TopWindow_GetTopWindow()
		pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

		# Hide all panes, make MultiplayerPane visible.
		pMultWindow.HideAllChildren ()

		# Hide the entire window and make options window visible.
		pMain = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
		pMain.SetVisible ()
		pTopWindow.MoveToFront (pMain)
	else:		
		# Assign myself to this team
		Mission6.g_kTeamDictionary [pNetwork.GetLocalID ()] = g_iTeam

	TGObject.CallNextHandler(pEvent)


###############################################################################
#	ResetLimitInfo()	
#	
#	Updates the user interface's limit buttons (time, frag, num players) to
#	reflect the accurate values of this information
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def ResetLimitInfo():
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared
	
	# player limit
	pcString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Players").GetCString()
	pcString = pcString % str(Multiplayer.MissionMenusShared.g_iPlayerLimit)
	pString = App.TGString(pcString)
	Multiplayer.MissionMenusShared.g_pPlayerLimitButton.SetName(pString)

	# time limit
	if (Multiplayer.MissionMenusShared.g_iTimeLimit == -1):
		Multiplayer.MissionMenusShared.g_pTimeLimitButton.SetName(Multiplayer.MissionShared.g_pDatabase.GetString("None"))
	else:
		pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Minutes")
		pcString = pString.GetCString ()

		pcSubString = pcString % str (Multiplayer.MissionMenusShared.g_iTimeLimit)

		pNewString = App.TGString ()
		pNewString.SetString (pcSubString)

		Multiplayer.MissionMenusShared.g_pTimeLimitButton.SetName(pNewString)




	# Frag limit
	if (g_iFragLimit == -1):
		Multiplayer.MissionMenusShared.g_pFragLimitButton.SetName(Multiplayer.MissionShared.g_pDatabase.GetString("None"))
	else:
		pString = None
		pcSubString = None
		if (Multiplayer.MissionMenusShared.g_iUseScoreLimit):
			pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Points")
			pcString = pString.GetCString ()
			pcSubString = pcString % str (g_iFragLimit * 10000)
		else:
			pString = Multiplayer.MissionShared.g_pDatabase.GetString("Num Frags")
			pcString = pString.GetCString ()
			pcSubString = pcString % str (g_iFragLimit)

		pNewString = App.TGString ()
		pNewString.SetString (pcSubString)

		Multiplayer.MissionMenusShared.g_pFragLimitButton.SetName(pNewString)


def UpdateStartButton():
	import Multiplayer.MissionMenusShared
	if App.g_kUtopiaModule.IsHost() and (not App.g_kUtopiaModule.IsClient()):
		if Multiplayer.MissionMenusShared.g_iSystem != 0:
			Multiplayer.MissionMenusShared.g_pStartButton.SetEnabled ()
			return
	else:
		if Multiplayer.MissionMenusShared.g_iSpecies != 0 and Multiplayer.MissionMenusShared.g_iSystem != 0:
			Multiplayer.MissionMenusShared.g_pStartButton.SetEnabled()
			return

	# if we get here, the start button should be disabled since something wasn't
	# selected yet.
	Multiplayer.MissionMenusShared.g_pStartButton.SetDisabled()
	return		

def StartMission (iSpecies, iSystem):
	import Multiplayer.MissionMenusShared
	import Multiplayer.SpeciesToShip
	import Multiplayer.SpeciesToSystem
	import Multiplayer.MissionShared
	import MainMenu.mainmenu
	# Specify (and load if necessary) our bridge
 
	# Get the current game.  We use this in various places below.
	pGame = App.Game_GetCurrentGame ()
	pMultGame = App.MultiplayerGame_Cast (pGame)	# Cast the game to a multiplayer game

	# Access the global variable that was created in Multiplayer.MissionShared.py to
	# get the pointer to the starting set.
	if (App.g_kUtopiaModule.IsHost ()):
		# If we're the host, create the starting set here if we haven't already started the game.
		# After teh game is started, we cannot change regions.
		if (not Multiplayer.MissionMenusShared.g_bGameStarted):
			pSet = Multiplayer.SpeciesToSystem.CreateSystemFromSpecies (iSystem)
			Multiplayer.MissionShared.g_pStartingSet = pSet
		else:
			pSet = Multiplayer.MissionShared.g_pStartingSet

		# Create the starbase
		import Mission6
		Mission6.CreateStarbase()
	else:
		# The staring set should have been send to us from the host.
		# Use it here.
		pSet = Multiplayer.MissionShared.g_pStartingSet

	if (App.IsNull (pSet)):
#		print ("Set is NULL!")
		return

	###################################################
	#This next section will create the ships and set their stats

	#Determine if we need to create the player's ship.
	if (iSpecies != Multiplayer.SpeciesToShip.UNKNOWN):
		# We've got a valid species.  Create the player's ship.
		pPlayer = Multiplayer.MissionMenusShared.CreateShip (iSpecies)

		if (pPlayer != None):
			pPlayer.RandomOrientation ()
			pPlayer.UpdateNodeOnly ()

			pNetwork = App.g_kUtopiaModule.GetNetwork ()
			if (pNetwork):
				pPlayer.SetNetPlayerID (pNetwork.GetLocalID ())

			# Get the player's name from the network.
			pNetwork = App.g_kUtopiaModule.GetNetwork ()
			if (not App.IsNull (pNetwork)):
				pcName = pNetwork.GetCName ()
			else:
				pcName = "N/A"

			# Determine if there is already a ship with the same name.
			pcOrigName = pcName
			i = 0
			iCount = 1
			while (i == 0):
				pObj = App.BaseObjectClass_GetObject (None, pcName)
				if (pObj):
					# Yes, an object already exists.  We need to create
					# a new name
					pcName = pcOrigName
					pcName = pcName + str (iCount)
					iCount = iCount + 1
				else:
					i = 1

			# randomly locate the player's ship.
			fRadius = pPlayer.GetRadius () * 1.25

			kPos = Multiplayer.MissionMenusShared.FindGoodLocation (pSet, fRadius)

			pPlayer.SetTranslate (kPos)

			# Add the ship to the set.
			pSet.AddObjectToSet (pPlayer, pcName)

			pMultGame.SetPlayer(pPlayer)

			# Remove phased plasma torpedos.
			pTorpSys = pPlayer.GetTorpedoSystem()
			if(pTorpSys):
				# Find proper torps..
				iNumTypes = pTorpSys.GetNumAmmoTypes()
				for iType in range(iNumTypes):
					pTorpType = pTorpSys.GetAmmoType(iType)
					if (pTorpType.GetAmmoName() == "Phased"):
						pTorpSys.RemoveAmmoType (iType)

			# Add event handler for when this ship is destroyed.
			# Find the Multiplayer window
			pTopWindow = App.TopWindow_GetTopWindow()
			pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))

			# Add broadcast handler for when an object is destroyed.  This handler will bring up the mission pane
			# again if the player's ship is destroyed.
			pMissionPane = pMultWindow.GetMissionPane ()
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_DELETE_OBJECT_PUBLIC, pMissionPane, "Multiplayer.MissionMenusShared.ObjectDestroyedHandler", pPlayer)


	# Hide select region menu and move ship selection menu into it's proper place
	pTopWindow = App.TopWindow_GetTopWindow()
	if (App.g_kUtopiaModule.IsHost ()):
		Multiplayer.MissionMenusShared.g_pSystemPane.SetNotVisible ()
		Multiplayer.MissionMenusShared.g_pSystemIcon.SetNotVisible ()
		Multiplayer.MissionMenusShared.g_pSystemDescPane.SetNotVisible ()

		Multiplayer.MissionMenusShared.g_pInfoPane.SetVisible ()

		if (not App.g_kUtopiaModule.IsClient ()):
			# Dedicated server.  Disable options toggling.
			pTopWindow.DisableOptionsMenu (1)	
			pResumeButton = App.STRoundedButton_Cast(App.TGObject_GetTGObjectPtr(MainMenu.mainmenu.g_idResumeButton))
			if (pResumeButton):
				pResumeButton.SetDisabled ()

	# Force tactical view
	if (App.g_kUtopiaModule.IsClient ()):
		# Now force tactical view.
		pTopWindow.ForceTacticalVisible ()

	# Ready for new players to join.  Notify the game of this.
	if (App.g_kUtopiaModule.IsHost ()):
		if (not pMultGame.IsReadyForNewPlayers ()):
			pMultGame.SetReadyForNewPlayers (1)				# Set flag to ready

		if (not Multiplayer.MissionMenusShared.g_bGameStarted):
			# Set time left for this mission if there's a time limit.
			if (Multiplayer.MissionMenusShared.g_iTimeLimit != -1):
				Multiplayer.MissionShared.CreateTimeLeftTimer (Multiplayer.MissionMenusShared.g_iTimeLimit * 60)
			Multiplayer.MissionMenusShared.g_bGameStarted = 1

	# rebuild the scoreboard to accurately display things
	RebuildPlayerList ()

def SelectTeamHandler (pSelf, pEvent):
	import Multiplayer.MissionShared
	import MainMenu.mainmenu

	pDatabase = Multiplayer.MissionShared.g_pDatabase

	global g_iTeam
	g_iTeam = 1	
	if (g_iTeam > 1):
		g_iTeam = 1

	# Update interface.
	if (g_iTeam == 0):
		g_pTeamButton.SetName (pDatabase.GetString ("Attackers"))
	else:
		g_pTeamButton.SetName (pDatabase.GetString ("Defenders"))

	pSelf.CallNextHandler (pEvent)
	return 0

# New version		
def RebuildInfoPane ():
	import Mission6
	import Multiplayer.SpeciesToSystem
	import Multiplayer.MissionMenusShared
	import MainMenu.mainmenu
	import Multiplayer.MissionShared
#	print ("Rebuilding info pane")
	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if (not pNetwork):
		# Don't rebuild the list since you can't
		return

	pDatabase = Multiplayer.MissionShared.g_pDatabase

	pOrigFontGroup = App.g_kFontManager.GetDefaultFont ()

	# Set the font small
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Kill all the children in the info pane, since we will be rebuilding it from scratch.
	Multiplayer.MissionMenusShared.g_pInfoPane.KillChildren ()
	
	pText = App.TGParagraph_CreateW (Multiplayer.MissionShared.g_pDatabase.GetString("Mission System"))
	pText.SetColor (App.g_kTitleColor)
	Multiplayer.MissionMenusShared.g_pInfoPane.AddChild (pText, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_X_POS, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS - pText.GetHeight () - 0.005, 0)
	fWidth = pText.GetWidth ()

	if (Multiplayer.MissionMenusShared.g_iSystem != 0):
		pText = App.TGParagraph_CreateW (Multiplayer.MissionShared.g_pSystemDatabase.GetString (Multiplayer.SpeciesToSystem.GetScriptFromSpecies (Multiplayer.MissionMenusShared.g_iSystem)))
	else:
		pText = App.TGParagraph_CreateW (pDatabase.GetString("Unknown"))

		pText.SetColor (App.g_kSTMenuTextHighlightColor)
	Multiplayer.MissionMenusShared.g_pInfoPane.AddChild (pText, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_X_POS + fWidth + 0.005, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS - pText.GetHeight () - 0.005, 0)

	# Build the stylized window.
	fHeight = Multiplayer.MissionMenusShared.SYSTEM_DESC_WINDOW_Y_POS + Multiplayer.MissionMenusShared.SYSTEM_DESC_WINDOW_HEIGHT - Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS
	pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", pDatabase.GetString("Players In Game"), 
						0.0, 0.0, None, 1, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, fHeight)
	pWindow.SetTitleBarThickness(Multiplayer.MissionMenusShared.SYSTEM_WINDOW_BAR_THICKNESS)
	Multiplayer.MissionMenusShared.g_pInfoPane.AddChild (pWindow, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_X_POS, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_Y_POS, 0)

	# Build player list pane.
	pListPane = App.STSubPane_Create (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, 500.0)
	
	pMultGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())

	# Display the team
	iTeam = 0

	pTeamScoresDict = Mission6.g_kTeamScoreDictionary
	pTeamKillsDict = Mission6.g_kTeamKillsDictionary
	pTeamDict = Mission6.g_kTeamDictionary 

	for iTeam in range (0, 2):
		if (iTeam == 1):
			pcTeamName = "Defenders"
			pcTeamName = pDatabase.GetString(pcTeamName).GetCString ()

			if (g_iFragLimit != -1):
				# there is a frag limit.  Append string that tells how
				# many ships left.
				iKilled = 0
				if (pTeamKillsDict.has_key (0)):
					iKilled = pTeamKillsDict [0]
				iShipsLeft = g_iFragLimit

				pcShipsLeft = pDatabase.GetString ("Ships Left").GetCString ()
				pcNewString = pcShipsLeft % (str (iShipsLeft))
				pcTeamName = pcTeamName + " - " + pcNewString
		else:
			pcTeamName = "Attackers"
			pcTeamName = pDatabase.GetString(pcTeamName).GetCString ()

		pText = App.TGParagraph_Create(pcTeamName)
		pListPane.AddChild (pText, 0, 0, 0)

		# Display the players on this team.
		pPlayerList = pNetwork.GetPlayerList ()
		iNumPlayers = pPlayerList.GetNumPlayers ()
		i = 0
		while (i < iNumPlayers):
			pPlayer = pPlayerList.GetPlayerAtIndex (i)
			
			if (pTeamDict.has_key (pPlayer.GetNetID ()) and pPlayer.IsDisconnected () == 0):
				 # This player is on a team.  See if he's on my team.
				 if (pTeamDict [pPlayer.GetNetID ()] == iTeam):
					pPane = CreatePlayerInfoEntry (pPlayer, pMultGame)

					pListPane.AddChild (pPane, 0.05, 0, 0)

			# Increment the index to look at the next player.				
			i = i + 1

	pListPane.Resize (pListPane.GetWidth (), pListPane.GetTotalHeightOfChildren (), 0)

	pWindow.AddChild (pListPane, 0, 0, 0)	
	pWindow.Layout()
	pWindow.InteriorChangedSize ()
	
	# Restore default font
	App.g_kFontManager.SetDefaultFont(pOrigFontGroup.GetFontName (), pOrigFontGroup.GetFontSize ())

	Multiplayer.MissionMenusShared.g_pInfoPane.Layout ()


def CreatePlayerInfoEntry (pPlayer, pMultGame):
	import Mission6
	import Multiplayer.SpeciesToShip
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared
	# create a pane to hold everything.
	pPlayerEntryPane = App.TGPane_Create (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, 0.1)

	pDatabase = Multiplayer.MissionShared.g_pDatabase

	# Create the player name text
#	pPane = App.TGPane_Create (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH - 0.1, 0.1)
	pPane = App.TGPane_Create (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, 0.1)
	pText = App.TGParagraph_CreateW (pPlayer.GetName ())
	pPane.AddChild (pText, 0.01, 0, 0)
	pPlayerEntryPane.PrependChild (pPane, 0, 0, 0)

	fHeight = pText.GetHeight ()
	fWidth = pText.GetWidth ()

	# Resize the player entry pane
	pPlayerEntryPane.Resize (Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH, fHeight, 0)

	# Create ship text
	iPlayerID = pPlayer.GetNetID ()
	pShip = pMultGame.GetShipFromPlayerID (iPlayerID)
	pcText = ""
	if (pShip):
		# Get the type from the ship.
		iType = pShip.GetNetType ()
		if (pShip.IsDying () or pShip.IsDead ()):
			pString = pDatabase.GetString ("Dead")
		else:
			if (iType == 0):
				# Don't know what ship.  Display unknown
#				print ("Got ship but don't know what type")
				pString = pDatabase.GetString ("Unknown")
			else:
				pString = Multiplayer.MissionShared.g_pShipDatabase.GetString (Multiplayer.SpeciesToShip.GetScriptFromSpecies (iType))
	else:
		# Don't know what ship.  Display unknown
#		print ("Didn't get ship")
		pString = pDatabase.GetString ("Unknown")

	pcString = pString.GetCString ()
	pcText = " - " + pcString

	pText = App.TGParagraph_Create (pcText)

	pPane.AddChild (pText, 0.01 + fWidth, 0, 0)

	# Create the score
	# Get the death total from the score dictionaries
#	pDict = Mission6.g_kScoresDictionary

#	iScore = 0
#	if (pDict.has_key (iPlayerID)):
#		iScore = pDict [iPlayerID]
#
#	pText = App.TGParagraph_Create (str (iScore) + "pts")
#	pPlayerEntryPane.AddChild (pText, Multiplayer.MissionMenusShared.SYSTEM_WINDOW_WIDTH - 0.1, 0, 0)

	return pPlayerEntryPane


###############################################################################
#	BuildMissionSpecificOptionsMenuPane()
#	
#	Builds the scoreboard along with the boot button that you see when you
#	press ESCAPE while playing in deathmatch mode
#	
#	Args:	TGPane*	pEventPane	- the pane that handles our events
#	
#	Return:	None
###############################################################################
def BuildMissionSpecificOptionsMenuPane(pEventPane):
	import MainMenu.mainmenu
	import Multiplayer.MultiplayerMenus
	import Multiplayer.MissionShared
	
	if App.g_kUtopiaModule.IsHost() and App.g_kUtopiaModule.IsClient():
		pSubtitle = Multiplayer.MissionShared.g_pDatabase.GetString("Defend the Starbase Host")
	elif App.g_kUtopiaModule.IsClient():
		pSubtitle = Multiplayer.MissionShared.g_pDatabase.GetString("Defend the Starbase Client")
	else:
		pSubtitle = Multiplayer.MissionShared.g_pDatabase.GetString("Defend the Starbase Direct Host")
	pPane = Multiplayer.MultiplayerMenus.GetMissionPane(pSubtitle)

	# We want our stylized window to take up 3/4 of the available height in
	# the pane, and to be centered
	fScoreWindowWidth = 0.5125
	fScoreWindowHeight = pPane.GetHeight() * 0.75
	fScoreXPos = (pPane.GetWidth() - fScoreWindowWidth) / 2.0 
	fScoreYPos = (pPane.GetHeight() - fScoreWindowHeight) / 2.0

	# Set the font larger
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcSmallFont,
				MainMenu.mainmenu.g_kSmallFontSize[MainMenu.mainmenu.g_iRes])

	# Create Player, Kills, Deaths, and Score text
	pTextPane = App.TGPane_Create(0.175, 0.04)
	pText = App.TGParagraph_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Player"))
	pText.SetColor(App.g_kMultiplayerBorderBlue)
	pTextPane.AddChild(pText, 0.0, 0.0, 0)
	pTextPane.Resize(0.175, pText.GetHeight(), 0)
	pPane.AddChild(pTextPane, 0.10 + fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	pTextPane = App.TGPane_Create(0.065, 0.1)
	pText = App.TGParagraph_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Kills"))
	pText.SetColor(App.g_kMultiplayerBorderBlue)
	pTextPane.AddChild(pText, 0.0, 0.0, 0)
	pTextPane.Resize(0.08, pText.GetHeight(), 0)
	pPane.AddChild(pTextPane, 0.27 + fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)
	
	pTextPane = App.TGPane_Create(0.065, 0.1)
	pText = App.TGParagraph_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Deaths"))
	pText.SetColor(App.g_kMultiplayerBorderBlue)
	pTextPane.AddChild(pText, 0.0, 0.0, 0)
	pTextPane.Resize(0.08, pText.GetHeight(), 0)
	pPane.AddChild(pTextPane, 0.335 + fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	# Build the black header the goes behind the captions.
	# Its purpose is to cover up menu items that scroll up behind it.
	# It handles events so that they won't reach any buttons that it's
	# covering up.
	pHeader = App.TGIcon_Create(App.GraphicsModeInfo_GetCurrentMode().GetLcarsString(), 200)
	pHeader.SetColor(App.NiColorA_BLACK)
	pHeader.Resize(0.502, 0.04, 0)
	pHeader.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".HandleMouseEventsForGlass")
	pPane.AddChild(pHeader,	fScoreXPos + 0.0105, fScoreYPos + 0.03, 0)

	# Create the stylized window in which our player list will go
	pWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", 
		Multiplayer.MissionShared.g_pDatabase.GetString("Score Board"), 0.0,
		0.0, None, 1, fScoreWindowWidth, fScoreWindowHeight)
	pWindow.SetTitleBarThickness(0.03, 0)
	pPane.AddChild(pWindow, fScoreXPos, fScoreYPos, 0)

	# Create a subpane inside of which will go the player list. It will be the nice,
	# unassuming, docile sort of subpane which obediently resizes itself to fit snugly
	# within its parent StylizedWindow
	global g_pOptionsWindowPlayerMenu
	g_pOptionsWindowPlayerMenu = App.STSubPane_Create(0.0, 0.0, 1)
	pWindow.AddChild(g_pOptionsWindowPlayerMenu, 0.0, 0.0, 0)
	pWindow.InteriorChangedSize(1)
	
	# We want the boot button to take up about 1/3 of the space under the
	# stylized window, horizontally, 2/5 of the space under it vertically,
	# and to be centered under it along both axes. It should be disabled if we're
	# not the host
	fBootButtonWidth = fScoreWindowWidth * (1.0/3.0)
	fBootButtonHeight = (pPane.GetHeight() - (fScoreWindowHeight + fScoreYPos)) * 0.4
	fBootButtonXPos = (pPane.GetWidth() - fBootButtonWidth) / 2.0
	fBootButtonYPos = (((pPane.GetHeight() - (fScoreWindowHeight + fScoreYPos)) - fBootButtonHeight) / 2.0) + fScoreWindowHeight + fScoreYPos

	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(ET_BOOT_BUTTON_CLICKED)
	pEvent.SetDestination(pEventPane)

	pBanEvent = App.TGEvent_Create()
	pBanEvent.SetEventType(ET_BAN_BUTTON_CLICKED)
	pBanEvent.SetDestination(pEventPane)

	global g_pOptionsWindowBootButton
	global g_pOptionsWindowBanButton

	g_pOptionsWindowBootButton = App.STButton_CreateW(
		Multiplayer.MissionShared.g_pDatabase.GetString("Boot"),
		pEvent, 0, fBootButtonWidth, fBootButtonHeight)
	g_pOptionsWindowBootButton.SetJustification(App.STButton.CENTER)
	g_pOptionsWindowBootButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pOptionsWindowBootButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pOptionsWindowBootButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pOptionsWindowBootButton.SetColorBasedOnFlags()
	g_pOptionsWindowBootButton.SetDisabled(0)

	g_pOptionsWindowBanButton = App.STButton_CreateW(Multiplayer.MissionShared.g_pDatabase.GetString("Ban"),
		pBanEvent, 0, fBootButtonWidth, fBootButtonHeight)
	g_pOptionsWindowBanButton.SetJustification(App.STButton.CENTER)
	g_pOptionsWindowBanButton.SetNormalColor(App.g_kMainMenuButtonColor)
	g_pOptionsWindowBanButton.SetHighlightedColor(App.g_kMainMenuButtonHighlightedColor)
	g_pOptionsWindowBanButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
	g_pOptionsWindowBanButton.SetColorBasedOnFlags()
	g_pOptionsWindowBanButton.SetDisabled(0)

	pPane.AddChild(g_pOptionsWindowBootButton, fBootButtonXPos, fBootButtonYPos, 0)
	pPane.AddChild(g_pOptionsWindowBanButton, 
				   fBootButtonXPos + g_pOptionsWindowBootButton.GetWidth() + (App.globals.DEFAULT_ST_INDENT_HORIZ * 2.0),
				   fBootButtonYPos, 0)

	pPane.Layout()

	# Go back to the flight font
	App.g_kFontManager.SetDefaultFont(MainMenu.mainmenu.g_pcFlightSmallFont,
				MainMenu.mainmenu.g_kFlightSmallFontSize[MainMenu.mainmenu.g_iRes])

###############################################################################
#	HandleMouseEventsForGlass()
#	
#	There are times that we want to cover up some UI elements with glass.
#	We have to make sure the user can't click on them, so we make the glass
#	handle mouse events before letting them pass underneath
#	
#	Args:	TGObject*	pObject	- the glass
#			TGEvent*	pEvent	- the ET_MOUSE_EVENT
#	
#	Return:	
###############################################################################
def HandleMouseEventsForGlass(pObject, pEvent):
	pEvent.SetHandled()
	pObject.CallNextHandler(pEvent)
