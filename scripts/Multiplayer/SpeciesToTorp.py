import App

# types for initializing torps create from C.
UNKNOWN = 0
ANTIMATTERTORP = 1
BREENTORP = 2
DISRUPTOR1 = 3
DISRUPTOR2 = 4
DISRUPTOR3 = 5
DISRUPTOR4 = 6
FUSIONBOLT = 7
GRAVIMETRIC1 = 8
GRAVIMETRIC2 = 9
INVERSIONTORP = 10
IONCANNON = 11
ISOLITICTORP = 12
MISSILE = 13
PHASEDTORP = 14
PHOTON1 = 15
PHOTON2 = 16
PHOTON3 = 17
PHOTON4 = 18
PHOTON4A = 19
PHOTON5 = 20
PHOTON6 = 21
PHOTON6A = 22
PHOTON7 = 23
PLASMA2 = 24
PLASMA3 = 25
PLASMA4 = 26
PLASMA5 = 27
POLARONTORP = 28
POSITRONTORP1 = 29
POSITRONTORP2 = 30
PULSEPHASER = 31
QUANTUM2 = 32
QUANTUM2D = 33
QUANTUM3 = 34
SCIMITARDIS = 35
SONATORP = 36
TRANSPHASICTORP = 37
VERTERONPULSE = 38
HYPOTHERMIC = 39
KRENIMPULSE = 40
SPATIALCHARGE = 41
PHOTON9001 = 42
FULLIMPULSEBLOCKER = 43
SHIELDDRAINORB = 44
HULLDRAINORB = 45
NULL = 46
MAX_TORPS = 47

# Setup tuples
kSpeciesTuple = ((UNKNOWN, None),
	(ANTIMATTERTORP, "AntimatterTorpedo"),
	(BREENTORP, "BreenTorp"),
	(DISRUPTOR1, "Disruptor 1"),
	(DISRUPTOR2, "Disruptor 2"),
	(DISRUPTOR3, "Disruptor 3"),
	(DISRUPTOR4, "Disruptor 4"),
	(FUSIONBOLT, "FusionBolt"),
	(GRAVIMETRIC1, "Gravimetric 1"),
	(GRAVIMETRIC2, "Gravimetric 2"),
	(INVERSIONTORP, "InversionTorpedo"),
	(IONCANNON, "IonCannon"),
	(ISOLITICTORP, "Isolitic"),
	(MISSILE, "Missile"),
	(PHASEDTORP, "PhasedPlasma"),
	(PHOTON1, "Photon 1"),
	(PHOTON2, "Photon 2"),
	(PHOTON3, "Photon 3"),
	(PHOTON4, "Photon 4"),
	(PHOTON4A, "Photon 4a"),
	(PHOTON5, "Photon 5"),
	(PHOTON6, "Photon 6"),
	(PHOTON6A, "Photon 6a"),
	(PHOTON7, "Photon 7"),
	(PLASMA2, "Plasma 2"),
	(PLASMA3, "Plasma 3"),
	(PLASMA4, "Plasma 4"),
	(PLASMA5, "Plasma 5"),
	(POLARONTORP, "PolaronTorpedo"),
	(POSITRONTORP1, "Positron 1"),
	(POSITRONTORP2, "Positron 2"),
	(PULSEPHASER, "PulsePhaser"),
	(QUANTUM2, "Quantum 2"),
	(QUANTUM2D, "Quantum 2d"),
	(QUANTUM3, "Quantum 3"),
	(SCIMITARDIS, "ScimitarPulse"),
	(SONATORP, "SonaTorp"),
	(TRANSPHASICTORP, "TransphasicTorpedo"),
	(VERTERONPULSE, "VerteronPulse"),
	(HYPOTHERMIC, "Hypothermic"),
	(KRENIMPULSE, "KrenimPulse"),
	(SPATIALCHARGE, "SpatialCharge"),
	(PHOTON9001, "Photon 9001"),
	(FULLIMPULSEBLOCKER, "Full Impulse Blocker"),
	(SHIELDDRAINORB, "Shield Drain Orb"),
	(HULLDRAINORB, "Hull Drain Orb"),
	(NULL, "Null"),
	(MAX_TORPS, None))

def CreateTorpedoFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	pcScript = pSpecTuple [1]

	pTorp = App.Torpedo_Create (pcScript)
	return pTorp

def GetScriptFromSpecies (iSpecies):
	if (iSpecies <= 0 or iSpecies >= MAX_TORPS):
		return None

	pSpecTuple = kSpeciesTuple [iSpecies]
	return pSpecTuple [1]
	
def InitObject (self, iType):
	# Get the script
	pcScript = GetScriptFromSpecies (iType)
	if (pcScript == None):
		return 0

	# call create function to initialize the torp.
	mod = __import__("Tactical.Projectiles." + pcScript)
	mod.Create(self)	

	self.UpdateNodeOnly ()

	return 1;
	
