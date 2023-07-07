###############################################################################
##	Filename:	Effects.py
##	
##	Confidential and Proprietary, Copyright 2000 by Totally Games
##	
##	Special effects, including weapon hit and explosion effects.
##	
##	Created:	10/31/00 - James Therien
###############################################################################

import App

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " module...")

g_pcWarpTrailTextureName = "data/Textures/starstreak.tga"
g_fWarpTrailWidth = 0.175
g_fWarpTrailHeight = 3.00

PROMETHEUS_SHIELD_DRAIN_WEAPON_RADIUS = 0.111222333
PROMETHEUS_KNOCKBACK_SPEED_KPH = 20000

def Reset():
	global LastPrometheusKnockbackTime
	LastPrometheusKnockbackTime = -9999999

Reset()

###############################################################################
## Basic Effect components
###############################################################################

def CreateExplosionPuffHigh(fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo):

	iTimingId  = App.TGProfilingInfo_StartTiming("Effects::CreateExplosionPuffHigh")

	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.6, 1.0, 1.0, 1.0)
	pExplosion.AddColorKey(0.8, 5.0 / 255, 5.0 / 255, 5.0 / 255) # purple (why again?)

	pExplosion.AddAlphaKey(0.4, 1.0)
	pExplosion.AddAlphaKey(0.7, 0.5)
	pExplosion.AddAlphaKey(1.0, 0.0)

	pExplosion.AddSizeKey(0.0, 0.1 * fSize)
	pExplosion.AddSizeKey(0.2, 0.5 * fSize)
	pExplosion.AddSizeKey(0.6, 1.6 * fSize)
	pExplosion.AddSizeKey(0.9, 2.0 * fSize)

	pExplosion.SetEmitRadius(fSize * 0.25) 

	# set up the emitter values
	# TWEAK ME
	fFrequency = 0.09 
	pExplosion.SetEmitLife(1.5)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(fLife + 1.5)

	# Set up the geometry
	if (App.g_kSystemWrapper.GetRandomNumber(10) < 7):
		pExplosion.CreateTarget("data/Textures/Effects/ExplosionA.tga")

		# This is ONE / INVSCRALPHA
		pExplosion.SetTargetAlphaBlendModes(0, 7)
	else:
		pExplosion.CreateTarget("data/Textures/Effects/ExplosionB.tga")


	# Set up the emit point.
	# Attach it to the hit point.
	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetEmitPositionAndDirection(kEmitPos, kEmitDir)

	# Make sure not to detach the emitter.
	pExplosion.SetDetachEmitObject(0)

	# Attach the actual geometry to the effects root.
	pExplosion.AttachEffect(pAttachTo)

	App.TGProfilingInfo_StopTiming(iTimingId)

	return App.EffectAction_Create(pExplosion)


def CreateExplosionPuffMed(fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo):

	iTimingId  = App.TGProfilingInfo_StartTiming("Effects::CreateExplosionPuffMed")

	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.6, 1.0, 1.0, 1.0)
	pExplosion.AddColorKey(0.8, 5.0 / 255, 5.0 / 255, 5.0 / 255) # purple (why again?)

	pExplosion.AddAlphaKey(0.7, 1.0)
	pExplosion.AddAlphaKey(1.0, 0.0)

	pExplosion.AddSizeKey(0.0, 0.1 * fSize)
	pExplosion.AddSizeKey(0.2, 0.5 * fSize)
	pExplosion.AddSizeKey(0.6, 1.6 * fSize)
	pExplosion.AddSizeKey(0.9, 2.0 * fSize)

	pExplosion.SetEmitRadius(fSize * 0.25) 

	# set up the emitter values
	# TWEAK ME
	fFrequency = 0.3 
	pExplosion.SetEmitLife(2.0)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(fLife + 1.5)

	# Set up the geometry
	if (App.g_kSystemWrapper.GetRandomNumber(10) < 7):
		pExplosion.CreateTarget("data/Textures/Effects/ExplosionA.tga")

		# This is ONE / INVSCRALPHA
		pExplosion.SetTargetAlphaBlendModes(0, 7)
	else:
		pExplosion.CreateTarget("data/Textures/Effects/ExplosionB.tga")

	# Set up the emit point.
	# Attach it to the hit point.
	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetEmitPositionAndDirection(kEmitPos, kEmitDir)

	# Make sure not to detach the emitter.
	pExplosion.SetDetachEmitObject(0)

	# Attach the actual geometry to the effects root.
	pExplosion.AttachEffect(pAttachTo)

	App.TGProfilingInfo_StopTiming(iTimingId)

	return App.EffectAction_Create(pExplosion)


def CreateExplosionPuffLow(fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo):

	iTimingId  = App.TGProfilingInfo_StartTiming("Effects::CreateExplosionPuffLow")

	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.6, 1.0, 1.0, 1.0)
	pExplosion.AddColorKey(0.8, 5.0 / 255, 5.0 / 255, 5.0 / 255) # purple (why again?)

	pExplosion.AddAlphaKey(0.7, 1.0)
	pExplosion.AddAlphaKey(1.0, 0.0)

	pExplosion.AddSizeKey(0.0, 0.1 * fSize)
	pExplosion.AddSizeKey(0.2, 0.5 * fSize)
	pExplosion.AddSizeKey(0.6, 1.6 * fSize)
	pExplosion.AddSizeKey(0.9, 2.0 * fSize)

	pExplosion.SetEmitRadius(fSize * 0.25) 

	# set up the emitter values
	# TWEAK ME
	fFrequency = 0.5 
	pExplosion.SetEmitLife(1.5)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(fLife + 1.5)

	# Set up the geometry
	pExplosion.CreateTarget("data/Textures/Effects/ExplosionA.tga")

	# This is ONE / INVSCRALPHA
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	# Set up the emit point.
	# Attach it to the hit point.
	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetEmitPositionAndDirection(kEmitPos, kEmitDir)

	# Make sure not to detach the emitter.
	pExplosion.SetDetachEmitObject(0)

	# Attach the actual geometry to the effects root.
	pExplosion.AttachEffect(pAttachTo)

	App.TGProfilingInfo_StopTiming(iTimingId)

	return App.EffectAction_Create(pExplosion)



def CreateExplosionPlumeHigh(fConeAngle, fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo):

	iTimingId  = App.TGProfilingInfo_StartTiming("Effects::CreateExplosionPlumeHigh")

	pPlume = App.ExplosionPlumeController_Create()

	pPlume.AddColorKey(0.0, 1.0, 1.0, 1.0)
	# purple
	pPlume.AddColorKey(0.4, 5.0 / 255.0, 5.0 / 255.0, 5.0 / 255.0)
	# then to black
	pPlume.AddColorKey(0.8, 0.0, 0.0, 0.0)

	# Alpha needs to be somewhat low not to obstruct main explosion
	pPlume.AddAlphaKey(0.0, 1.0)
	pPlume.AddAlphaKey(0.3, 0.5)
	pPlume.AddAlphaKey(1.0, 0.0)

	fRand = App.g_kSystemWrapper.GetRandomNumber(100) * 0.015 * fSize
	pPlume.AddSizeKey(0.3, fSize * 1.0 + fRand)
	pPlume.AddSizeKey(1.0, fSize * 1.5 + fRand)

	fFrequency = 0.09
	pPlume.SetEmitLife(fLife / 2.0)
	pPlume.SetEmitFrequency(fFrequency)
	pPlume.SetEffectLifeTime(fLife)

	pPlume.CreateTarget("data/Textures/Effects/ExplosionA.tga")	

	pPlume.SetEmitFromObject(pEmitFrom)
	pPlume.SetEmitPositionAndDirection(kEmitPos, kEmitDir)
	pPlume.SetInheritsVelocity(1)

	# Attach the actual geometry in the graph
	pPlume.AttachEffect(pAttachTo)
	
	pPlume.SetUpRandomVelocity(fConeAngle, fSize / 10)
	pPlume.SetDetachEmitObject(0)
		
	App.TGProfilingInfo_StopTiming(iTimingId)

	return App.EffectAction_Create(pPlume)


def CreateSmokeHigh(fVelocity, fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo):

	iTimingId  = App.TGProfilingInfo_StartTiming("Effects::CreateSmokeHigh")

	pSmoke = App.AnimTSParticleController_Create()

	pSmoke.AddColorKey(0.0, 1.0, 1.0, 1.0)

	pSmoke.AddAlphaKey(0.0, 0.6)
	pSmoke.AddAlphaKey(0.5, 0.5)
	pSmoke.AddAlphaKey(1.0, 0.0)

	pSmoke.AddSizeKey(0.0, 0.2 * fSize)
	pSmoke.AddSizeKey(0.6, 1.0 * fSize)
	pSmoke.AddSizeKey(0.9, 2.0 * fSize)

	pSmoke.SetEmitVelocity(fVelocity)
	pSmoke.SetAngleVariance(60.0) # 60 is propably what we want

	# we might want to varry this with the velocity 
	# so the puffs are not so far from each other
	fFrequency = 0.05
	pSmoke.SetEmitLife(1.5)
	pSmoke.SetEmitFrequency(fFrequency)
	pSmoke.SetEffectLifeTime(10.3)

	pSmoke.SetDrawOldToNew(0)

	pSmoke.CreateTarget("data/Textures/Effects/ExplosionB.tga")

	pSmoke.SetEmitFromObject(pEmitFrom)
	pSmoke.SetEmitPositionAndDirection(kEmitPos, kEmitDir)
	pSmoke.SetInheritsVelocity(1)
	
	pSmoke.AttachEffect(pAttachTo)

	App.TGProfilingInfo_StopTiming(iTimingId)

	return App.EffectAction_Create(pSmoke)




###############################################################################
#
# CreateWeaponExplosion()
#
# Creates an explosion for a weapon hit event
#r
###############################################################################
def	CreateWeaponExplosion(fSize, fLife, pEvent):
	
	# Set up the emit point.
	# Attach it to the hit point.
	pTargetObject = pEvent.GetTargetObject()
	kEmitPos = pEvent.GetObjectHitPoint()
	kEmitDir = pEvent.GetObjectHitNormal()

	pAttachTo = pTargetObject.GetNode()
	pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pAttachTo)


	if (App.EffectController_GetEffectLevel() >= App.EffectController.HIGH):

		pExplosion = CreateExplosionPuffHigh(fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo)

		if (App.g_kSystemWrapper.GetRandomNumber(100) < 50):
			pSequence = App.TGSequence_Create()

			pSequence.AddAction(pExplosion)
			iNumPlume = App.g_kSystemWrapper.GetRandomNumber(6) + 2

			for iPoint in range( iNumPlume ):
				pSequence.AddAction(CreateExplosionPlumeHigh(120.0, fLife / 2, fSize * 0.2, pEmitFrom, kEmitPos, kEmitDir, pAttachTo))
		
			return pSequence

		# Wrap it in an action to take care of timing the start/stop calls... 
		return pExplosion

	elif (App.EffectController_GetEffectLevel() == App.EffectController.MEDIUM):

		pExplosion = CreateExplosionPuffMed(fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo)

		if (App.g_kSystemWrapper.GetRandomNumber(100) < 10):
			pSequence = App.TGSequence_Create()

			pSequence.AddAction(pExplosion)
			iNumPlume = App.g_kSystemWrapper.GetRandomNumber(5) + 1

			for iPoint in range( iNumPlume ):
				pSequence.AddAction(CreateExplosionPlumeHigh(120.0, fLife / 2, fSize * 0.2, pEmitFrom, kEmitPos, kEmitDir, pAttachTo))
		
			return pSequence

		# Wrap it in an action to take care of timing the start/stop calls... 
		return pExplosion

	else:

		return CreateExplosionPuffLow(fLife, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo)



	###
	# Some spark effect
	# Returns an effect action
def CreateWeaponSparks(fDuration, pEvent, pEffectRoot):

	fEmitRate = 0.005
	pSpark = App.SparkParticleController_Create(fDuration + (App.g_kSystemWrapper.GetRandomNumber(15) + 20) * fEmitRate, fDuration, fEmitRate)

	# Setup some default values for velocity, colors and alpha
	# Setup some default values for velocity, colors and alpha
	pSpark.AddColorKey(0.0, 1.0, 1.0, 0.8)
	pSpark.AddColorKey(0.8, 1.0, 1.0, 0.6)
	pSpark.AddColorKey(1.0, 1.0, 1.0, 0.0)
	
	pSpark.AddAlphaKey(0.0, 1.0)
	pSpark.AddAlphaKey(0.9, 0.9)
	pSpark.AddAlphaKey(1.0, 0.0)

	# TWEAK ME might still be too big on view screen
	pSpark.AddSizeKey(0.0, 0.01)
	pSpark.AddSizeKey(0.2, 0.04)
	pSpark.AddSizeKey(0.8, 0.04)
	pSpark.AddSizeKey(1.0, 0.01)

	pSpark.SetEmitVelocity(2.5)
	pSpark.SetTailLength(0.1 * (App.g_kSystemWrapper.GetRandomNumber(2) + 1))

	pSpark.SetAngleVariance(120.0)
	pSpark.SetEmitLifeVariance(fDuration / 4.0)
	pSpark.CreateTarget("data/rough.tga")

	pTargetObject = pEvent.GetTargetObject()
	kEmitPos = pEvent.GetObjectHitPoint()
	kEmitDir = pEvent.GetObjectHitNormal()
	pSpark.SetEmitFromObject(App.TGModelUtils_CastNodeToAVObject(pTargetObject.GetNode()))
	pSpark.SetEmitPositionAndDirection(kEmitPos, kEmitDir)

	# Make sure not to detach the emitter.
	pSpark.SetDetachEmitObject(0)

	pSpark.SetDamping(0.3)

	pSpark.AttachEffect(pEffectRoot)

	return	App.EffectAction_Create(pSpark)	


	###
	# Some smoke effect
	# Returns an effect action
def CreateWeaponSmoke(fDuration, fSize, pEvent, pEffectRoot):

	pTargetObject = pEvent.GetTargetObject()
	kEmitPos = pEvent.GetObjectHitPoint()
	kEmitDir = pEvent.GetObjectHitNormal()

	pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pTargetObject.GetNode())

	return CreateSmokeHigh(0.2, 2.0 + App.g_kSystemWrapper.GetRandomNumber(30) / 10.0, fSize, pEmitFrom, kEmitPos, kEmitDir, pEffectRoot)



def	CreateDebrisExplosion(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot):
	
	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.4, 1.0, 1.0, 1.0)
	pExplosion.AddColorKey(0.8, 1.0 / 255, 1.0 / 255, 1.0 / 255)

	pExplosion.AddAlphaKey(0.4, 1.0)
	pExplosion.AddAlphaKey(1.0, 0.0)

	pExplosion.AddSizeKey(0.0, 0.1 * fSize)
	pExplosion.AddSizeKey(0.2, 0.5 * fSize)
	pExplosion.AddSizeKey(0.6, 1.6 * fSize)
	pExplosion.AddSizeKey(0.9, 2.0 * fSize)

	fFrequency = 0.02
	pExplosion.SetEmitLife(1.5)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(fLife + 1.5)

	pExplosion.CreateTarget("data/Textures/Effects/ExplosionA.tga")
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	pExplosion.AttachEffect(pEffectRoot)

	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetDetachEmitObject(bOwnsEmitFrom)

	return App.EffectAction_Create(pExplosion)

def	CreateElectricExplosion(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot):
	
	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.4, 1.0, 1.0, 1.0)
	pExplosion.AddColorKey(0.8, 1.0 / 255, 1.0 / 255, 1.0 / 255)

	pExplosion.AddAlphaKey(0.4, 1.0)
	pExplosion.AddAlphaKey(1.0, 0.0)

	pExplosion.AddSizeKey(0.0, 1.0 * fSize)
	pExplosion.AddSizeKey(0.2, 1.0 * fSize)
	pExplosion.AddSizeKey(0.6, 1.0 * fSize)
	pExplosion.AddSizeKey(0.9, 1.0 * fSize)

	fFrequency = 1.0
	pExplosion.SetEmitLife(1.0)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(fLife + 2.0)

	pExplosion.CreateTarget("data/Textures/Effects/ElectricExplosion.tga")
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	pExplosion.AttachEffect(pEffectRoot)

	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetDetachEmitObject(bOwnsEmitFrom)

	return App.EffectAction_Create(pExplosion)

def	CreateSpatialExplosion(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot):
	
	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.4, 1.0, 1.0, 1.0)
	pExplosion.AddColorKey(0.8, 1.0 / 255, 1.0 / 255, 1.0 / 255)

	pExplosion.AddAlphaKey(0.4, 0.5)
	pExplosion.AddAlphaKey(1.0, 0.5)

	pExplosion.AddSizeKey(0.0, 1.0 * fSize)
	pExplosion.AddSizeKey(0.2, 1.0 * fSize)
	pExplosion.AddSizeKey(0.6, 1.0 * fSize)
	pExplosion.AddSizeKey(0.9, 1.0 * fSize)

	fFrequency = 0.01
	pExplosion.SetEmitLife(3.0)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(3.0)

	pExplosion.CreateTarget("data/Textures/Effects/ExplosionC.tga")
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	pExplosion.AttachEffect(pEffectRoot)

	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetDetachEmitObject(bOwnsEmitFrom)

	return App.EffectAction_Create(pExplosion)

def	CreateCoreExplosion(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot):
	
	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.0, 0.75, 0.75, 0.75)
	pExplosion.AddColorKey(0.9, 0.0, 0.0, 0.0)

	pExplosion.AddAlphaKey(0.0, 0.5)
	pExplosion.AddAlphaKey(0.2, 0.4)
	pExplosion.AddAlphaKey(0.4, 0.3)
	pExplosion.AddAlphaKey(0.6, 0.2)
	pExplosion.AddAlphaKey(0.8, 0.1)
	pExplosion.AddAlphaKey(1.0, 0.0)
	
	pExplosion.AddSizeKey(0.00, 0.000 * fSize)
	pExplosion.AddSizeKey(0.05, 1.500 * fSize)
	pExplosion.AddSizeKey(0.10, 2.270 * fSize)
	pExplosion.AddSizeKey(0.15, 2.770 * fSize)
	pExplosion.AddSizeKey(0.20, 3.161 * fSize)
	pExplosion.AddSizeKey(0.25, 3.501 * fSize)
	pExplosion.AddSizeKey(0.30, 3.808 * fSize)
	pExplosion.AddSizeKey(0.35, 4.090 * fSize)
	pExplosion.AddSizeKey(0.40, 4.350 * fSize)
	pExplosion.AddSizeKey(0.45, 4.588 * fSize)
	pExplosion.AddSizeKey(0.50, 4.804 * fSize)
	pExplosion.AddSizeKey(0.55, 4.999 * fSize)
	pExplosion.AddSizeKey(0.60, 5.172 * fSize)
	pExplosion.AddSizeKey(0.65, 5.324 * fSize)
	pExplosion.AddSizeKey(0.70, 5.455 * fSize)
	pExplosion.AddSizeKey(0.75, 5.564 * fSize)
	pExplosion.AddSizeKey(0.80, 5.652 * fSize)
	pExplosion.AddSizeKey(0.85, 5.719 * fSize)
	pExplosion.AddSizeKey(0.90, 5.764 * fSize)
	pExplosion.AddSizeKey(0.95, 5.788 * fSize)
	pExplosion.AddSizeKey(1.00, 5.791 * fSize)

	fFrequency = 0.01
	pExplosion.SetEmitLife(3.0)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(3.0)

	pExplosion.CreateTarget("data/Textures/Effects/CoreExplosion.tga")
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	pExplosion.AttachEffect(pEffectRoot)

	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetDetachEmitObject(bOwnsEmitFrom)

	return App.EffectAction_Create(pExplosion)

def	CreateBorgDrain(fSize, fLife, pEmitFrom, bOwnsEmitFrom, pEffectRoot):
	
	pExplosion = App.AnimTSParticleController_Create()

	pExplosion.AddColorKey(0.0, 0.0, 0.0, 0.0)
	pExplosion.AddColorKey(0.1, 0.3, 0.3, 0.3)
	pExplosion.AddColorKey(0.6, 0.3, 0.3, 0.3)
	pExplosion.AddColorKey(0.9, 0.0, 0.0, 0.0)

	pExplosion.AddAlphaKey(0.0, 0.0)
	pExplosion.AddAlphaKey(0.1, 1.0)
	pExplosion.AddAlphaKey(0.6, 1.0)
	pExplosion.AddAlphaKey(0.9, 0.0)
	
	pExplosion.AddSizeKey(0.00, 1.0 * fSize)
	pExplosion.AddSizeKey(1.00, 1.0 * fSize)

	fFrequency = 0.01
	pExplosion.SetEmitLife(3.0)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(3.0)

	pExplosion.CreateTarget("data/Textures/Effects/BorgShieldDrain.tga")
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	pExplosion.AttachEffect(pEffectRoot)

	pExplosion.SetEmitFromObject(pEmitFrom)
	pExplosion.SetDetachEmitObject(bOwnsEmitFrom)

	return App.EffectAction_Create(pExplosion)


	###
	# Some smoke effect
	# Returns an effect action
def CreateDebrisSmoke(fDuration, fSize, pEmitFrom, bOwnsEmitFrom, pEffectRoot):

	# Params are:
	# Life of emitter,
	# Base life 
	# Base frequency
	pSmoke = App.AnimTSParticleController_Create()				
	
	# Setup some default values for velocity, colors and alpha
	# Time zero.
	pSmoke.AddColorKey(0.0, 1.0, 1.0, 1.0)
	pSmoke.AddAlphaKey(0.0, 0.8)
	pSmoke.AddSizeKey(0.0, 1.0 * fSize)

	# End of life.
	pSmoke.AddColorKey(1.0, 0.1, 0.1, 0.1)
	pSmoke.AddAlphaKey(1.0, 0.0)
	pSmoke.AddSizeKey(1.0, 2.0 * fSize)

	pSmoke.SetEmitVelocity(0.2)
	pSmoke.SetEmitLifeVariance(0.2)

	pSmoke.CreateTarget("data/rough.tga")

	pSmoke.AttachEffect(pEffectRoot)

	pSmoke.SetEmitFromObject(pEmitFrom)
	pSmoke.SetDetachEmitObject(bOwnsEmitFrom)

	return App.EffectAction_Create(pSmoke)


	###
	# Some spark effect
	# Returns an effect action
def CreateDebrisSparks(fDuration, pEmitFrom, bOwnsEmitFrom, pEffectRoot):

	fEmitRate = 0.05
	pSpark = App.SparkParticleController_Create(fDuration + ((App.g_kSystemWrapper.GetRandomNumber(10) + 20) * fEmitRate), fDuration, fEmitRate)

	# Setup some default values for velocity, colors and alpha
	pSpark.AddColorKey(0.0, 1.0, 1.0, 0.8)
	pSpark.AddColorKey(0.8, 1.0, 1.0, 0.6)
	pSpark.AddColorKey(1.0, 1.0, 1.0, 0.0)
	
	pSpark.AddAlphaKey(0.0, 1.0)
	pSpark.AddAlphaKey(0.9, 0.9)
	pSpark.AddAlphaKey(1.0, 0.0)

	pSpark.AddSizeKey(0.0, 0.01)
	pSpark.AddSizeKey(0.2, 0.04)
	pSpark.AddSizeKey(0.8, 0.04)
	pSpark.AddSizeKey(1.0, 0.01)

	pSpark.SetEmitVelocity(4.0)
	pSpark.SetTailLength(0.1 * (App.g_kSystemWrapper.GetRandomNumber(2) + 1))

	pSpark.SetAngleVariance(360.0)
	pSpark.SetEmitLifeVariance(fDuration / 4.0)

	pSpark.CreateTarget("data/smooth.tga")

	pSpark.AttachEffect(pEffectRoot)

	pSpark.SetEmitFromObject(pEmitFrom)
	pSpark.SetDetachEmitObject(bOwnsEmitFrom)

	return	App.EffectAction_Create(pSpark)	

###############################################################################
#	CreateCollisionExplosion
#	
#	Create an action that'll make an explosion
#	
#	Args:	fNumberOfPuffs	- Number of puffs. :)
#			fLifeOfPuff		- Lifetime of each puff
#			vLocation		- Worldspace location for the explosion.
#			vDirection		- Direction info for the explosion.
#			pEffectRoot		- The set's effect root.
#	
#	Return:	A TGAction for the explosion.
###############################################################################
def	CreateCollisionExplosion(fSize, vLocation, vDirection, pEffectRoot):
	
	pExplosion = App.AnimTSParticleController_Create()

	# Keys to make it look good
	pExplosion.AddColorKey(0.6, 1.0, 1.0, 1.0)
	pExplosion.AddColorKey(0.8, 5.0 / 255, 5.0 / 255, 5.0 / 255) # purple

	pExplosion.AddAlphaKey(0.4, 1.0)
	pExplosion.AddAlphaKey(0.7, 0.5)
	pExplosion.AddAlphaKey(1.0, 0.0)

	pExplosion.AddSizeKey(0.0, 0.7 * fSize)
	pExplosion.AddSizeKey(0.2, 1.0 * fSize)
	pExplosion.AddSizeKey(0.6, 1.3 * fSize)
	pExplosion.AddSizeKey(0.9, 1.3 * fSize)
	pExplosion.AddSizeKey(1.0, 1.4 * fSize)

	pExplosion.SetEmitRadius(fSize * 0.25) 

	# set up the emitter values
	# TWEAKME
	# Change as well as size for LOD?
	fFrequency = 0.09 
	pExplosion.SetEmitLife(1.5)
	pExplosion.SetEmitFrequency(fFrequency)
	pExplosion.SetEffectLifeTime(5.0)

	# Set up the geometry
	pExplosion.CreateTarget("data/Textures/Effects/ExplosionA.tga")
	pExplosion.SetTargetAlphaBlendModes(0, 7)

	# Set up the emit point.
	# Attach it to the hit point.
	pExplosion.SetEmitPositionAndDirection(vLocation, vDirection)

	# Attach the actual geometry to the effects root.
	pExplosion.AttachEffect(pEffectRoot)

	# Wrap it in an action to take care of timing the start/stop calls... 
	return App.EffectAction_Create(pExplosion)


###########################
#
# Actual events handling
#
##########################

def TorpedoShieldHit(TGObject, pEvent):
	# Set up
	pObject = App.ObjectClass_Cast(TGObject)

	if not pObject:
#		debug("Unexpected NULL Ptr in TorpedoShieldHit")
		TGObject.CallNextHandler(pEvent)
		return

	# we need a set to put it in
	# this should never be null, but you never know
	pSet = pObject.GetContainingSet()
	if not pSet:
#		debug("Unexpected NULL Set Ptr in TorpedoShieldHit")
		TGObject.CallNextHandler(pEvent)
		return

	pSequence = App.TGSequence_Create()

	# the main explosion, always there
	pExplosion = CreateWeaponExplosion(pEvent.GetRadius() * 3.0, 1.25, pEvent)
	pSequence.AddAction(pExplosion)

	import LoadTacticalSounds


	#Borg Inversion Pulse
	if pEvent.GetDamage() == 15.0:

		pTarget = App.ShipClass_Cast(TGObject)
		if pTarget:
			TorpDamage = 3000
			pShields = pTarget.GetShields()
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShieldStatus = pShields.GetCurShields(ShieldDir)
				pShieldChunk = pShields.GetMaxShields(ShieldDir)
				if (pShieldStatus > TorpDamage):
					pShields.SetCurShields(ShieldDir,pShieldStatus - TorpDamage)
				if (pShieldStatus <= TorpDamage):
					pShields.SetCurShields(ShieldDir,0)

			sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsBorgDrainSounds )
			pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
			pSound.SetNode(pObject.GetNode())
			#pExplosion = CreateBorgDrain(pObject.GetRadius() * 2.0, 1.0, pEvent, 1, pSet.GetEffectRoot())
			#pSequence.AddAction(pExplosion)
			pSequence.AddAction(pSound)

	#Breen Drain Torpedo
	elif pEvent.GetDamage() == 25.0:

		pTarget = App.ShipClass_Cast(TGObject)
		if pTarget:
			if (pTarget.GetShipProperty().IsStationary() != 1) and (100 <= pTarget.GetShipProperty().GetSpecies() <= 899):   #Check to see if target is a station or a Borg ship

				TorpDamage = 0.5
				pShields = pTarget.GetShields()
				pPower = pTarget.GetPowerSubsystem()
				pImpulse = pTarget.GetImpulseEngineSubsystem()
				
				for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):   #Set all shields to zero
					pShieldStatus = pShields.GetCurShields(ShieldDir)
					pShieldChunk = pShields.GetMaxShields(ShieldDir)
					if (pShieldStatus > 0):
						pShields.SetCurShields(ShieldDir, 0 )
				
				pPowerStatus = pPower.GetCondition()		#Set Main Power Subsystem to 50%
				pPowerChunk = pPower.GetMaxCondition()
				if (pPowerStatus > pPowerChunk * TorpDamage):
					pPower.SetCondition(pPowerChunk * TorpDamage)
			
				sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsBreenDrainSounds )
				pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
				pSound.SetNode(pObject.GetNode())
				pSequence.AddAction(pSound)

				iCycleCount = 1
				while (iCycleCount < 1000):

					pElectricShockSequence = App.TGSequence_Create()
					pEmitPos = pObject.GetRandomPointOnModel()	
					pExplosion = CreateElectricExplosion(pObject.GetRadius() * 0.05, 1.0, pEmitPos, 1, pObject.GetNode())
					pElectricShockSequence.AddAction(pExplosion, App.TGAction_CreateNull(), iCycleCount * 0.005)
					pElectricShockSequence.Play()
					iCycleCount = iCycleCount + 1

	#Malon Spatial Charge
	elif pEvent.GetDamage() == 301.0 or pEvent.GetDamage() == 602.0:
		sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsBreenDrainSounds )
		pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
		pEmitPos = pObject.GetRandomPointOnModel()	
		pSound.SetNode(pObject.GetNode())
		pExplosion = CreateSpatialExplosion(2.0, 1.0, pEmitPos, 1, pSet.GetEffectRoot())
		pSequence.AddAction(pExplosion)
		pSequence.AddAction(pSound)

	#Chroniton Torpedo	
	elif pEvent.GetDamage() == 35.0:

		pTarget = App.ShipClass_Cast(TGObject)
		if pTarget:
			pTorpDamage = 900
			pHull = pTarget.GetHull()
			pHullStatus = pHull.GetCondition()
			pHullMax = pHull.GetMaxCondition()
			
			if (pHullStatus > pTorpDamage):
				pHull.SetCondition(pHullStatus - pTorpDamage)
			else:
				pHull.SetCondition(0)
		
	#Regular Impact
	else:
		sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsWeaponExplosions )
		pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
		pSound.SetNode(pObject.GetNode())
		pSequence.AddAction(pSound)
		
	pSequence.Play()


	##########################
	#
	# A torpedo hitting a ship
	#
def TorpedoHullHit(TGObject, pEvent):

	# Set up
	pObject = App.ObjectClass_Cast(TGObject)

	if not pObject:
#		debug("Unexpected NULL Ptr in TorpedoHullHit")
		TGObject.CallNextHandler(pEvent)
		return

	# we need a set to put it in
	# this should never be null, but you never know
	pSet = pObject.GetContainingSet()
	if not pSet:
#		debug("Unexpected NULL Set Ptr in TorpedoHullHit")
		TGObject.CallNextHandler(pEvent)
		return

	pSequence = App.TGSequence_Create()

	# the main explosion, always there
	pExplosion = CreateWeaponExplosion(pEvent.GetRadius() * 3.0, 1.25, pEvent)
	pSequence.AddAction(pExplosion)

	if (App.EffectController_GetEffectLevel() >= App.EffectController.MEDIUM):
		if (App.g_kSystemWrapper.GetRandomNumber(10) < 5):
			pSparks = CreateWeaponSparks(1.0, pEvent, pSet.GetEffectRoot())
			pSequence.AddAction(pSparks)

		if (App.g_kSystemWrapper.GetRandomNumber(10) < 2):
			pSmoke = CreateWeaponSmoke(1.0 + App.g_kSystemWrapper.GetRandomNumber(5) * 0.5, 0.3, pEvent, pSet.GetEffectRoot())	
			pSequence.AddAction(pSmoke, App.TGAction_CreateNull(), 0.5)

	import LoadTacticalSounds

	#Borg Inversion Pulse
	if pEvent.GetDamage() == 15.0:

		pTarget = App.ShipClass_Cast(TGObject)
		if pTarget:
			TorpDamage = 3000
			pShields = pTarget.GetShields()
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				pShieldStatus = pShields.GetCurShields(ShieldDir)
				pShieldChunk = pShields.GetMaxShields(ShieldDir)
				if (pShieldStatus > TorpDamage):
					pShields.SetCurShields(ShieldDir,pShieldStatus - TorpDamage)
				if (pShieldStatus <= TorpDamage):
					pShields.SetCurShields(ShieldDir,0)

			sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsBorgDrainSounds )
			pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
			pSound.SetNode(pObject.GetNode())
			pSequence.AddAction(pSound)

	#Breen Drain Torpedo
	elif pEvent.GetDamage() == 25.0:

		pTarget = App.ShipClass_Cast(TGObject)
		if pTarget:
			if (pTarget.GetShipProperty().IsStationary() != 1) and (100 <= pTarget.GetShipProperty().GetSpecies() <= 899):   #Check to see if target is a station or a Borg ship

				TorpDamage = 0.5
				pShields = pTarget.GetShields()
				pPower = pTarget.GetPowerSubsystem()
				pImpulse = pTarget.GetImpulseEngineSubsystem()
				
				for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):   #Set all shields to zero
					pShieldStatus = pShields.GetCurShields(ShieldDir)
					pShieldChunk = pShields.GetMaxShields(ShieldDir)
					if (pShieldStatus > 0):
						pShields.SetCurShields(ShieldDir, 0 )
				
				pPowerStatus = pPower.GetCondition()		#Set Main Power Subsystem to 50%
				pPowerChunk = pPower.GetMaxCondition()
				if (pPowerStatus > pPowerChunk * TorpDamage):
					pPower.SetCondition(pPowerChunk * TorpDamage)
			
				sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsBreenDrainSounds )
				pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
				pSound.SetNode(pObject.GetNode())
				pSequence.AddAction(pSound)

				iCycleCount = 1
				while (iCycleCount < 1000):

					pElectricShockSequence = App.TGSequence_Create()
					pEmitPos = pObject.GetRandomPointOnModel()	
					pExplosion = CreateElectricExplosion(pObject.GetRadius() * 0.05, 1.0, pEmitPos, 1, pObject.GetNode())
					pElectricShockSequence.AddAction(pExplosion, App.TGAction_CreateNull(), iCycleCount * 0.005)
					pElectricShockSequence.Play()
					iCycleCount = iCycleCount + 1

	#Malon Spatial Charge
	elif pEvent.GetDamage() == 301.0 or pEvent.GetDamage() == 602.0:
		sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsBreenDrainSounds )
		pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
		pEmitPos = pObject.GetRandomPointOnModel()	
		pSound.SetNode(pObject.GetNode())
		pExplosion = CreateSpatialExplosion(2.0, 1.0, pEmitPos, 1, pSet.GetEffectRoot())
		pSequence.AddAction(pExplosion)
		pSequence.AddAction(pSound)

	#Chroniton Torpedo	
	elif pEvent.GetDamage() == 35.0:

		pTarget = App.ShipClass_Cast(TGObject)
		if pTarget:
			pTorpDamage = 900
			pHull = pTarget.GetHull()
			pHullStatus = pHull.GetCondition()
			pHullMax = pHull.GetMaxCondition()
			
			if (pHullStatus > pTorpDamage):
				pHull.SetCondition(pHullStatus - pTorpDamage)
			else:
				pHull.SetCondition(0)

	#Regular Impact
	else:
		sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsWeaponExplosions )
		pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
		pSound.SetNode(pObject.GetNode())
		pSequence.AddAction(pSound)

	pSequence.Play()

	# wrap up
	TGObject.CallNextHandler(pEvent)

def PhaserHullHit(TGObject, pEvent):
	if (IsPrometheusSniperBeamHit(pEvent)):
		PrometheusSniperBeamHitHull(pEvent)

		# Don't produce so many smoke effects
		if (App.g_kSystemWrapper.GetRandomNumber(10) < 7):
			TGObject.CallNextHandler(pEvent)
			return

	elif (App.g_kSystemWrapper.GetRandomNumber(10) < 5):
		TGObject.CallNextHandler(pEvent)
		return

	# Set up
	pDamageable = App.DamageableObject_Cast(TGObject)

	if (pDamageable == None):
#		debug("Unexpected NULL Ptr")
		TGObject.CallNextHandler(pEvent)
		return

	# we need a set to put it in
	# this should never be null, but you never know
	pSet = pDamageable.GetContainingSet()
	if (pSet == None):
#		debug("Unexpected NULL Set Ptr")
		TGObject.CallNextHandler(pEvent)
		return

	pSequence = App.TGSequence_Create()

	if (App.g_kSystemWrapper.GetRandomNumber(10) < 5):
		pExplosion = CreateWeaponExplosion(pEvent.GetRadius() * 2.0, 1.0, pEvent)
		pSequence.AddAction(pExplosion)

		if (App.EffectController_GetEffectLevel() >= App.EffectController.MEDIUM):
			import LoadTacticalSounds
			sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsWeaponExplosions )

			pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())

			pSound.SetNode(pDamageable.GetNode())
			pSequence.AddAction(pSound)

	if (App.EffectController_GetEffectLevel() >= App.EffectController.MEDIUM):
		if (App.g_kSystemWrapper.GetRandomNumber(10) < 5):
			pSparks = CreateWeaponSparks(1.0, pEvent, pSet.GetEffectRoot())
			pSequence.AddAction(pSparks)

		# sometime do a jet
		if (App.g_kSystemWrapper.GetRandomNumber(10) < 3):
			pSmoke = CreateWeaponSmoke(1.0 + App.g_kSystemWrapper.GetRandomNumber(5) * 0.5, 0.3, pEvent, pSet.GetEffectRoot())	
			pSequence.AddAction(pSmoke)

	pSequence.Play()

	# wrap up
	TGObject.CallNextHandler(pEvent)

	###
	# part of a script action to deal with creation
def DeathExplosionDamage(pAction, pEmitPos, iObjectID, fRadius, fDamage):
	# By the time this action is called, pEmitPos may be invalid, due to save & load.
	if hasattr(pEmitPos, "INVALID"):
		#debug("DeathExplosionDamage handled an invalid NiAVObject wrapper without crashing!")
		return 0

	pObject = App.DamageableObject_GetObjectByID(None, iObjectID)

	if (pObject):
		pObject.AddDamage(pEmitPos, fRadius, fDamage)

	return (0)


	####
	# This a periodic explision happening on a debris
def CreateObjectExplosion(pObject, bSound):
	pSequence = App.TGSequence_Create()

	pEmitPos = pObject.GetRandomPointOnModel()	

	fRadius = pObject.GetRadius()

	# Damage the model with these explosions.
	if (App.g_kSystemWrapper.GetRandomNumber(10) < 11):
		pSequence.AddAction(App.TGScriptAction_Create("Effects", "DeathExplosionDamage", pEmitPos, pObject.GetObjID(), 1.5, 1000.0))
		pSequence.AddAction(App.TGScriptAction_Create("Effects", "DeathExplosionDamage", pEmitPos, pObject.GetObjID(), 1.5, 1000.0))
		pSequence.AddAction(App.TGScriptAction_Create("Effects", "DeathExplosionDamage", pEmitPos, pObject.GetObjID(), 1.5, 1000.0))

	pExplosion = CreateDebrisExplosion(fRadius * 0.25, 1.5,  pEmitPos, 1, pObject.GetNode())
	pSequence.AddAction(pExplosion)

	pSet = pObject.GetContainingSet()
	if bSound:
		sSound = GetDeathExplosionSound(pObject)

		# Add an action to play the sound.
		pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
		pSound.SetNode(pObject.GetNode())
		pSequence.AddAction(pSound)

	return pSequence


	##########################
	#
	# Final death sequence
	#
def ObjectExploding(TGObject):
	# Set up
	pObject = App.DamageableObject_Cast(TGObject)

	if (pObject == None):
#		debug("Unexpected NULL Ptr")
		return

	# we need a set to put it in
	# this should never be null, but you never know
	pSet = pObject.GetContainingSet()
	if (pSet == None):
#		debug("Unexpected NULL Set Ptr")
		return

	# This will hold the whole enchilada
	pFullSequence = App.TGSequence_Create()

	if (pObject.GetLifeTime () > 1000000.0):
		# lifetime has not been set yet, we'll randomly generate it here.
		# Generate random lifetime for 5 to 15 seconds.
		fTotalLifeLeft = float (App.g_kSystemWrapper.GetRandomNumber (100))
		fTotalLifeLeft = fTotalLifeLeft / 50.0 + 4.0	# / 25.0 + 2.0
		pObject.SetLifeTime (fTotalLifeLeft)
	else:
		# lifetime has already been set.  We'll use that to generate the effects.
		fTotalLifeLeft = pObject.GetLifeTime ()
	
	fExplosionTime = 0.0
	fLastSound = -1.0e20

	while (fExplosionTime < fTotalLifeLeft):
		# Don't play a sound for every explosion, or we end
		# up flooding all the 3D sound handles.
		bSound = 0
		if fExplosionTime - fLastSound > 0.4:
			bSound = 1
			fLastSound = fExplosionTime

		pSmallExplosionSequence = CreateObjectExplosion(pObject, bSound)
		pFullSequence.AddAction(pSmallExplosionSequence, App.TGAction_CreateNull(), fExplosionTime)
		fExplosionTime = fExplosionTime + (App.g_kSystemWrapper.GetRandomNumber(4) * 0.15)

	pFinalExplosionSequence = App.TGSequence_Create()
	

	# Note: Create more explosions with fewer patches
	pEmitPos = pObject.GetRandomPointOnModel()	

	pSparks = CreateDebrisSparks(1.0, pEmitPos, 0, pSet.GetEffectRoot())
	pFinalExplosionSequence.AddAction(pSparks)

	pExplosion = CreateDebrisExplosion(pObject.GetRadius() * 0.5, 0.5, pEmitPos, 1, pSet.GetEffectRoot())
	pFinalExplosionSequence.AddAction(pExplosion)

	pEmitPos = pObject.GetRandomPointOnModel()	
	pExplosion = CreateDebrisExplosion(pObject.GetRadius() * 0.5, 0.5, pEmitPos, 1, pSet.GetEffectRoot())
	pFinalExplosionSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.15)

	if (App.EffectController_GetEffectLevel() >= App.EffectController.MEDIUM):
		pEmitPos = pObject.GetRandomPointOnModel()	
		pExplosion = CreateDebrisExplosion(pObject.GetRadius() * 0.5, 0.5, pEmitPos, 1, pSet.GetEffectRoot())
		pFinalExplosionSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 0.15)

		pEmitPos = pObject.GetRandomPointOnModel()	
		pExplosion = CreateDebrisExplosion(pObject.GetRadius() * 3, 1.0, pEmitPos, 1, pSet.GetEffectRoot())
		pExplosion2 = CreateCoreExplosion(pObject.GetRadius() * 3, 1.0, pEmitPos, 1, pSet.GetEffectRoot())
		pFinalExplosionSequence.AddAction(pExplosion, App.TGAction_CreateNull(), 1.0)
		pFinalExplosionSequence.AddAction(pExplosion2, App.TGAction_CreateNull(), 1.0)
		#pFinalExplosionSequence.AddAction(App.TGScriptAction_Create("Effects", "DeathExplosionDamage", pEmitPos, pObject.GetObjID(), pObject.GetRadius() * 0.75, 1000.0))

	pEmitPos = pObject.GetRandomPointOnModel()	

	pSet = pObject.GetContainingSet()

	sSound = GetDeathExplosionSound(pObject)
	pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())
	pSound.SetNode(pObject.GetNode())
	pFinalExplosionSequence.AddAction(pSound)
	
	pFullSequence.AddAction(pFinalExplosionSequence, App.TGAction_CreateNull(), fTotalLifeLeft - 1.5)

	pFullSequence.Play()

	return

###############################################################################
#	CollisionEffect
#	
#	Create flashy local effects for collisions between objects.
#	
#	Args:	pDamageableObject	- The damageable object on which this
#								  effect is taking place.
#			pEvent				- The ET_OBJECT_COLLISION event.
#	
#	Return:	None
###############################################################################
def CollisionEffect(pDamageableObject, pEvent):
	pSet = pDamageableObject.GetContainingSet()
	if pSet:
		pEffectRoot = pSet.GetEffectRoot()

		# Get the collision points.
		for iPoint in range( pEvent.GetNumPoints() ):
			pPoint = pEvent.GetPoint(iPoint)

			# Add an explosion at this point.  The point is in worldspace.
			CreateCollisionExplosion(2.5, pPoint, App.TGPoint3_GetRandomUnitVector(), pEffectRoot).Play()

		# Add a single sound.
		import LoadTacticalSounds
		sSound = LoadTacticalSounds.GetRandomSound( LoadTacticalSounds.g_lsCollisionSounds )

		pSound = App.TGSoundAction_Create(sSound, 0, pSet.GetName())

		pSound.SetNode(pDamageableObject.GetNode())
		pSound.Play()

	pDamageableObject.CallNextHandler(pEvent)

###############################################################################
#	GetDeathExplosionSound
#	
#	Get the name of a death explosion sound for the given object.
#	
#	Args:	pObject	- The object we need a death explosion sound for.
#	
#	Return:	The name of a death explosion sound to use.
###############################################################################
def GetDeathExplosionSound(pObject):
	# Figure out which sound group to use for this object.
	sSound = ""
	pShipObject = App.ShipClass_Cast(pObject)
	if pShipObject:
		pShipProperty = pShipObject.GetShipProperty()
		sNewSound = pShipProperty.GetDeathExplosionSound()
		sSound = sNewSound

	# Load that sound group from the LoadTacticalSounds module.
	import LoadTacticalSounds
	lSoundGroup = None
	try:
		lSoundGroup = getattr(LoadTacticalSounds, sSound)
	except AttributeError: pass
	if not lSoundGroup:
		lSoundGroup = LoadTacticalSounds.g_lsDeathExplosions

	# Get a random sound from that group.
	return LoadTacticalSounds.GetRandomSound( lSoundGroup )

def IsPrometheusSniperBeamHit(pEvent):
	return pEvent.GetRadius() > PROMETHEUS_SHIELD_DRAIN_WEAPON_RADIUS - 0.001 \
		and pEvent.GetRadius() < PROMETHEUS_SHIELD_DRAIN_WEAPON_RADIUS + 0.001

def PrometheusSniperBeamHitHull(pEvent):
	global LastPrometheusKnockbackTime
	if (LastPrometheusKnockbackTime + 0.1 > App.g_kUtopiaModule.GetGameTime()):
		return

	LastPrometheusKnockbackTime = App.g_kUtopiaModule.GetGameTime()

	target = App.ShipClass_Cast(pEvent.GetTargetObject())
	attacker = App.ShipClass_Cast(pEvent.GetFiringObject())
	
	# Prevent full impulse from cancelling momentum so easily
	# target.SetImpulse(0, attacker.GetWorldForwardTG(), App.ShipClass.DIRECTION_MODEL_SPACE)
	target.GetImpulseEngineSubsystem().SetPowerPercentageWanted(0)

	zero = App.TGPoint3()
	zero.SetXYZ(0, 0, 0)
	target.AlignToVectors(attacker.GetWorldForwardTG(), attacker.GetWorldUpTG())
	target.SetAngularVelocity(zero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
	# import MissionLib
	# MissionLib.SetRandomRotation(target, 1000)

	knockVelocity = attacker.GetWorldForwardTG() # pEvent.GetObjectHitNormal() # TODO try GetWorldHitPoint
	knockVelocity.Unitize()
	import Bridge.XOMenuHandlers
	knockVelocity.Scale(Bridge.XOMenuHandlers.kphToInternalGameSpeed(PROMETHEUS_KNOCKBACK_SPEED_KPH))

	newVelocity = target.GetVelocityTG()
	newVelocity.Add(knockVelocity)
	target.SetVelocity(newVelocity)