import App
import loadspacehelper
import MissionLib
import BasicAI
import Mission6Menus
import DynamicMusic
import Multiplayer.MissionShared
import Multiplayer.MissionMenusShared
import Multiplayer.SpeciesToShip
import string
import Foundation
import Tactical.Interface.ShieldPercentages
from Custom.MultiplayerExtra.MultiplayerLib import CreateMessageStream, SendMessageToEveryone

#Start debugger
#debug = App.CPyDebug(__name__).Print
#debug("Loading multiplayer mission: " + __name__)


#global variables
NonSerializedObjects = (
#"debug",
"g_kKillsDictionary",
"g_kDeathsDictionary",
"g_kScoresDictionary",
"g_kDamageDictionary",
"g_kTeamDictionary",
"g_kTeamScoreDictionary",
"g_kTeamKillsDictionary",
"g_pStarbase",
"g_pAttackerGroup",
"g_pDefenderGroup",
)

# Global variables.  

# setup scoring objects
g_bStarbaseDead = 0
g_pStarbase = None
g_kKillsDictionary = {}
g_kDeathsDictionary = {}
g_kScoresDictionary = {}
g_kDamageDictionary = {}
g_kTeamDictionary = {}
g_kTeamScoreDictionary = {}
g_kTeamKillsDictionary = {}
g_pAttackerGroup = None
g_pDefenderGroup = None
g_kWaveIDList = []
g_bStarbaseCutsceneStarted = 0
g_iShipsRemaining = 0
g_iCurrentWave = 0


# define some messages.  Start at 20 for mission specific message types
SCORE_INIT_MESSAGE = App.MAX_MESSAGE_TYPES + 20
TEAM_SCORE_MESSAGE = App.MAX_MESSAGE_TYPES + 21
TEAM_MESSAGE = App.MAX_MESSAGE_TYPES + 22
AI_LIST_MESSAGE = App.MAX_MESSAGE_TYPES + 23

# Invalid team number
INVALID_TEAM = 255

#Wave Events
ET_WAVE_1			= App.Mission_GetNextEventType()
ET_WAVE_2			= App.Mission_GetNextEventType()
ET_WAVE_3			= App.Mission_GetNextEventType()
ET_WAVE_4			= App.Mission_GetNextEventType()
ET_WAVE_5			= App.Mission_GetNextEventType()
ET_WAVE_6			= App.Mission_GetNextEventType()
ET_WAVE_7			= App.Mission_GetNextEventType()
ET_WAVE_8			= App.Mission_GetNextEventType()
ET_WAVE_9			= App.Mission_GetNextEventType()
ET_WAVE_10			= App.Mission_GetNextEventType()
ET_WAVE_11			= App.Mission_GetNextEventType()
ET_WAVE_12			= App.Mission_GetNextEventType()
ET_WAVE_13			= App.Mission_GetNextEventType()
ET_WAVE_14			= App.Mission_GetNextEventType()
ET_WAVE_15			= App.Mission_GetNextEventType()
ET_WAVE_16			= App.Mission_GetNextEventType()
ET_WAVE_17			= App.Mission_GetNextEventType()
ET_WAVE_18			= App.Mission_GetNextEventType()
ET_WAVE_19			= App.Mission_GetNextEventType()
ET_WAVE_20			= App.Mission_GetNextEventType()
ET_BOSS_WAVE		= App.Mission_GetNextEventType()


# Attacking Ship Selection Lists
kSmallShipList = [
	"NX",
	"Constitution",
	"ConstitutionR",
	"Freighter",
	"Transport",
	"CardFreighter"]

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

kPredatorList = [
	"Scimitar",
	"Founder",
	"Cube",
	"CubeT",
	"Bioship",
	"KrenimTimeship"]


###############################################################################
#	PlayerDestroyed()
#	
#	Handles a player ship having been destroyed.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def PlayerDestroyed(pShip):
	global g_kWaveIDList

	pShipID = pShip.GetObjID()
	pNetType = pShip.GetNetType()
	sSpecies = Multiplayer.SpeciesToShip.GetNameFromSpecies(pNetType)
	
	if pShipID in g_kWaveIDList:
		return
	elif sSpecies in kFrigateList:
		Mission6Menus.g_iFragLimit = Mission6Menus.g_iFragLimit - 4
		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
	elif sSpecies in kDestroyerList:
		Mission6Menus.g_iFragLimit = Mission6Menus.g_iFragLimit - 6
		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
	elif sSpecies in kLightCruiserList:
		Mission6Menus.g_iFragLimit = Mission6Menus.g_iFragLimit - 9
		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
	elif sSpecies in kHeavyCruiserList:
		Mission6Menus.g_iFragLimit = Mission6Menus.g_iFragLimit - 13
		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
	elif sSpecies in kBattleCruiserList:
		Mission6Menus.g_iFragLimit = Mission6Menus.g_iFragLimit - 18
		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
	elif sSpecies in kDreadnoughtList:
		Mission6Menus.g_iFragLimit = Mission6Menus.g_iFragLimit - 24
		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
	elif sSpecies in kBattleshipList:
		Mission6Menus.g_iFragLimit = Mission6Menus.g_iFragLimit - 31
		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
	else:
		print "Invalid Ship Destroyed"
		
	bOver = 0
	if (Mission6Menus.g_iFragLimit < 4):
		# Yes, game is over.
		bOver = 1				

	if (bOver):
		Multiplayer.MissionShared.EndGame(Multiplayer.MissionShared.END_NUM_FRAGS_REACHED)



###############################################################################
#	AttackerDestroyed()
#	
#	Handles an attacking ship having been destroyed.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def AttackerDestroyed(pShip):
	global g_iShipsRemaining
	global g_iCurrentWave
	global g_kWaveIDList
	
	pShipID = pShip.GetObjID()
	if pShipID in g_kWaveIDList:
		g_iShipsRemaining = g_iShipsRemaining - 1
	
	if g_iShipsRemaining == 0:
		MissionLib.TextBanner(None, App.TGString("Wave Clear"), 0, 0.25, 3.0, 20, 1)
		
		fDelayStart = App.g_kUtopiaModule.GetGameTime()
		if g_iCurrentWave == 1:
			MissionLib.CreateTimer(ET_WAVE_2, __name__ + ".CreateWaveTwo", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 2:
			MissionLib.CreateTimer(ET_WAVE_3, __name__ + ".CreateWaveThree", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 3:
			MissionLib.CreateTimer(ET_WAVE_4, __name__ + ".CreateWaveFour", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 4:
			MissionLib.CreateTimer(ET_WAVE_5, __name__ + ".CreateWaveFive", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 5:
			MissionLib.CreateTimer(ET_WAVE_6, __name__ + ".CreateWaveSix", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 6:
			MissionLib.CreateTimer(ET_WAVE_7, __name__ + ".CreateWaveSeven", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 7:
			MissionLib.CreateTimer(ET_WAVE_8, __name__ + ".CreateWaveEight", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 8:
			MissionLib.CreateTimer(ET_WAVE_9, __name__ + ".CreateWaveNine", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 9:
			MissionLib.CreateTimer(ET_WAVE_10, __name__ + ".CreateWaveTen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 10:
			MissionLib.CreateTimer(ET_WAVE_11, __name__ + ".CreateWaveEleven", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 11:
			MissionLib.CreateTimer(ET_WAVE_12, __name__ + ".CreateWaveTwelve", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 12:
			MissionLib.CreateTimer(ET_WAVE_13, __name__ + ".CreateWaveThirteen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 13:
			MissionLib.CreateTimer(ET_WAVE_14, __name__ + ".CreateWaveFourteen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 14:
			MissionLib.CreateTimer(ET_WAVE_15, __name__ + ".CreateWaveFifteen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 15:
			MissionLib.CreateTimer(ET_WAVE_16, __name__ + ".CreateWaveSixteen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 16:
			MissionLib.CreateTimer(ET_WAVE_17, __name__ + ".CreateWaveSeventeen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 17:
			MissionLib.CreateTimer(ET_WAVE_18, __name__ + ".CreateWaveEighteen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 18:
			MissionLib.CreateTimer(ET_WAVE_19, __name__ + ".CreateWaveNineteen", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 19:
			MissionLib.CreateTimer(ET_WAVE_20, __name__ + ".CreateWaveTwenty", fDelayStart + 10, 0, 0)
		elif g_iCurrentWave == 20:
			MissionLib.CreateTimer(ET_BOSS_WAVE, __name__ + ".CreateBossWave", fDelayStart + 10, 0, 0)
		

###############################################################################
#	SendShipLists()
#	
#	Sends ship list data from each spawn wave to the client.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################

def SendShipLists():
	global g_iShipsRemaining
	global g_iCurrentWave
	global g_kWaveIDList

	pMessage = App.TGMessage_Create ()
	pMessage.SetGuaranteed (1)
	
	kStream = App.TGBufferStream ()
	kStream.OpenBuffer (1024)
	
	kStream.WriteChar (chr (AI_LIST_MESSAGE))

	kStream.WriteInt (g_iShipsRemaining)
	kStream.WriteInt (g_iCurrentWave)
	kStream.WriteInt (len(g_kWaveIDList))
	for i in g_kWaveIDList:
		kStream.WriteLong(i)
				
	pMessage.SetDataFromStream (kStream)

	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if (not App.IsNull (pNetwork)):
		pNetwork.SendTGMessageToGroup ("NoMe", pMessage)

	kStream.CloseBuffer ()


###############################################################################
#	CreateWaveOne()
#	
#	Create wave one.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveOne(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_pDefenderGroup
	global g_kWaveIDList

	g_iCurrentWave = 1
	MissionLib.TextBanner(None, App.TGString("Wave 1"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet
		
		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 1", "")
		g_pAttackerGroup.AddName(pShip1.GetName())
		
		pShip2Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 2", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		kWaveList = [pShip1, pShip2]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID()]
		g_iShipsRemaining = 2

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveTwo()
#	
#	Create wave two.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveTwo(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 2
	MissionLib.TextBanner(None, App.TGString("Wave 2"), 0, 0.25, 3.0, 20, 1)

	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 3", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 4", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 5", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		kWaveList = [pShip1, pShip2, pShip3]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID()]
		g_iShipsRemaining = 3

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveThree()
#	
#	Create wave three.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveThree(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 3
	MissionLib.TextBanner(None, App.TGString("Wave 3"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 6", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 7", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 8", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 9", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID()]
		g_iShipsRemaining = 4

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveFour()
#	
#	Create wave four.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveFour(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 4
	MissionLib.TextBanner(None, App.TGString("Wave 4"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 10", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 11", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 12", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 13", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID()]
		g_iShipsRemaining = 4

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveFive()
#	
#	Create wave five.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveFive(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 5
	MissionLib.TextBanner(None, App.TGString("Wave 5"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 14", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 15", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 16", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 17", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID()]
		g_iShipsRemaining = 4

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveSix()
#	
#	Create wave six.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveSix(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 6
	MissionLib.TextBanner(None, App.TGString("Wave 6"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 18", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 19", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 20", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 21", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 22", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveSeven()
#	
#	Create wave seven.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveSeven(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 7
	MissionLib.TextBanner(None, App.TGString("Wave 7"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 23", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 24", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 25", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 26", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 27", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveEight()
#	
#	Create wave eight.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveEight(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 8
	MissionLib.TextBanner(None, App.TGString("Wave 8"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 28", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 29", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 30", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 31", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 32", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveNine()
#	
#	Create wave nine.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveNine(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 9
	MissionLib.TextBanner(None, App.TGString("Wave 9"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 33", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 34", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 35", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 36", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 37", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveTen()
#	
#	Create wave ten.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveTen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 10
	MissionLib.TextBanner(None, App.TGString("Wave 10"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 38", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 39", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 40", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 41", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 42", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveEleven()
#	
#	Create wave eleven.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveEleven(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 11
	MissionLib.TextBanner(None, App.TGString("Wave 11"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 43", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 44", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 45", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 46", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 47", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveTwelve()
#	
#	Create wave twelve.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveTwelve(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 12
	MissionLib.TextBanner(None, App.TGString("Wave 12"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 48", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 49", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 50", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 51", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 52", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveThirteen()
#	
#	Create wave thirteen.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveThirteen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 13
	MissionLib.TextBanner(None, App.TGString("Wave 13"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 53", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 54", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 55", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 56", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 57", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveFourteen()
#	
#	Create wave fourteen.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveFourteen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 14
	MissionLib.TextBanner(None, App.TGString("Wave 14"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 58", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 59", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 60", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 61", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 62", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveFifteen()
#	
#	Create wave fifteen.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveFifteen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 15
	MissionLib.TextBanner(None, App.TGString("Wave 15"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 63", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 64", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 65", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 66", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 67", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID()]
		g_iShipsRemaining = 5

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveSixteen()
#	
#	Create wave sixteen.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveSixteen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 16
	MissionLib.TextBanner(None, App.TGString("Wave 16"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 68", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 69", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 70", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 71", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 72", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		pShip6Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip6 = loadspacehelper.CreateShip(str(pShip6Choice), pSet, "Attacker 73", "")
		g_pAttackerGroup.AddName(pShip6.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5, pShip6]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID(), pShip6.GetObjID()]
		g_iShipsRemaining = 6

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveSeventeen()
#	
#	Create wave seventeen.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveSeventeen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 17
	MissionLib.TextBanner(None, App.TGString("Wave 17"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kSmallShipList[App.g_kSystemWrapper.GetRandomNumber(len(kSmallShipList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 74", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 75", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 76", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 77", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 78", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		pShip6Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip6 = loadspacehelper.CreateShip(str(pShip6Choice), pSet, "Attacker 79", "")
		g_pAttackerGroup.AddName(pShip6.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5, pShip6]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID(), pShip6.GetObjID()]
		g_iShipsRemaining = 6

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveEighteen()
#	
#	Create wave eighteen.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveEighteen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 18
	MissionLib.TextBanner(None, App.TGString("Wave 18"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 80", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 81", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 82", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 83", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 84", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		pShip6Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip6 = loadspacehelper.CreateShip(str(pShip6Choice), pSet, "Attacker 85", "")
		g_pAttackerGroup.AddName(pShip6.GetName())

		pShip7Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip7 = loadspacehelper.CreateShip(str(pShip7Choice), pSet, "Attacker 86", "")
		g_pAttackerGroup.AddName(pShip7.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5, pShip6, pShip7]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID(), pShip6.GetObjID(), pShip7.GetObjID()]
		g_iShipsRemaining = 7

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveNineteen()
#	
#	Create wave nineteen.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveNineteen(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 19
	MissionLib.TextBanner(None, App.TGString("Wave 19"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 87", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 88", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 89", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 90", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 91", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		pShip6Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip6 = loadspacehelper.CreateShip(str(pShip6Choice), pSet, "Attacker 92", "")
		g_pAttackerGroup.AddName(pShip6.GetName())

		pShip7Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip7 = loadspacehelper.CreateShip(str(pShip7Choice), pSet, "Attacker 93", "")
		g_pAttackerGroup.AddName(pShip7.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5, pShip6, pShip7]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID(), pShip6.GetObjID(), pShip7.GetObjID()]
		g_iShipsRemaining = 7

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateWaveTwenty()
#	
#	Create wave twenty.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateWaveTwenty(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 20
	MissionLib.TextBanner(None, App.TGString("Wave 20"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kFrigateList[App.g_kSystemWrapper.GetRandomNumber(len(kFrigateList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Attacker 94", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		pShip2Choice = kDestroyerList[App.g_kSystemWrapper.GetRandomNumber(len(kDestroyerList))]
		pShip2 = loadspacehelper.CreateShip(str(pShip2Choice), pSet, "Attacker 95", "")
		g_pAttackerGroup.AddName(pShip2.GetName())

		pShip3Choice = kLightCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kLightCruiserList))]
		pShip3 = loadspacehelper.CreateShip(str(pShip3Choice), pSet, "Attacker 96", "")
		g_pAttackerGroup.AddName(pShip3.GetName())

		pShip4Choice = kHeavyCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kHeavyCruiserList))]
		pShip4 = loadspacehelper.CreateShip(str(pShip4Choice), pSet, "Attacker 97", "")
		g_pAttackerGroup.AddName(pShip4.GetName())

		pShip5Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip5 = loadspacehelper.CreateShip(str(pShip5Choice), pSet, "Attacker 98", "")
		g_pAttackerGroup.AddName(pShip5.GetName())

		pShip6Choice = kBattleCruiserList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleCruiserList))]
		pShip6 = loadspacehelper.CreateShip(str(pShip6Choice), pSet, "Attacker 99", "")
		g_pAttackerGroup.AddName(pShip6.GetName())

		pShip7Choice = kDreadnoughtList[App.g_kSystemWrapper.GetRandomNumber(len(kDreadnoughtList))]
		pShip7 = loadspacehelper.CreateShip(str(pShip7Choice), pSet, "Attacker 100", "")
		g_pAttackerGroup.AddName(pShip7.GetName())

		pShip8Choice = kBattleshipList[App.g_kSystemWrapper.GetRandomNumber(len(kBattleshipList))]
		pShip8 = loadspacehelper.CreateShip(str(pShip8Choice), pSet, "Attacker 101", "")
		g_pAttackerGroup.AddName(pShip8.GetName())

		kWaveList = [pShip1, pShip2, pShip3, pShip4, pShip5, pShip6, pShip7, pShip8]
		g_kWaveIDList = [pShip1.GetObjID(), pShip2.GetObjID(), pShip3.GetObjID(), pShip4.GetObjID(), pShip5.GetObjID(), pShip6.GetObjID(), pShip7.GetObjID(), pShip8.GetObjID()]
		g_iShipsRemaining = 8

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	CreateBossWave()
#	
#	Create wave twenty.
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def CreateBossWave(TGObject, pEvent):

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_pAttackerGroup
	global g_kWaveIDList
	
	g_iCurrentWave = 21
	MissionLib.TextBanner(None, App.TGString("BOSS ROUND"), 0, 0.25, 3.0, 20, 1)
	
	if (App.g_kUtopiaModule.IsHost ()):	
		pSet = Multiplayer.MissionShared.g_pStartingSet

		pShip1Choice = kPredatorList[App.g_kSystemWrapper.GetRandomNumber(len(kPredatorList))]
		pShip1 = loadspacehelper.CreateShip(str(pShip1Choice), pSet, "Boss Ship", "")
		g_pAttackerGroup.AddName(pShip1.GetName())

		kWaveList = [pShip1]
		g_kWaveIDList = [pShip1.GetObjID()]
		g_iShipsRemaining = 1

		SendShipLists()

		for i in kWaveList:
			kLocation = App.TGPoint3()
			kLocation.SetXYZ(0.0, 0.0, 0.0)
			x = App.g_kSystemWrapper.GetRandomNumber (250)
			x = x + 1500;
			y = App.g_kSystemWrapper.GetRandomNumber (250)
			y = y + 1;
			z = App.g_kSystemWrapper.GetRandomNumber (250)
			z = z + 1;
			kLocation.SetXYZ (x, y, z)
			i.SetTranslate(kLocation)
			i.SetAI(BasicAI.CreateTeamAI(i, g_pDefenderGroup))


###############################################################################
#	GetWinString()
#	
#	Returns a string that describes who won
#	
#	Args:	None
#	
#	Return:	char*
###############################################################################
def GetWinString():
	import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase
	
	# Play the appropriate win/lose fanfare
	import Mission6Menus
	import DynamicMusic
	if g_bStarbaseDead:
		if Mission6Menus.g_iTeam == 0:
			DynamicMusic.PlayFanfare("Win")
		else:
			DynamicMusic.PlayFanfare("Lose")
	else:
		if Mission6Menus.g_iTeam == 0:
			DynamicMusic.PlayFanfare("Lose")
		else:
			DynamicMusic.PlayFanfare("Win")

	if g_bStarbaseDead:
		return pDatabase.GetString("AttackersWin").GetCString()
	else:
		return pDatabase.GetString("DefendersWin").GetCString()

#Kill the Mission database
def Terminate(pMission):
	import Multiplayer.MissionShared
	import Mission6Menus
#	debug("Terminating multiplayer mission 3.")

	# Remove the starbase from the attacker group.  Do this before MissionShared.Terminate
	# because the database will be deleted afterthat.
	global g_pAttackerGroup
	pDatabase = Multiplayer.MissionShared.g_pDatabase
	g_pAttackerGroup.RemoveName(pDatabase.GetString("Starbase").GetCString())
	g_pAttackerGroup = None

	# Terminate common stuff, which will handle delete of mission
	# menus as well.
	Multiplayer.MissionShared.Terminate (pMission)

	# Clear dictionaries
	global g_kKillsDictionary 
	global g_kDeathsDictionary 
	global g_kScoresDictionary 
	global g_kDamageDictionary 
	global g_kTeamDictionary 
	global g_kTeamScoreDictionary 
	global g_kTeamKillsDictionary 

	for iKey in g_kKillsDictionary.keys ():
		del g_kKillsDictionary [iKey]		

	for iKey in g_kDeathsDictionary.keys ():
		del g_kDeathsDictionary [iKey]		

	for iKey in g_kScoresDictionary.keys ():
		del g_kScoresDictionary [iKey]		

	for iKey in g_kDamageDictionary.keys ():
		del g_kDamageDictionary [iKey]		

	for iKey in g_kTeamDictionary.keys ():
		del g_kTeamDictionary [iKey]		

	for iKey in g_kTeamKillsDictionary.keys ():
		del g_kTeamKillsDictionary [iKey]		

	for iKey in g_kTeamScoreDictionary.keys ():
		del g_kTeamScoreDictionary [iKey]		

	Mission6Menus.g_fYPixelOffset = 0.0
	Mission6Menus.g_fXPixelOffset = 0.0

	Mission6Menus.g_iTeam = 0
	Mission6Menus.g_iIdOfCurrentlySelectedPlayer = App.TGNetwork.TGNETWORK_INVALID_ID

	# Global pointers to user interface items
	Mission6Menus.g_pTeamButton = None
	Mission6Menus.g_pOptionsWindowBootButton = None
	Mission6Menus.g_pOptionsWindowPlayerMenu = None

#Episode level stuff
def CreateMenus():
	return 0


def RemoveHooks():
	return


###############################################################################
#	PreLoadAssets()
#	
#	This is called once, at the beginning of the mission before Initialize()
#	to allow us to add models to be pre loaded
#	
#	Args:	pMission	- the Mission object
#	
#	Return:	none
###############################################################################
def PreLoadAssets(pMission):
	return
	#loadspacehelper.PreloadShip("NX", 1)
	#loadspacehelper.PreloadShip("Constitution", 1)
	#loadspacehelper.PreloadShip("ConstitutionR", 1)
	#loadspacehelper.PreloadShip("Freighter", 1)
	#loadspacehelper.PreloadShip("Transport", 1)
	#loadspacehelper.PreloadShip("CardFreighter", 1)
	#loadspacehelper.PreloadShip("Sabre", 1)
	#loadspacehelper.PreloadShip("Miranda", 1)
	#loadspacehelper.PreloadShip("Nova", 1)
	#loadspacehelper.PreloadShip("BirdOfPrey", 1)
	#loadspacehelper.PreloadShip("Talon", 1)
	#loadspacehelper.PreloadShip("Hideki", 1)
	#loadspacehelper.PreloadShip("Bug", 1)
	#loadspacehelper.PreloadShip("KazonRaider", 1)
	#loadspacehelper.PreloadShip("KrenimPatrol", 1)
	# loadspacehelper.PreloadShip("Norway", 1)
	# loadspacehelper.PreloadShip("Steamrunner", 1)
	# loadspacehelper.PreloadShip("Constellation", 1)
	# loadspacehelper.PreloadShip("Kvort", 1)
	# loadspacehelper.PreloadShip("Falcon", 1)
	# loadspacehelper.PreloadShip("Rectangle", 1)
	# loadspacehelper.PreloadShip("HirogenHunter", 1)
	# loadspacehelper.PreloadShip("Centaur", 1)
	# loadspacehelper.PreloadShip("Defiant", 1)
	# loadspacehelper.PreloadShip("Intrepid", 1)
	# loadspacehelper.PreloadShip("KTinga", 1)
	# loadspacehelper.PreloadShip("Galor", 1)
	# loadspacehelper.PreloadShip("SonaCruiser", 1)
	# loadspacehelper.PreloadShip("HirogenHoloship", 1)
	# loadspacehelper.PreloadShip("KazonPredator", 1)
	# loadspacehelper.PreloadShip("KrenimWarship", 1)
	# loadspacehelper.PreloadShip("Excelsior", 1)
	# loadspacehelper.PreloadShip("ExcelsiorR", 1)
	# loadspacehelper.PreloadShip("Ambassador", 1)
	# loadspacehelper.PreloadShip("Keldon", 1)
	# loadspacehelper.PreloadShip("Breen", 1)
	# loadspacehelper.PreloadShip("Diamond", 1)
	# loadspacehelper.PreloadShip("Marauder", 1)
	# loadspacehelper.PreloadShip("KessokLight", 1)
	# loadspacehelper.PreloadShip("VidiianCruiser", 1)
	# loadspacehelper.PreloadShip("Luna", 1)
	# loadspacehelper.PreloadShip("Akira", 1)
	# loadspacehelper.PreloadShip("Nebula", 1)
	# loadspacehelper.PreloadShip("Vorcha", 1)
	# loadspacehelper.PreloadShip("ObsidianKeldon", 1)
	# loadspacehelper.PreloadShip("SonaBattleship", 1)
	# loadspacehelper.PreloadShip("MalonFreighter", 1)
	# loadspacehelper.PreloadShip("Galaxy", 1)
	# loadspacehelper.PreloadShip("Sovereign", 1)
	# loadspacehelper.PreloadShip("Valdore", 1)
	# loadspacehelper.PreloadShip("Sphere", 1)
	# loadspacehelper.PreloadShip("KessokHeavy", 1)
	# loadspacehelper.PreloadShip("HirogenVenatic", 1)
	# loadspacehelper.PreloadShip("Prometheus", 1)
	# loadspacehelper.PreloadShip("SovereignR", 1)
	# loadspacehelper.PreloadShip("Neghvar", 1)
	# loadspacehelper.PreloadShip("Warbird", 1)
	# loadspacehelper.PreloadShip("CardHybrid", 1)
	# loadspacehelper.PreloadShip("Vorta", 1)


#Mission startup
def Initialize(pMission):
	import Mission6Menus
	import Multiplayer.MissionShared
#	debug("Multiplayer mission start.")
	# Call common initialize routine
	Multiplayer.MissionShared.Initialize (pMission)

	global g_bStarbaseDead
	g_bStarbaseDead = 0

	if (App.g_kUtopiaModule.IsHost ()):	
		Mission6Menus.BuildMission6Menus ()

	#Setup event handlers
	SetupEventHandlers(pMission)

	if (App.g_kUtopiaModule.IsHost () and App.g_kUtopiaModule.IsClient ()):
		pNetwork = App.g_kUtopiaModule.GetNetwork ()
		iPlayerID = pNetwork.GetHostID ()

		if (not g_kKillsDictionary.has_key (iPlayerID)):
			# Add a blank key
			global g_kKillsDictionary
			g_kKillsDictionary [iPlayerID] = 0		# No kills

		if (not g_kDeathsDictionary.has_key (iPlayerID)):
			# Add a blank key
			global g_kDeathsDictionary
			g_kDeathsDictionary [iPlayerID] = 0		# No kills

	# Initialize team scores for two teams
	global g_kTeamScoreDictionary
	g_kTeamScoreDictionary [0] = 0
	g_kTeamScoreDictionary [1] = 0

	# Create the group of attackers for the starbase AI
	global g_pAttackerGroup
	g_pAttackerGroup = App.ObjectGroupWithInfo()
	
	global g_pDefenderGroup
	g_pDefenderGroup = App.ObjectGroupWithInfo()

	global g_kWaveIDList
	g_kWaveIDList = []

	Tactical.Interface.ShieldPercentages.init()

	
	# Now we're done.  The menu will do the work to create the ship.
	

# setup any event handlers specific to this mission.
def SetupEventHandlers (pMission):
	import Multiplayer.MissionShared
	if (App.g_kUtopiaModule.IsHost ()):
		# Only hosts handling scoring.
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectKilledHandler")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__ + ".DamageEventHandler")
	else:
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".StarbaseKilledHandler")

	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_DESTROYED, pMission, __name__ + ".ObjectDestroyedHandler")

	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NEW_PLAYER_IN_GAME, pMission, __name__ + ".NewPlayerHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_DELETE_PLAYER, pMission, __name__ + ".DeletePlayerHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_NAME_CHANGE_EVENT, pMission, __name__ + ".ProcessNameChangeHandler")

	# setup handler for listening for packets.
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, pMission, __name__ + ".ProcessMessageHandler")

	pMission.AddPythonFuncHandlerForInstance(Multiplayer.MissionShared.ET_RESTART_GAME, __name__ + ".RestartGameHandler")

	return 0

def ProcessNameChangeHandler (self, pEvent):
	import Mission6Menus
	import Multiplayer.MissionMenusShared

	if (Multiplayer.MissionMenusShared.g_pInfoPane != None):
		# A player's name has changed.  Rebuild the info pane.
		Mission6Menus.RebuildInfoPane ()
	return

def ProcessMessageHandler (self, pEvent):
	import Mission6Menus
	import Multiplayer.SpeciesToSystem
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared

	pMission = MissionLib.GetMission ()
	if (pMission == None):
		# Mission is over, don't process messages.
		return

	pMessage = pEvent.GetMessage()
	if not App.IsNull(pMessage):
		# Get the data from the message
		# Open a buffer stream to read the data
		kStream = pMessage.GetBufferStream ();

		cType = kStream.ReadChar ();

		cType = ord (cType)

		if (cType == Multiplayer.MissionShared.MISSION_INIT_MESSAGE):
#			debug("Process mission init message")

			# Read the max number of players
			Multiplayer.MissionMenusShared.g_iPlayerLimit = ord(kStream.ReadChar())

			# Read the system species
			Multiplayer.MissionMenusShared.g_iSystem = ord (kStream.ReadChar ())
			iNum = ord (kStream.ReadChar())
			if (iNum == 255):
				Multiplayer.MissionMenusShared.g_iTimeLimit = -1
			else:
				Multiplayer.MissionMenusShared.g_iTimeLimit = iNum
				iEndTime = kStream.ReadInt()
				Multiplayer.MissionShared.CreateTimeLeftTimer(iEndTime - int(App.g_kUtopiaModule.GetGameTime()))

			iNum = ord (kStream.ReadChar ())
			if (iNum == 255):
				Mission6Menus.g_iFragLimit = -1
			else:
				Mission6Menus.g_iFragLimit = iNum
				
			# Read the Wave Spawn Data
			#g_iShipsRemaining = ord(kStream.ReadChar())
			#g_iCurrentWave = ord(kStream.ReadChar())
			

			# Create the system
#			debug("Creating system")
			Multiplayer.MissionShared.g_pStartingSet = Multiplayer.SpeciesToSystem.CreateSystemFromSpecies (Multiplayer.MissionMenusShared.g_iSystem)

			Mission6Menus.BuildMission6Menus ()

			# Update info
			Mission6Menus.ResetLimitInfo ()
			Mission6Menus.RebuildInfoPane ()
		elif (cType == Multiplayer.MissionShared.SCORE_CHANGE_MESSAGE):
#			debug("Process score change message")

			global g_kScoresDictionary

			# Read the player id of killer
			iFiringPlayerID = kStream.ReadLong ()

			iKills = 0
			if (iFiringPlayerID != 0):
				# Read the kills
				iKills = kStream.ReadLong ()

				# Read the firing player's score
				g_kScoresDictionary [iFiringPlayerID] = kStream.ReadLong ()

			# Read the player id of killed
			iKilledPlayerID = kStream.ReadLong ()

			# Read the deaths
			iDeaths = kStream.ReadLong ()

			# Read the number of players
			iScoreCount = ord (kStream.ReadChar ())
#			debug("Received " + str (iScoreCount) + "scores")

			while (iScoreCount > 0):
				iPlayerID = kStream.ReadLong ()
				if (iPlayerID != 0):
					iPlayerScore = kStream.ReadLong ()

					g_kScoresDictionary [iPlayerID] = iPlayerScore
				iScoreCount = iScoreCount - 1

			UpdateScore (iFiringPlayerID, iKills, iKilledPlayerID, iDeaths)

		elif (cType == Multiplayer.MissionShared.SCORE_MESSAGE):
#			debug("Process score message")

			global g_kKillsDictionary
			global g_kDeathsDictionary
			global g_kScoresDictionary


			# Read the key id.
			iKey = kStream.ReadLong ()

			# Read Kills
			iKills = kStream.ReadLong ()

			# Read deaths
			iDeaths = kStream.ReadLong ()
			
			# Read score
			iScore = kStream.ReadLong ()
			
			g_kKillsDictionary [iKey] = iKills
			g_kDeathsDictionary [iKey] = iDeaths
			g_kScoresDictionary [iKey] = iScore

			Mission6Menus.RebuildPlayerList ()

		elif (cType == Multiplayer.MissionShared.RESTART_GAME_MESSAGE):
#			debug("Process restart game message")

			RestartGame ()		

		elif (cType == SCORE_INIT_MESSAGE):
#			debug("Process score init message")

			global g_kKillsDictionary
			global g_kDeathsDictionary
			global g_kScoresDictionary
			global g_kTeamDictionary

			# Read the key id.
			iKey = kStream.ReadLong ()

			# Read Kills
			iKills = kStream.ReadLong ()

			# Read deaths
			iDeaths = kStream.ReadLong ()
			
			# Read score
			iScore = kStream.ReadLong ()
			
			# Read score
			iTeam = kStream.ReadChar ()
			iTeam = ord (iTeam)
			
			g_kKillsDictionary [iKey] = iKills
			g_kDeathsDictionary [iKey] = iDeaths
			g_kScoresDictionary [iKey] = iScore
			g_kTeamDictionary [iKey] = iTeam

			Mission6Menus.RebuildPlayerList ()

		elif (cType == TEAM_SCORE_MESSAGE):
#			debug("Process team score message")

			global g_kTeamKillsDictionary
			global g_kTeamScoreDictionary

			# Read the team
			iKey = kStream.ReadChar ()
			iKey = ord (iKey)

			# Read Kills
			iKills = kStream.ReadLong ()

			# Read score
			iScore = kStream.ReadLong ()

			g_kTeamKillsDictionary [iKey] = iKills
			g_kTeamScoreDictionary [iKey] = iScore

			Mission6Menus.RebuildPlayerList ()

		elif (cType == TEAM_MESSAGE):
#			debug("Process team message")

			global g_kTeamDictionary

			iKey = kStream.ReadLong ()
			iTeam = kStream.ReadChar ()
			iTeam = ord (iTeam)

			g_kTeamDictionary [iKey] = iTeam

			if (App.g_kUtopiaModule.IsHost ()):
				# If I'm the host, I have to forward this information to
				# everybody else so they'll know what team this player is on
				pNetwork = App.g_kUtopiaModule.GetNetwork ()
				if (pNetwork):
					pCopyMessage = pMessage.Copy ()
					pNetwork.SendTGMessageToGroup ("NoMe", pCopyMessage)

			Mission6Menus.RebuildPlayerList ()

		elif (cType == AI_LIST_MESSAGE):
			#Wave lists sent to the client.
			global g_iShipsRemaining
			global g_iCurrentWave
			global g_kWaveIDList
						
			g_iShipsRemaining = kStream.ReadInt()
			g_iCurrentWave = kStream.ReadInt()
			g_kWaveIDList = []
			for i in range(kStream.ReadInt()):
				nextship = kStream.ReadLong()
				g_kWaveIDList.append(nextship)

		kStream.Close ()

# This method is called if you are the host and a new player joins.  Use this
# method to send any relevant information about the game to the player joining.
# For example, the name of the system that the mission takes place in would
# be something the hosts decides in his menus and then sends to other players.
def InitNetwork (iToID):
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared

	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if (not pNetwork):
		# Huh?  No network?  bail.
		return

	###############################################################
	# Send mission init message with info needed to start mission
	# allocate the message.
	pMessage = App.TGMessage_Create ()
	pMessage.SetGuaranteed (1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream ()		# Allocate a local buffer stream.
	kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar (chr (Multiplayer.MissionShared.MISSION_INIT_MESSAGE))

	# Write the maximum number of players
	kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iPlayerLimit))

	# Write the system species
	kStream.WriteChar (chr (Multiplayer.MissionMenusShared.g_iSystem))

	if (Multiplayer.MissionMenusShared.g_iTimeLimit == -1):
		kStream.WriteChar (chr (255))
	else:
		kStream.WriteChar(chr(Multiplayer.MissionMenusShared.g_iTimeLimit))
		kStream.WriteInt(Multiplayer.MissionShared.g_iTimeLeft + int(App.g_kUtopiaModule.GetGameTime()))

	if (Mission6Menus.g_iFragLimit == -1):
		kStream.WriteChar (chr (255))
	else:
		kStream.WriteChar (chr (Mission6Menus.g_iFragLimit))
		
	# Write the Wave Spawn Data
	#kStream.WriteChar (chr (g_iShipsRemaining))
	#kStream.WriteChar (chr (g_iCurrentWave))
	

	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream (kStream)

	# Send the message.
	pNetwork.SendTGMessage (iToID, pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer ()

	###############################################################
	# Send the scores for each player in the dictionary
	# allocate the message.
	global g_kKillsDictionary
	global g_kDeathsDictionary
	global g_kScoresDictionary
	global g_kTeamDictionary
	global g_kTeamKillsDictionary
	global g_kTeamScoreDictionary
	global g_pAttackerGroup
	global g_pDefenderGroup


	# Construct a new dictionary containing the keys of 
	# people in the game.
	pDict = {}

	for iKey in g_kKillsDictionary.keys ():
		pDict [iKey] = 1

	for iKey in g_kDeathsDictionary.keys ():
		pDict [iKey] = 1

	for iKey in g_kScoresDictionary.keys ():
		pDict [iKey] = 1

	for iKey in g_kTeamDictionary.keys ():
		pDict [iKey] = 1

	# Now go through the keys in the new dictionary
	# and send that person's score around.

	for iKey in pDict.keys ():
		iKills = 0
		iDeaths = 0
		iScore = 0
		iTeam = INVALID_TEAM
		
		if (g_kKillsDictionary.has_key (iKey)):
			iKills = g_kKillsDictionary [iKey]
					
		if (g_kDeathsDictionary.has_key (iKey)):
			iDeaths = g_kDeathsDictionary [iKey]
					
		if (g_kScoresDictionary.has_key (iKey)):
			iScore = g_kScoresDictionary [iKey]

		if (g_kTeamDictionary.has_key (iKey)):
			iTeam = g_kTeamDictionary [iKey]
				 
		pMessage = App.TGMessage_Create ()
		pMessage.SetGuaranteed (1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream ()		# Allocate a local buffer stream.
		kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar (chr (SCORE_INIT_MESSAGE))

		# write kills and deaths
		kStream.WriteLong (iKey)
		kStream.WriteLong (iKills)
		kStream.WriteLong (iDeaths)
		kStream.WriteLong (iScore)
		kStream.WriteChar (chr (iTeam))

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream (kStream)

		# Send the message.
		pNetwork.SendTGMessage (iToID, pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer ()

	# Now send the team scores
	for iTeam in g_kTeamScoreDictionary.keys ():
		iScore = g_kTeamScoreDictionary [iTeam]

		iKills = 0
		if (g_kTeamKillsDictionary.has_key (iTeam)):
			iKills = g_kTeamKillsDictionary [iTeam]

		pMessage = App.TGMessage_Create ()
		pMessage.SetGuaranteed (1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream ()		# Allocate a local buffer stream.
		kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar (chr (TEAM_SCORE_MESSAGE))

		# write kills and score
		kStream.WriteChar (chr (iTeam))
		kStream.WriteLong (iKills)
		kStream.WriteLong (iScore)

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream (kStream)

		# Send the message.
		pNetwork.SendTGMessage (iToID, pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer ()

	#Send Ship List Data

	global g_iShipsRemaining
	global g_iCurrentWave
	global g_kWaveIDList

	pMessage = App.TGMessage_Create ()
	pMessage.SetGuaranteed (1)
	
	kStream = App.TGBufferStream ()
	kStream.OpenBuffer (1024)
	
	kStream.WriteChar (chr (AI_LIST_MESSAGE))

	kStream.WriteInt (g_iShipsRemaining)
	kStream.WriteInt (g_iCurrentWave)
	kStream.WriteInt (len(g_kWaveIDList))
	for i in g_kWaveIDList:
		kStream.WriteLong(i)
				
	pMessage.SetDataFromStream (kStream)

	pNetwork.SendTGMessage (iToID, pMessage)

	kStream.CloseBuffer ()

	print "Send data to new palyer"

	return 1


def DamageEventHandler(pObject, pEvent):
	if (pEvent.IsHullHit() == 1):
		DamageHandler(pObject, pEvent, 1)
	else:
		DamageHandler(pObject, pEvent, 0)


def DamageHandler (TGObject, pEvent, bHullDamage):
	import Multiplayer.Modifier
	import Multiplayer.SpeciesToShip

	# Damage was done.  We need to record this for scoring purposes.
	# Get the player id of the shooter.
	iHitterID = pEvent.GetFiringPlayerID ()
	
	if (iHitterID == 0):
		# No player doing the hitting.  Don't record.
		return

	# Get the object id of the ship that was hit.
	pShip = App.ShipClass_Cast (pEvent.GetDestination ())
	if (not pShip):
		# Don't score non-ship objects
		return 

	iHitID = pShip.GetObjID ()

	iHitClass = 0
	iHitterClass = 0

	# Get the hitter's ship.
	pGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())
	pHitterShip = pGame.GetShipFromPlayerID (iHitterID)
	if (pHitterShip):
		iHitterClass = Multiplayer.SpeciesToShip.GetClassFromSpecies (pHitterShip.GetNetType ())

	iHitClass = Multiplayer.SpeciesToShip.GetClassFromSpecies (pShip.GetNetType ())

	# Get the amount of damage done.
	fDamage = pEvent.GetDamage ()

	# Modifify damage based on ship class
	fDamage = fDamage * Multiplayer.Modifier.GetModifier (iHitterClass, iHitClass)

	# get the team of the person who did the hitting.
	iHitterTeam = INVALID_TEAM
	if (g_kTeamDictionary.has_key (iHitterID)):
		iHitterTeam = g_kTeamDictionary [iHitterID]

	# Get the team of the ship that got hit.
	if (IsSameTeam (iHitterID, pShip.GetNetPlayerID ())):
		# Same team, so penalize their score
		fDamage = -fDamage		

	# Get the dictionary that stores all the people that have hit this object.
	global g_kDamageDictionary
	pDamageByDict = None
	if (g_kDamageDictionary.has_key (iHitID)):
		# This object has been hit before.  Fetch it's damage by dictionary
		pDamageByDict = g_kDamageDictionary [iHitID]
	else:
		# Create a new dictionary since this object has not been hit by a player
		# before
		pDamageByDict = {}
		g_kDamageDictionary [iHitID] = pDamageByDict


	# Update the damage by dictinary.
	fPreviousDamageDone = 0.0
	pDamageList = None
	if (pDamageByDict.has_key (iHitterID)):
		# This player has done damage before.  Fetch previous damage done.
		# Get the list from the damage dict
		pDamageList = pDamageByDict [iHitterID]
		fPreviousDamageDone = pDamageList [bHullDamage]	# zero is shield, 1 is hull
	else:
		# This player has not done damage before.  Create a new damage list
		# to add to the damage dict.
		pDamageList = [0, 0]		# List of two elements
		pDamageByDict [iHitterID] = pDamageList

	# Add in the damage done this time.
	fPreviousDamageDone = fPreviousDamageDone + fDamage

	# Store it in the database
	pDamageList [bHullDamage] = fPreviousDamageDone


# This handler clears away the starbase when it is destroyed
def ObjectDestroyedHandler(pObject, pEvent):
	import Multiplayer.MissionShared
	global g_pAttackerGroup

	pKilledObject = pEvent.GetDestination ()
	if (pKilledObject.IsTypeOf(App.CT_SHIP)):
		pShip = App.ShipClass_Cast(pKilledObject)
		pShipName = pShip.GetName()
		AttackerDestroyed(pShip)
		PlayerDestroyed(pShip)
		
		if g_pStarbase and pShip.GetObjID () == g_pStarbase.GetObjID ():
#			debug("The starbase has been destroyed")
			global g_pStarbase
			g_pStarbase = None
			global g_bStarbaseDead
			g_bStarbaseDead = 1

			if (g_bStarbaseCutsceneStarted):
				pSequence = App.TGSequence_Create ()

				pAction	= App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pShip.GetContainingSet ().GetName ())
				pSequence.AppendAction(pAction)

				pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StopCinematicMode")
				pSequence.AppendAction(pAction)

				pAction = App.TGScriptAction_Create("MissionLib", "EndCutscene")
				pSequence.AppendAction (pAction)

				pSequence.Play ()

				global g_bStarbaseCutsceneStarted
				g_bStarbaseCutsceneStarted = 0
				Multiplayer.MissionShared.EndGame(Multiplayer.MissionShared.END_STARBASE_DEAD)
				
		#elif 
				
def StarbaseKilledHandler (pObject, pEvent):
	import Multiplayer.MissionShared
	if (Multiplayer.MissionShared.g_bGameOver != 0):
		# If the game is over, then don't do anymore score processing
		return

	pKilledObject = pEvent.GetDestination ()
	if (pKilledObject.IsTypeOf (App.CT_SHIP)):
		pShip = App.ShipClass_Cast (pKilledObject)

		iShipID = pShip.GetObjID ()
	
		if g_pStarbase and pShip.GetObjID () == g_pStarbase.GetObjID ():
			DoStarbaseDestroyedCutscene ()
			global g_bStarbaseDead
			g_bStarbaseDead = 1

	return

# This handler updates the score when an object is killed.
def ObjectKilledHandler (pObject, pEvent):
	import Multiplayer.MissionShared
	if (Multiplayer.MissionShared.g_bGameOver != 0):
		# If the game is over, then don't do anymore score processing
		return

	# Get the player ID of the firing object from the event
	iFiringPlayerID = pEvent.GetFiringPlayerID ()

	# Get the player id of the player who got killed.  It could be AI object,
	# in which case the ID is zero.
	iShipID = App.NULL_ID


	pKilledObject = pEvent.GetDestination ()
	if (pKilledObject.IsTypeOf (App.CT_SHIP)):
		pShip = App.ShipClass_Cast (pKilledObject)

		if g_pAttackerGroup.IsNameInGroup(pShip.GetName()):
			# Remove ship from attacker group.
			g_pAttackerGroup.RemoveName(pShip.GetName())

		# Get the player id of the ship from the multiplayer game.
		iKilledPlayerID = pShip.GetNetPlayerID ()
		iShipID = pShip.GetObjID ()
	
		if g_pStarbase and pShip.GetObjID () == g_pStarbase.GetObjID ():
#			debug("The starbase is exploding")
			global g_bStarbaseDead
			g_bStarbaseDead = 1
	else:
		iKilledPlayerID = 0

	# At this point, we have the player id of the person who made the killing shot.
	# Award a frag to him.
	iKills = 0

	if (iFiringPlayerID != 0):
		# Get the previous frag count.
		global g_kKillsDictionary
		if (g_kKillsDictionary.has_key (iFiringPlayerID) == 1):
			# There is already this player is the kill table.  Get his previous kill total.
			iKills = g_kKillsDictionary [iFiringPlayerID]	
		else:
			# First kill.
			iKills = 0

		if (g_kTeamDictionary.has_key (iFiringPlayerID)):
			iTeam = g_kTeamDictionary [iFiringPlayerID]

			if (not IsSameTeam (iFiringPlayerID, iKilledPlayerID)):
				# Yes, enemy ship.  Award kill
				# Increment kills by one to count for this current kill.
				iKills = iKills + 1

				# Award kill to team as well.
				iTeamKills = 0
				if (g_kTeamKillsDictionary.has_key (iTeam)):
					iTeamKills = g_kTeamKillsDictionary [iTeam]

				iTeamKills = iTeamKills + 1

				g_kTeamKillsDictionary [iTeam] = iTeamKills
	else:
		# Self destruct?  Collision?  Still award a team kill to the defenders if appropriate.
		if (g_kTeamDictionary.has_key (iKilledPlayerID)):
			# get the team that the killed player was on.
			iKilledTeam = g_kTeamDictionary [iKilledPlayerID]
			if (iKilledTeam == 1):	# Attacking team died
				# award a kill to the defending team.
				iTeamKills = 0
				if (g_kTeamKillsDictionary.has_key (0)):
					iTeamKills = g_kTeamKillsDictionary [0]
				
				iTeamKills = iTeamKills + 1					
				g_kTeamKillsDictionary [1] = iTeamKills

	# Award a death to the person that just got killed.
	global g_kDeathsDictionary
	if (g_kDeathsDictionary.has_key (iKilledPlayerID) == 1):
		# There is already this player is the death table.  Get his previous death total.
		iDeaths = g_kDeathsDictionary [iKilledPlayerID]	
	else:
		# First death
		iDeaths = 0

	# Increment Deaths by one to count for this current kill.
	iDeaths = iDeaths + 1

	# Okay, now give all the player's who damaged this object credit.
	iScoreUpdateCount = 0		# Keep track of how many players had their score changed.
	iFiringPlayerScore = 0		# Keep track of this to send the event later.
	global g_kDamageDictionary
	global g_kScoresDictionary
	global g_kTeamScoreDictionary
	global g_kTeamKillsDictionary

	pDamageByDict = None

	if (iShipID != App.NULL_ID):
		if (g_kDamageDictionary.has_key (iShipID)):
			# Okay, there are player damage points to award.
			pDamageByDict = g_kDamageDictionary [iShipID]

	if (pDamageByDict):
		# Okay, there are player damage points to award.
		pDamageByDict = g_kDamageDictionary [iShipID]

		# Loop through the player list and award score.
		for iPlayerID in pDamageByDict.keys ():
			# Get shield and hull damage done by this player.
			pDamageList = pDamageByDict [iPlayerID]
			fShieldDamageDone = pDamageList [0]
			fHullDamageDone = pDamageList [1]

			# Compute damage done based on some formula.  For now
			# it is simple addition.
			fDamageDone = fShieldDamageDone + fHullDamageDone
			fDamageDone = fDamageDone / 10.0		# Reduce points by factor of 10 to keep numbers reasonable

			# Get previous score
			fScore = 0.0
			if (g_kScoresDictionary.has_key (iPlayerID)):
				fScore = g_kScoresDictionary [iPlayerID]
			
			fScore = fScore + fDamageDone

			# Count the number of non firing player scores.  This is
			# used to send the scores later.  The firing player has
			# his score sent separately, so it shouldn't to be counted.
			if (iPlayerID == iFiringPlayerID):
				iFiringPlayerScore = int (fScore)
			else:
#				debug("Counting " + str (iPlayerID))
				iScoreUpdateCount = iScoreUpdateCount + 1
											
			g_kScoresDictionary [iPlayerID] = int (fScore)

			# Update team score as well
			# Get this player's team.
			if (g_kTeamDictionary.has_key (iPlayerID)):
				iTeam = g_kTeamDictionary [iPlayerID]

				fTeamScore = 0
				if (g_kTeamScoreDictionary.has_key (iTeam)):
					fTeamScore = g_kTeamScoreDictionary [iTeam]
				
				fTeamScore = fTeamScore + fDamageDone
				g_kTeamScoreDictionary [iTeam] = int (fTeamScore)


	# Update the score
	UpdateScore (iFiringPlayerID, iKills, iKilledPlayerID, iDeaths)

	# Now send a message to everybody else that the score was updated.
	# allocate the message.
	pMessage = App.TGMessage_Create ()
	pMessage.SetGuaranteed (1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream ()		# Allocate a local buffer stream.
	kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar (chr (Multiplayer.MissionShared.SCORE_CHANGE_MESSAGE))

	# Write the player id of killer
	kStream.WriteLong (iFiringPlayerID)

	if (iFiringPlayerID != 0):
		# Write the kills
		kStream.WriteLong (iKills)

		# Write the score as a long
		kStream.WriteLong (iFiringPlayerScore)

	# Write the player id of killed
	kStream.WriteLong (iKilledPlayerID)
	
	# Write the deaths
	kStream.WriteLong (iDeaths)

	# Write out the number of score changes
	kStream.WriteChar (chr (iScoreUpdateCount))

	# Write out scores for all the players that have score changes.
	iCount = 0
	if (pDamageByDict):
		# Loop through the player list and store the score.
		for iPlayerID in pDamageByDict.keys ():
#			debug("Checking " + str (iPlayerID))
			if (iPlayerID != iFiringPlayerID and iPlayerID != 0):	# firing player already has his score stored
#				debug("Writing score for " + str (iPlayerID) + " for " + str (g_kScoresDictionary [iPlayerID]) + " points.")
				kStream.WriteLong (iPlayerID)
				kStream.WriteLong (g_kScoresDictionary [iPlayerID])
				iCount = iCount + 1

	# Error condition.  Just put some filler in.
	while (iCount < iScoreUpdateCount):
		kStream.WriteLong (0)

	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream (kStream)

	# Send the message to everybody but me.  Use the NoMe group, which
	# is set up by the multiplayer game.
	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if (not App.IsNull (pNetwork)):
		pNetwork.SendTGMessageToGroup ("NoMe", pMessage)

	# We're done.  Close the buffer.
	kStream.CloseBuffer ()

	# Clear the damage dictionary for this object since it is now
	# dead an we don't want memory wasted storing who did damage to
	# this thing anymore.
	if (iShipID != App.NULL_ID):
		if (g_kDamageDictionary.has_key (iShipID)):
			del g_kDamageDictionary [iShipID]

	# Now send the team scores
	for iTeam in g_kTeamScoreDictionary.keys ():
		iScore = g_kTeamScoreDictionary [iTeam]

		iKills = 0
		if (g_kTeamKillsDictionary.has_key (iTeam)):
			iKills = g_kTeamKillsDictionary [iTeam]

		pMessage = App.TGMessage_Create ()
		pMessage.SetGuaranteed (1)		# Yes, this is a guaranteed packet
		
		# Setup the stream.
		kStream = App.TGBufferStream ()		# Allocate a local buffer stream.
		kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
		
		# Write relevant data to the stream.
		# First write message type.
		kStream.WriteChar (chr (TEAM_SCORE_MESSAGE))

		# write kills and score
		kStream.WriteChar (chr (iTeam))
		kStream.WriteLong (iKills)
		kStream.WriteLong (iScore)

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream (kStream)

		# Send the message.
		pNetwork.SendTGMessageToGroup ("NoMe", pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer ()

	# Check if the starbase is dead to see if the game is over
	if g_bStarbaseDead:
		# Do cutscene of starbase being destroyed
		DoStarbaseDestroyedCutscene ()

	# Check frag limit to see if game is over
	CheckFragLimit ()

	return

def CheckFragLimit ():
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared

	if (Multiplayer.MissionShared.g_bGameOver):
		# Don't check frag limit if game is over
		return

	iFragLimit = Mission6Menus.g_iFragLimit
	if (iFragLimit == -1):
		# There are no frag limits
		return

	# only check the defending team if it has reached the frag limit.
	bOver = 0
	if (iFragLimit < 4):
		# Yes, game is over.
		bOver = 1				

	if (bOver):
		Multiplayer.MissionShared.EndGame(Multiplayer.MissionShared.END_NUM_FRAGS_REACHED)


def DoStarbaseDestroyedCutscene ():
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared
	# Set this flag so we don't suddenly give a win to the defender
	# while the starbase is in cutscene mode because time runs out.
	Multiplayer.MissionShared.g_bGameOver = 1

	global g_bStarbaseCutsceneStarted
	g_bStarbaseCutsceneStarted = 1

	# Hide multiplayer window's children, just in case chat or scoreboard was up.
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast (pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	pMultWindow.HideAllChildren()

	# also hide time limit.
	Multiplayer.MissionMenusShared.g_pEndTimePane.SetNotVisible (0)

	pSequence = App.TGSequence_Create ()

	pAction = App.TGScriptAction_Create("MissionLib", "StartCutscene")
	pSequence.AppendAction (pAction)

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "StartCinematicMode", 0)
	pSequence.AppendAction(pAction)	# Start cinematic mode first

	pAction	= App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", g_pStarbase.GetContainingSet ().GetName ())
	pSequence.AppendAction(pAction)

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", g_pStarbase.GetContainingSet ().GetName (), g_pStarbase.GetName ())
	pSequence.AppendAction(pAction)

	pSequence.Play ()

	return 0


def UpdateScore (iFiringPlayerID, iKills, iKilledPlayerID, iDeaths):
	import Mission6Menus
	# Set the new value in the dictionary
	global g_kKillsDictionary
	global g_kDeathsDictionary

	if (iFiringPlayerID != 0):
		g_kKillsDictionary [iFiringPlayerID] = iKills

	g_kDeathsDictionary [iKilledPlayerID] = iDeaths

	# Do a little subtitle announcing the kill.
	DoKillSubtitle (iFiringPlayerID, iKilledPlayerID)

	# Update the interface
	Mission6Menus.RebuildPlayerList ()

def DoKillSubtitle (iFiringPlayerID, iKilledPlayerID):
	import Multiplayer.MissionShared
	pDatabase = Multiplayer.MissionShared.g_pDatabase

	pcSubString = None
	pcName = None
	pcKilledName = None
	pcString = None
	pcFiringTeamName = None
	pcKilledTeamName = None

	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if (pNetwork):
		# Create a subtitle action to display the fact that a kill/death occurred.
		pPlayerList = pNetwork.GetPlayerList ()

		# Get killer's name
		if (iFiringPlayerID != 0):
			pPlayer = pPlayerList.GetPlayer (iFiringPlayerID)
			if (pPlayer):
				kName = pPlayer.GetName ()
				pcName = kName.GetCString ()

				# Get the killers team name
				if (g_kTeamDictionary.has_key (iFiringPlayerID)):
					iTeam = g_kTeamDictionary [iFiringPlayerID]
					if (iTeam == 0):
						pcFiringTeamName = pDatabase.GetString("Attackers")
					else:
						pcFiringTeamName = pDatabase.GetString("Defenders")
					pcFiringTeamName = pcFiringTeamName.GetCString ()


		# Get killed name
		if (iKilledPlayerID != 0):
			pPlayer = pPlayerList.GetPlayer (iKilledPlayerID)
			if (pPlayer):
				kName = pPlayer.GetName ()
				pcKilledName = kName.GetCString ()

			# The ship name is more likely to be accurate than the listing from the
			# Network (what if the killed player has disconnected?). We use that
			# instead, if we can.
			pGame = App.MultiplayerGame_Cast(App.Game_GetCurrentGame())
			pShip = pGame.GetShipFromPlayerID(iKilledPlayerID)
			if pShip:
				if pShip.GetName():
					pcKilledName = pShip.GetName()

			# Get the killed team name
			if (g_kTeamDictionary.has_key (iKilledPlayerID)):
				iTeam = g_kTeamDictionary [iKilledPlayerID]
				if (iTeam == 0):
					pcKilledTeamName = pDatabase.GetString("Attackers")
				else:
					pcKilledTeamName = pDatabase.GetString("Defenders")

				pcKilledTeamName = pcKilledTeamName.GetCString ()


		if (pcName != None and pcKilledName != None):	
			# Player killed by player

			# Get the main string from the database.  The main
			# string will have formatting information in it for
			# translation reasons.
			pString = pDatabase.GetString ("Team Killed By")
			pcString = pString.GetCString ()

			# Construct the sentence in manner similar to sprintf.
			# Use the formatting information in pString to 
			# construct the sentence.
			pcSubString = pcString % (pcKilledName, pcKilledTeamName, pcName, pcFiringTeamName)
		elif (iKilledPlayerID != 0 and iFiringPlayerID == 0):
			# AI killed player
			# Get the main string from the database.  The main
			# string will have formatting information in it for
			# translation reasons.
			pString = pDatabase.GetString ("Team Was Killed")
			pcString = pString.GetCString ()

			# Construct the sentence in manner similar to sprintf.
			# Use the formatting information in pString to 
			# construct the sentence.
			pcSubString = pcString % (pcKilledName, pcKilledTeamName)

	if (pcSubString != None):
		# Okay, there's a subtitle to display
		pSequence = App.TGSequence_Create ()
		pSubtitleAction = App.SubtitleAction_CreateC (pcSubString)
		pSubtitleAction.SetDuration (5.0)
		pSequence.AddAction (pSubtitleAction)
		pSequence.Play ()

		
def NewPlayerHandler (TGObject, pEvent):
	import Mission6Menus
	# check if player is host and not dedicated server.  If dedicated server, don't
	# add the host in as a player.
	iPlayerID = pEvent.GetPlayerID ()

	# Check if this player is already in the dictionary.
	global g_kKillsDictionary 
	global g_kDeathsDictionary 

	if (not g_kKillsDictionary.has_key (iPlayerID)):
		# Add a blank key
		g_kKillsDictionary [iPlayerID] = 0		# No kills

	if (not g_kDeathsDictionary.has_key (iPlayerID)):
		# Add a blank key
		g_kDeathsDictionary [iPlayerID] = 0		# No deaths

	# Rebuild the player list since a new player was added
	Mission6Menus.RebuildPlayerList ()

	return

def DeletePlayerHandler (TGObject, pEvent):
	import Mission6Menus
	# We only handle this event if we're still connected.  If we've been disconnected,
	# then we don't handle this event since we want to preserve the score list to display
	# as the end game dialog.

	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	if (pNetwork):
		if (pNetwork.GetConnectStatus () == App.TGNETWORK_CONNECTED or pNetwork.GetConnectStatus () == App.TGNETWORK_CONNECT_IN_PROGRESS):
			# We do not remove the player from the dictionary.  This way, if the
			# player rejoins, his score will be preserved.
			
			# Rebuild the player list since a player was removed.
			Mission6Menus.RebuildPlayerList ()
	return

def ObjectCreatedHandler (TGObject, pEvent):
	import Mission6Menus
	import Multiplayer.SpeciesToShip
	global g_kWaveIDList

	pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()

	# We only care about ships.
	pShip = App.ShipClass_Cast (pEvent.GetDestination ())
	if (pShip):
		#print "New Ship"
		# We only care about ships.
		if (pShip.IsPlayerShip ()):
#			debug("In object created handler is player ship")
			# A player ship just got created, we need to update the info pane
			Mission6Menus.RebuildInfoPane()
			#print "New Player Ship"
			#AddShipNameToGroup(pShip)
			# Figure out if it goes in the attacker group
			iPlayerID = pShip.GetNetPlayerID ()
			iTeam = g_kTeamDictionary[iPlayerID]
			if iTeam == 0:
				global g_pAttackerGroup
				g_pAttackerGroup.AddName(pShip.GetName())
			else:
				global g_pDefenderGroup
				g_pDefenderGroup.AddName(pShip.GetName())
				
			# A new ship has entered the world.  Reset the friendly enemy group assignments
			ResetEnemyFriendlyGroups ()
			
		else:
			if (pShip.GetNetType () == Multiplayer.SpeciesToShip.FEDSTARBASE):
				global g_pStarbase
				g_pStarbase = pShip
				#print "Starbase Spawn"
			else:
				#print "New AI ship"
				pEnemyGroup.AddName (pShip.GetName ())

def RestartGameHandler (pObject, pEvent):
	import Multiplayer.MissionShared
	pNetwork = App.g_kUtopiaModule.GetNetwork ()

	if (not pNetwork):
		return

	# Okay, we're restarting the game.
	
	# Send Message to everybody to restart
	pMessage = App.TGMessage_Create ()
	pMessage.SetGuaranteed (1)		# Yes, this is a guaranteed packet
	
	# Setup the stream.
	kStream = App.TGBufferStream ()		# Allocate a local buffer stream.
	kStream.OpenBuffer (256)				# Open the buffer stream with a 256 byte buffer.
	
	# Write relevant data to the stream.
	# First write message type.
	kStream.WriteChar (chr (Multiplayer.MissionShared.RESTART_GAME_MESSAGE))

	# Okay, now set the data from the buffer stream to the message
	pMessage.SetDataFromStream (kStream)

	# Send the message.
	pNetwork.SendTGMessage (0, pMessage)

def RestartGame ():
	import Mission6Menus
	import Multiplayer.MissionShared
	import Multiplayer.MissionMenusShared

	# Reset scoreboard.
	# Clear dictionaries
	global g_kKillsDictionary 
	global g_kDeathsDictionary 
	global g_kScoresDictionary 
	global g_kDamageDictionary 
	global g_kTeamDictionary 
	global g_kTeamScoreDictionary 
	global g_kTeamKillsDictionary 
	global g_bStarbaseCutsceneStarted

	for iKey in g_kKillsDictionary.keys ():
		g_kKillsDictionary [iKey] = 0	

	for iKey in g_kDeathsDictionary.keys ():
		g_kDeathsDictionary [iKey] = 0

	for iKey in g_kScoresDictionary.keys ():
		g_kScoresDictionary [iKey] = 0

	for iKey in g_kDamageDictionary.keys ():
		g_kDamageDictionary [iKey] = 0

	for iKey in g_kTeamDictionary.keys ():
		g_kTeamDictionary [iKey] = 0

	for iKey in g_kTeamKillsDictionary.keys ():
		g_kTeamKillsDictionary [iKey] = 0

	for iKey in g_kTeamScoreDictionary.keys ():
		g_kTeamScoreDictionary [iKey] = 0

	# Clear game over flag
	Multiplayer.MissionShared.g_bGameOver = 0

	# Clear ships again just in case
	Multiplayer.MissionShared.ClearShips ()

	# Make sure we've killed the starbase, even if it's exploding
	ClearShips(1)

	# Rebuild score board
	Mission6Menus.RebuildPlayerList ()

	global g_bStarbaseDead
	g_bStarbaseDead = 0

	g_bStarbaseCutsceneStarted = 0

	# Reset time limit
	if (Multiplayer.MissionMenusShared.g_iTimeLimit != -1):
		Multiplayer.MissionShared.g_iTimeLeft = Multiplayer.MissionMenusShared.g_iTimeLimit * 60

	# Recreate the starbase
	if (App.g_kUtopiaModule.IsHost ()):
		CreateStarbase()
	
	# Clear the Attacker group.
	global g_pAttackerGroup
	if (g_pAttackerGroup):
		g_pAttackerGroup.RemoveAllNames ()

	# Turn off the chat window and put it back where it belongs
	pTopWindow = App.TopWindow_GetTopWindow()
	pMultWindow = App.MultiplayerWindow_Cast(pTopWindow.FindMainWindow(App.MWT_MULTIPLAYER))
	pChatWindow = pMultWindow.GetChatWindow()
	pChatWindow.SetPosition(0.0, 0.0, 0)
	if pChatWindow.IsVisible():
		pMultWindow.ToggleChatWindow()

	# Treat as if ship got killed, so go to select ship screen.
	Multiplayer.MissionMenusShared.ShowShipSelectScreen ()


def ResetEnemyFriendlyGroups ():
	import Mission6Menus
	# Go through all the ships in the world, assigned them to
	# friendly/enemy based on team assignment
	iOurTeam = Mission6Menus.g_iTeam

	# Go through player list, trying to find all the ships

	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	pGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())

	if (pNetwork and pGame):
		pMission = MissionLib.GetMission ()
		pEnemyGroup = pMission.GetEnemyGroup ()
		pFriendlyGroup = pMission.GetFriendlyGroup ()

		# First clear the groups.  We will be readding everybody
		# so we want to start with an empty group.
		#pEnemyGroup.RemoveAllNames ()
		pFriendlyGroup.RemoveAllNames()

		pPlayerList = pNetwork.GetPlayerList ()
		iNumPlayers = pPlayerList.GetNumPlayers ()

		for i in range(iNumPlayers):
			pPlayer = pPlayerList.GetPlayerAtIndex (i)
			iPlayerID = pPlayer.GetNetID ()
			pShip = pGame.GetShipFromPlayerID (iPlayerID)		

			if (pShip):
				# Good, there is a ship for this player
				# Determine which team the player is on
				if (g_kTeamDictionary.has_key (iPlayerID)):
					iTeam = g_kTeamDictionary [iPlayerID]

					if (iTeam == iOurTeam):
#						debug("adding to friendly group %s" % pShip.GetName ())
						pFriendlyGroup.AddName (pShip.GetName ())
					else:						
#						debug("adding to enemy group %s" % pShip.GetName ())
						pEnemyGroup.AddName (pShip.GetName ())

		# Add the starbase to the proper group, depending on which side the
		# player is on
		import Multiplayer.MissionShared
		pDatabase = Multiplayer.MissionShared.g_pDatabase
		pcName = pDatabase.GetString("Starbase").GetCString()
		if iOurTeam == 0: # We're attackers
			pEnemyGroup.AddName(pcName)
		else: # we're defenders
			pFriendlyGroup.AddName(pcName)

def IsSameTeam (iObj1PlayerID, iObj2PlayerID):
	# Get the team of the obj1
	if (iObj1PlayerID != 0):
		if (iObj2PlayerID != 0):
			# Okay, these are player ships.  Determine if they're
			# on the same team
			iObj1Team = INVALID_TEAM
			iObj2Team = INVALID_TEAM
								
			if (g_kTeamDictionary.has_key (iObj1PlayerID)):
				iObj1Team = g_kTeamDictionary [iObj1PlayerID]

				if (g_kTeamDictionary.has_key (iObj2PlayerID)):
					iObj2Team = g_kTeamDictionary [iObj2PlayerID]

					# Okay got both teams
					if (iObj1Team == iObj2Team):
						return 1
					else:
						return 0
					
###############################################################################
#	CreateStarbase()
#	
#	Creates the starbase
#	
#	Args:	None
#	
#	Return:	None
###############################################################################
def CreateStarbase():
#	debug("In create starbase")


	if not App.g_kUtopiaModule.IsHost():
#		debug("The client isn't supposed to create AI ships")
		return

	if g_pStarbase:
#		debug("But we already HAVE a starbase.")
		return

	import Multiplayer.MissionShared
	import StarbaseAI
	import loadspacehelper

	pSet = Multiplayer.MissionShared.g_pStartingSet
	if (pSet):

		#print "Create Starbase"

		MissionLib.TextBanner(None, App.TGString("Frag Points Remaining: " + str(Mission6Menus.g_iFragLimit)), 0, 0.30, 5.0, 20, 1)
		fDelayStart = App.g_kUtopiaModule.GetGameTime()
		MissionLib.CreateTimer(ET_WAVE_1, __name__ + ".CreateWaveOne", fDelayStart + 15, 0, 0)

		# Now build the starbase
		pDatabase = Multiplayer.MissionShared.g_pDatabase
		pcName = pDatabase.GetString("Starbase").GetCString()
		global g_pStarbase
		g_pStarbase = loadspacehelper.CreateShip("FedStarbase", pSet, pcName, "")
		g_pStarbase.DisableCollisionDamage (1)

		#g_pStarbase.RandomOrientation ()
		g_pStarbase.UpdateNodeOnly ()

		fRadius = g_pStarbase.GetRadius() * 1.1

		# Make sure the starbase's location won't overlap any other objects in the world.
		iCount = 0
		kLocation = App.TGPoint3()
		kLocation.SetXYZ(0.0, 0.0, 0.0)

		while (iCount < 100):
			x = App.g_kSystemWrapper.GetRandomNumber (300)
			x = x - 150;
			y = App.g_kSystemWrapper.GetRandomNumber (300)
			y = y - 150;
			z = App.g_kSystemWrapper.GetRandomNumber (300)
			z = z - 150;

			kLocation.SetXYZ (x, y, z)

			if (pSet.IsLocationEmptyTG (kLocation, fRadius, 1)):
				# Okay, found a good location.  Place it here.
				# Update the starbase with its new positional information...
				g_pStarbase.SetTranslate(kLocation)
				break

			iCount = iCount + 1

		if (iCount >= 100):
			# Couldn't find a good place for it.  We're desperate.  Go
			# ahead and do the offset placement method, which will end
			# up sticking the starbase far far away.

			kLocation.SetXYZ(0.0, 0.0, 0.0)
			kForward = App.TGPoint3()
			kForward.SetXYZ(0.0, 0.0, 0.0)
			kPoint = App.TGPoint3()
			ChooseNewLocation(kLocation, kForward)
			kPoint.Set(kLocation)
			kPoint.Add(kForward)
			while pSet.IsLocationEmptyTG(kPoint, fRadius, 1) == 0:
				ChooseNewLocation(kLocation, kForward)
				kPoint.Set(kLocation)
				kPoint.Add(kForward)

			# Update the starbase with its new positional information...
			g_pStarbase.SetTranslate(kPoint)

		g_pStarbase.UpdateNodeOnly()

		# update the proximity manager with this object's new position.
		pProximityManager = pSet.GetProximityManager()
		if (pProximityManager):
		   pProximityManager.UpdateObject (g_pStarbase)

		# Add the starbase itself to the attacker list -- the AI needs to have
		# *something* on the attacker list so as not to crash, but it won't
		# try to attack itself
		g_pAttackerGroup.AddName(g_pStarbase.GetName())
		g_pDefenderGroup.AddName(g_pStarbase.GetName())
		
		g_pStarbase.SetAI(StarbaseAI.CreateAI(g_pStarbase))

	
#	debug("Done with CreateStarbase")


###############################################################################
#	ChooseNewLocation(vOrigin, vOffset)
#	
#	Chooses a location for the starbase
#	
#	Args:	vOrigin		- the origin -- input parameter
#			vOffset		- the offset -- returns the location for the ship
#	
#	Return:	zero
###############################################################################
def ChooseNewLocation(vOrigin, vOffset):
	# Add some random amount to vOffset
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * 20.0

	vOffset.SetX( vOffset.GetX() + fUnitRandom )


	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * 20.0

	vOffset.SetY( vOffset.GetY() + fUnitRandom )

	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * 20.0

	vOffset.SetZ( vOffset.GetZ() + fUnitRandom )

	return 0

def ClearShips(bForceClear = 0):
	# Call from MissionShared.py to clear any mission specific ships.  Not all mission
	# scripts need this function, just those that have special cleanup to do.
	if (App.g_kUtopiaModule.IsHost ()):
		pGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())
		if (pGame):
			# Delete the starbase
			if g_pStarbase:
				global g_pStarbase
				if not g_pStarbase.IsDying() or bForceClear:
					pGame.DeleteObjectFromGame(g_pStarbase)
					g_pStarbase = None

