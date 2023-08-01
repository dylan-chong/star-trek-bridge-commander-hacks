import App

# types for initializing objects create from C.
UNKNOWN = 0
SABRE = 1
MIRANDA = 2
NOVA = 3
NORWAY = 4
STEAMRUNNER = 5
CONSTELLATION = 6
CENTAUR = 7
DEFIANT = 8
INTREPID = 9
EXCELSIOR = 10
EXCELSIORREFIT = 11
AMBASSADOR = 12
LUNA = 13
AKIRA = 14
NEBULA = 15
GALAXY = 16
SOVEREIGN = 17
PROMETHEUS = 18
SOVEREIGNREFIT = 19
BIRDOFPREY = 20
KVORT = 21
KTINGA = 22
VORCHA = 23
NEGHVAR = 24
TALON = 25
FALCON = 26
VALDORE = 27
WARBIRD = 28
SCIMITAR = 29
HIDEKI = 30
GALOR = 31
KELDON = 32
OBSIDIANKELDON = 33
CARDHYBRID = 34
BUG = 35
BREEN = 36
VORTA = 37
FOUNDER = 38
RECTANGLE = 39
DIAMOND = 40
SPHERE = 41
CUBE = 42
TACTICALCUBE = 43
ASSIMILATIONCUBE = 44
MARAUDER = 45
KESSOKLIGHT = 46
KESSOKHEAVY = 47
SONACRUISER = 48
SONABATTLESHIP = 49
BIOSHIP = 50
HIROGENHUNTER = 51
HIROGENHOLOSHIP = 52
HIROGENVENATIC = 53
KAZONRAIDER = 54
KAZONPREDATOR = 55
KRENIMPATROL = 56
KRENIMWARSHIP = 57
KRENIMTIMESHIP = 58
MALONFREIGHTER = 59
VIDIIANCRUISER = 60
SHUTTLE = 61
FIGHTER = 62
DANUBE = 63
DANUBEREFIT = 64
DELTAFLYER = 65
ARMOREDINTREPID = 66
NX = 67
CONSTITUTION = 68
CONSTITUTIONREFIT = 69
FREIGHTER = 70
TRANSPORT = 71
ESCAPEPOD = 72
CARDFREIGHTER = 73
SUNBUSTER = 74
WEAPONSPLATFORM = 75
KESSOKMINE = 76
FEDOUTPOST = 77
SPACEFACILITY = 78
FEDCOMPLEX = 79
FEDSTARBASE = 80
DS9 = 81
CARDOUTPOST = 82
CARDSTATION = 83
CARDSTARBASE = 84
COMMARRAY = 85
COMMLIGHT = 86
DRYDOCK = 87
PROBE = 88
DECOY = 89
ASTEROID = 90
ASTEROID1 = 91
ASTEROID2 = 92
ASTEROID3 = 93
AMAGON = 94
BIRANUSTATION = 95
ENTERPRISE = 96
GERONIMO = 97
PEREGRINE = 98
ASTEROIDH1 = 99
ASTEROIDH2 = 100
ASTEROIDH3 = 101
BUGRAMMER = 102
WALL = 103
KRENIMORBSHIP = 104
MAX_SHIPS = 105
MAX_FLYABLE_SHIPS = 85

# Setup tuples
kSpeciesTuple = (
	(None, 0, "Neutral", 0),
	("Sabre", 109, "Federation", 1),
	("Miranda", 110, "Federation", 1),
	("Nova", 111, "Federation", 1),
	("Norway", 112, "Federation", 1),
	("Steamrunner", 113, "Federation", 1),
	("Constellation", 114, "Federation", 1),
	("Centaur", 115, "Federation", 1),
	("Defiant", 116, "Federation", 1),
	("Intrepid", 117, "Federation", 1),
	("Excelsior", 118, "Federation", 1),
	("ExcelsiorR", 119, "Federation", 1),
	("Ambassador", App.SPECIES_AMBASSADOR, "Federation", 1),
	("Luna", 120, "Federation", 1),
	("Akira", App.SPECIES_AKIRA, "Federation", 1),
	("Nebula" , App.SPECIES_NEBULA, "Federation", 1),
	("Galaxy", App.SPECIES_GALAXY, "Federation", 1),
	("Sovereign" , App.SPECIES_SOVEREIGN, "Federation", 1),
	("Prometheus" , 121, "Federation", 1),
	("SovereignR" , 122, "Federation", 1),
	("BirdOfPrey", App.SPECIES_BIRD_OF_PREY, "Klingon", 1),
	("Kvort", 403, "Klingon", 1),
	("KTinga", 404, "Klingon", 1),
	("Vorcha" , App.SPECIES_VORCHA, "Klingon", 1),
	("Neghvar", 405, "Klingon", 1),
	("Talon" , 302, "Romulan", 1),
	("Falcon" , 303, "Romulan", 1),
	("Valdore" , 304, "Romulan", 1),
	("Warbird" , App.SPECIES_WARBIRD, "Romulan", 1),
	("Scimitar" , 305, "Romulan", 1),
	("Hideki" , 205, "Cardassian", 1),
	("Galor" , App.SPECIES_GALOR, "Cardassian", 1),
	("Keldon" , App.SPECIES_KELDON, "Cardassian", 1),
	("ObsidianKeldon" , 206, "Cardassian", 1),
	("CardHybrid", App.SPECIES_CARDHYBRID, "Cardassian", 1),
	("Bug" , 801, "Dominion", 1),
	("Breen" , 802, "Dominion", 1),
	("Vorta" , 803, "Dominion", 1),
	("Founder" , 804, "Dominion", 1),
	("Rectangle" , 901, "Borg", 1),
	("Diamond" , 902, "Borg", 1),
	("Sphere" , 903, "Borg", 1),
	("Cube" , 904, "Borg", 1),
	("CubeT" , 905, "Borg", 1),
	("CubeA" , 906, "Borg", 1),
	("Marauder" , App.SPECIES_MARAUDER, "Ferengi", 1),
	("KessokLight" , App.SPECIES_KESSOK_LIGHT, "Kessok", 1),
	("KessokHeavy" , App.SPECIES_KESSOK_HEAVY, "Kessok", 1),  
	("SonaCruiser" , 805, "Sona", 1),
	("SonaBattleship" , 806, "Sona", 1),
	("Bioship" , 750, "Delta Quadrant", 1),
	("HirogenHunter" , 751, "Delta Quadrant", 1),
	("HirogenHoloship" , 752, "Delta Quadrant", 1),
	("HirogenVenatic" , 753, "Delta Quadrant", 1),
	("KazonRaider" , 754, "Delta Quadrant", 1),
	("KazonPredator" , 755, "Delta Quadrant", 1),
	("KrenimPatrol" , 756, "Delta Quadrant", 1),
	("KrenimWarship" , 757, "Delta Quadrant", 1),
	("KrenimTimeship" , 758, "Delta Quadrant", 1),
	("MalonFreighter" , 759, "Delta Quadrant", 1),
	("VidiianCruiser" , 760, "Delta Quadrant", 1),
	("Shuttle" , App.SPECIES_SHUTTLE, "Shuttles", 1),
	("Fighter" , 123, "Shuttles", 1),
	("Danube" , 124, "Shuttles", 1),
	("DanubeR" , 125, "Shuttles", 1),
	("DeltaFlyer" , 126, "Shuttles", 1),
	("ArmoredIntrepid" , 127, "Other", 1),
	("NX" , 128, "Other", 1),
	("Constitution" , 129, "Other", 1),
	("ConstitutionR" , 130, "Other", 1),
	("Freighter" , App.SPECIES_FREIGHTER, "Other", 1),
	("Transport" , App.SPECIES_TRANSPORT, "Other", 1),
	("EscapePod" , App.SPECIES_ESCAPEPOD, "Other", 1),
	("CardFreighter" ,  App.SPECIES_CARDFREIGHTER, "Other", 1),
	("Sunbuster" , App.SPECIES_SUNBUSTER, "Other", 1),
	("OrbitalWeaponsPlatform" , 207, "Other", 1),
	("KessokMine" , App.SPECIES_KESSOKMINE, "Other", 1),
	("FedOutpost" , App.SPECIES_FED_OUTPOST, "Bases", 1),
	("SpaceFacility" , App.SPECIES_SPACE_FACILITY, "Bases", 1),
	("FedComplex" , 761, "Bases", 1),
	("FedStarbase" , App.SPECIES_FED_STARBASE, "Bases", 1),
	("DS9" , 762, "Bases", 1),
	("CardOutpost" , App.SPECIES_CARD_OUTPOST, "Bases", 1),
	("CardStation" , App.SPECIES_CARD_STATION, "Bases", 1),
	("CardStarbase" , App.SPECIES_CARD_STARBASE, "Bases", 1),
	("CommArray" , App.SPECIES_COMMARRAY, "Other", 1),
	("CommLight", App.SPECIES_COMMLIGHT, "Other", 1),
	("DryDock" , App.SPECIES_DRYDOCK, "Bases", 1),
	("Probe" , App.SPECIES_PROBE, "Other", 1),
	("Decoy" , App.SPECIES_PROBETYPE2, "Other", 1),
	("Asteroid" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid1" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid2" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid3" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Amagon", App.SPECIES_ASTEROID, "Neutral", 1),
	("BiranuStation", App.SPECIES_SPACE_FACILITY, "Neutral", 1),
	("Enterprise", App.SPECIES_SOVEREIGN, "Neutral", 1),
	("Geronimo", App.SPECIES_AKIRA, "Neutral", 1),
	("Peregrine", App.SPECIES_NEBULA, "Neutral", 1),
	("Asteroidh1" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroidh2" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroidh3" , App.SPECIES_ASTEROID, "Neutral", 1),
	("BugRammer" , 1001, "Dominion", 1),
	("Wall" , 1002, "Neutral", 1),
	("KrenimOrbship" , 1003, "Delta Quadrant", 1),
	(None, 1, "Neutral", 1))

def GetShipFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_SHIPS):
#		print ("Species out of range")
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	pcScript = pSpecTuple [0]

	ShipScript = __import__("ships." + pcScript)
	ShipScript.LoadModel ()
	return ShipScript.GetShipStats ()

def GetScriptFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_SHIPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	return pSpecTuple [0]

	
# This function is called from code to fill in the spec of
# an object that has been serialized over the net.
def InitObject (self, iType):
	kStats = GetShipFromSpecies (iType)
	if (kStats == None):
		# Failed.  Unknown type. Bail.
		return 0

	# Now that we have the stats, initialize the objects.
	# Initialize the ship's model.
	self.SetupModel (kStats['Name'])

	# Load hardpoints.
	pPropertySet = self.GetPropertySet()
	mod = __import__("ships.Hardpoints." + kStats['HardpointFile'])

	App.g_kModelPropertyManager.ClearLocalTemplates ()
	reload (mod)

	mod.LoadPropertySet(pPropertySet)

	self.SetupProperties()

	self.UpdateNodeOnly()
		
	return 1

def CreateShip (iType):
	# Get ship stats
	kStats = GetShipFromSpecies (iType)

	if (kStats == None):
		# Failed.  Unknown type. Bail.
		return None

#	print ("Creating " + kStats['Name'] + "\n")
	pShip = App.ShipClass_Create (kStats['Name'])

	sModule = "ships." + kSpeciesTuple [iType][0]
#	print ("*** Setting script module " + sModule)
	pShip.SetScript(sModule)

	# Load hardpoints.
	pPropertySet = pShip.GetPropertySet()
	mod = __import__("ships.Hardpoints." + kStats['HardpointFile'])

	App.g_kModelPropertyManager.ClearLocalTemplates ()
	reload(mod)

	mod.LoadPropertySet(pPropertySet)

	pShip.SetupProperties()

	pShip.UpdateNodeOnly()
		
	pShip.SetNetType (iType)

	return pShip

def GetNameFromSpecies (iSpecies):
	pSpecTuple = kSpeciesTuple [iSpecies]
	pcName = pSpecTuple [0]

	return pcName

def GetIconNum (iSpecies):
	pSpecTuple = kSpeciesTuple [iSpecies]
	iNum = pSpecTuple [1]

	return iNum

def GetSideFromSpecies (iSpecies):
	pSpecTuple = kSpeciesTuple [iSpecies]
	pcSide = pSpecTuple [2]

	return pcSide

def GetClassFromSpecies (iSpecies):
	pSpecTuple = kSpeciesTuple [iSpecies]
	iClass = pSpecTuple [3]

	return iClass