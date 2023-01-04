###############################################################################
#	Filename:	KlingonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of klingon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a klingon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 250.0 / 255.0, 255.0 / 255., 1.000000)	
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(50.0 / 255.0, 100.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/DualQuantumCore.tga",
					kCoreColor, 
					1.00,
					0.00,	 
					"data/Textures/Tactical/DualQuantumGlow.tga", 
					kGlowColor,
					0.1,	
					1.0,	 
					1.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,	#8	
					0.2,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(6 * 0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM2D)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Quantum Torpedo 2")

def GetPowerCost():
	return(40.0)

def GetName():
	return("2 QUANTUM")

def GetDamage():
	return 0.5 * 2200.0

def GetGuidanceLifetime():
	return 0.1

def GetMaxAngularAccel():
	return 10.0
