# This file is commented out because it is not used anywhere that I can see,
# and when it is run by the multiplayer script checksum, it triggers module not found errors

#                                                              ###############################################################################
#                                                              #	Filename:	Disruptor.py
#                                                              #	
#                                                              #	Confidential and Proprietary, Copyright 2000 by Totally Games
#                                                              #	
#                                                              #	Script for filling in the attributes of disruptor blasts.
#                                                              #	
#                                                              #	Created:	11/3/00 -	Erik Novales
#                                                              #       Modified:       29/10/2006 -    Lost_Jedi
#                                                              #                                           Now includes torpedo trails
#                                                              ###############################################################################
#                                                              
#                                                              import App
#                                                              import Trails.Plasma
#                                                              
#                                                              ###############################################################################
#                                                              #	Create(pTorp)
#                                                              #	
#                                                              #	Creates a disruptor blast.
#                                                              #	
#                                                              #	Args:	pTorp - the "torpedo", ready to be filled-in
#                                                              #	
#                                                              #	Return:	zero
#                                                              ###############################################################################
#                                                              def Create(pTorp):
#                                                              
#                                                              	kCoreColor = App.TGColorA()
#                                                              	kCoreColor.SetRGBA((128.0 / 255.0), (255.0 / 255.0), (128.0 / 255.0), 1.0)
#                                                              	kGlowColor = App.TGColorA()
#                                                              	kGlowColor.SetRGBA((128.0 / 255.0), (255.0 / 255.0), (128.0 / 255.0), 1.0)
#                                                              	kFlareColor = App.TGColorA()
#                                                              	kFlareColor.SetRGBA((128.0 / 255.0), (255.0 / 128.0), (128.0 / 255.0), 1.0)
#                                                              	pTorp.CreateTorpedoModel('data/Textures/Tactical/CAPlasma.tga', kCoreColor, 1.0, 1.5, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 8.0, 0.8, 0.8, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 15, 0.05, 0.27)
#                                                              	pTorp.SetDamage( GetDamage() )
#                                                              	pTorp.SetDamageRadiusFactor(0.1)
#                                                              	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
#                                                              	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
#                                                              	pTorp.SetLifetime( GetLifetime() )
#                                                              
#                                                              	# Multiplayer specific stuff.  Please, if you create a new torp
#                                                              	# type. modify the SpeciesToTorp.py file to add the new type.
#                                                              	import Multiplayer.SpeciesToTorp
#                                                              	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PLASMA2)
#                                                              
#                                                              
#                                                                      ## Add a creation handler to the torpedo :)
#                                                                      Trails.Plasma.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")
#                                                                      return(0)
#                                                              
#                                                              def AttachSmoke(self, pEvent = None):
#                                                                  ## Attach Missile Effect
#                                                                  pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
#                                                                  if not pTorpedo:
#                                                                      return (1)
#                                                                  ## Create and Play a sequence
#                                                                  Trails.Plasma.SetupSmokeTrail(pTorpedo)
#                                                                  return (0)
#                                                              
#                                                              def GetLaunchSpeed():
#                                                              	return(25.0)
#                                                              
#                                                              def GetLaunchSound():
#                                                              	return("Plasma")
#                                                              
#                                                              def GetPowerCost():
#                                                              	return(100.0)
#                                                              
#                                                              def GetName():
#                                                              	return("2 PLASMA")
#                                                              
#                                                              def GetDamage():
#                                                              	return 400.0
#                                                              
#                                                              def GetGuidanceLifetime():
#                                                              	return 30.0
#                                                              
#                                                              def GetMaxAngularAccel():
#                                                              	return 0.5
#                                                              
#                                                              def GetLifetime():
#                                                              	return 30.0
#                                                              