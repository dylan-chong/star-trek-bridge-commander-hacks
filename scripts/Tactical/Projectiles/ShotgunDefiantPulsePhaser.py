###############################################################################
#	Filename:	Disruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a disruptor blast.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 200, 150, 45)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 120, 20, 6)

	LENGTH = 1.0
	RADIUS = 1.3
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, LENGTH * 0.9, RADIUS * 0.07)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.SHOTGUNDEFIANTPULSEPHASER)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Pulse Phaser")

def GetPowerCost():
	return(10.0)

def GetName():
	return("PulsePhaser")

def GetDamage():
	return 1.3 * 160.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.1

def GetLifetime():
	return 0.1 * 10.0