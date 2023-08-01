import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"DamageRadMod" : 0.500,
		#"DamageStrMod" : 1.000,
		"FilenameHigh": "data/Models/Ships/KrenimWarship/KrenimWarship.nif",
		#"FilenameMed": "data/Models/Ships/KrenimWarship/KrenimWarship.nif",
		#"FilenameLow": "data/Models/ships/KrenimWarship/KrenimWarship.nif",
		"Name": "Krenim Orbship",
		"HardpointFile": "KrenimOrbship",
		"Species": Multiplayer.SpeciesToShip.KRENIMORBSHIP
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 1500.0, 15.0, 15.0, 200, 2000, "_glow", None, "_specular")
		#pLODModel.AddLOD(pStats["FilenameMed"],  10, 400.0, 15.0, 15.0, 400, 900, "_glow", None, "_specular")
		#pLODModel.AddLOD(pStats["FilenameLow"],  10, 800.0, 15.0, 30.0, 400, 900, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
