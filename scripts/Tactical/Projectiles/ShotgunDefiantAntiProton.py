###############################################################################
#	Filename:	FtaBreenTorp.py
#	By:		edtheborg
###############################################################################

import App

CORE_SIZE = 0.8
GLOW_SPEED = 0.25
GLOW_SIZE = 3.0
FLARE_LENGTH = 1.3

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 186.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					CORE_SIZE * 0.8,
					3.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					GLOW_SPEED * 2.0,	
					GLOW_SIZE * 0.5,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					20,		
					FLARE_LENGTH * 0.3,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.SHOTGUNDEFIANTANTIPROTON)

	return(0)

def GetLaunchSound():
	return("Quantum Torpedo 2")

def GetName():
	return 'Antiproton'

def GetLaunchSpeed():
	return(100.0)

def GetPowerCost():
	return(40.0)

def GetDamage():
	return 0.5 * 2200.0

def GetGuidanceLifetime():
	return 0.1

def GetMaxAngularAccel():
	return 10.0
