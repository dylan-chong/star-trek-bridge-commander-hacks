###############################################################################
#	Filename:	PhotonTorpedo2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	10/29/01 -	Evan Birkby
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a photon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ds9torp.tga",
					kCoreColor, 
					3 * 0.2,
					3 * 6.0,	 
					"data/Textures/Tactical/ds9torp.tga", 
					kGlowColor,
					3 * 1.0,	
					3 * 0.5,	 
					3 * 0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					3 * 12,		
					3 * 0.4,		
					3 * 0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON6)

	return(0)

# def GetLaunchSpeed():
# 	return(2 * 100.0)

def GetLaunchSound():
	return("Photon Torpedo 6")

def GetPowerCost():
	return(20.0)

def GetName():
	return("6 PHOTON")

# def GetDamage():
# 	return 2 * 625.0

# def GetGuidanceLifetime():
# 	return 0.2 * 0.1

# def GetMaxAngularAccel():
# 	return 1 * 10.0





def GetLaunchSpeed():
	return(0.03 * 100.0)

# def GetLaunchSound():
# 	return("Positron Torpedo")

def GetPowerCost():
	return(10.0)

# def GetName():
# 	return("2 POSITRON")

def GetDamage():
	return 0.4 * 1100.0

def GetGuidanceLifetime():
	return 10000000 * 0.1

def GetMaxAngularAccel():
	return 5 * 10.0
