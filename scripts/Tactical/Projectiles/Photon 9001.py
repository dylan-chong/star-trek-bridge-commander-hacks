###############################################################################
#	Filename:	PhasedPlasma.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of antimatter torpedoes.
#	
#	Created:	07/3/01 -	Evan Birkby
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Phased Plasma torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 64.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 64.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NXGlow.tga",
					kCoreColor,
					5 * 0.5,
					5 * 8.0,	 
					"data/Textures/Tactical/NXGlow.tga", 
					kGlowColor,
					5 * 7.0,	
					5 * 0.76,	 
					5 * 0.72,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,						
					5 * 25,		
					5 * 0.12,		
					5 * 0.12)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(10 * 0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON1)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Photon Torpedo 9001")

def GetPowerCost():
	return(20.0)

def GetName():
	return("9001 PHOTONIC")

def GetDamage():
	return 0.5 * 20 * 250.0

def GetGuidanceLifetime():
	return 0.1

def GetMaxAngularAccel():
	return 10.0
