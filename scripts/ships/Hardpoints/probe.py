# C:\Utopia\Current\Build\scripts\ships\Hardpoints\probe.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(0.1 * 200.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(50.000000, 50.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ControlSystem = App.HullProperty_Create("Control System")

ControlSystem.SetMaxCondition(100.000000)
ControlSystem.SetCritical(1)
ControlSystem.SetTargetable(1)
ControlSystem.SetPrimary(0)
ControlSystem.SetPosition(0.000000, -0.030000, 0.060000)
ControlSystem.SetPosition2D(64.000000, 50.000000)
ControlSystem.SetRepairComplexity(1.000000)
ControlSystem.SetDisabledPercentage(0.500000)
ControlSystem.SetRadius(0.300000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ControlSystem)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(100.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.010000, 0.000000)
ShieldGenerator.SetPosition2D(50.000000, 50.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.020000)
ShieldGenerator.SetNormalPowerPerSecond(1.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.250000, 0.500000, 1.000000, 1.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 100.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 100.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 100.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 100.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 100.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 100.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.200000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.200000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.200000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.200000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.200000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(100.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.020000, 0.000000)
SensorArray.SetPosition2D(35.000000, 40.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.022000)
SensorArray.SetNormalPowerPerSecond(1.000000)
SensorArray.SetBaseSensorRange(4000.000000)
SensorArray.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(100.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(1.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(1.000000)
ImpulseEngines.SetMaxAccel(2.750000)
ImpulseEngines.SetMaxAngularAccel(0.560000)
ImpulseEngines.SetMaxAngularVelocity(0.560000)
ImpulseEngines.SetMaxSpeed(8.730160)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
Impulse = App.EngineProperty_Create("Impulse")

Impulse.SetMaxCondition(100.000000)
Impulse.SetCritical(0)
Impulse.SetTargetable(0)
Impulse.SetPrimary(1)
Impulse.SetPosition(0.000000, -0.020000, 0.000000)
Impulse.SetPosition2D(80.000000, 75.000000)
Impulse.SetRepairComplexity(1.000000)
Impulse.SetDisabledPercentage(0.500000)
Impulse.SetRadius(0.020000)
Impulse.SetEngineType(Impulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Impulse)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(100.000000)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(0)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, 0.000000)
PowerPlant.SetPosition2D(65.000000, 65.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.200000)
PowerPlant.SetMainBatteryLimit(8000.000000)
PowerPlant.SetBackupBatteryLimit(4000.000000)
PowerPlant.SetMainConduitCapacity(100.000000)
PowerPlant.SetBackupConduitCapacity(100.000000)
PowerPlant.SetPowerOutput(15.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(100.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, 0.000000)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.250000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Warp = App.EngineProperty_Create("Warp")

Warp.SetMaxCondition(100.000000)
Warp.SetCritical(0)
Warp.SetTargetable(0)
Warp.SetPrimary(1)
Warp.SetPosition(0.000000, -0.030000, 0.000000)
Warp.SetPosition2D(95.000000, 90.000000)
Warp.SetRepairComplexity(3.000000)
Warp.SetDisabledPercentage(0.750000)
Warp.SetRadius(0.025000)
Warp.SetEngineType(Warp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp)
#################################################
Probe = App.ShipProperty_Create("Probe")

Probe.SetGenus(1)
Probe.SetSpecies(710)
Probe.SetMass(300000000000.0 * 0.001000)
Probe.SetRotationalInertia(0.100000)
Probe.SetShipName("Probe")
Probe.SetModelFilename("data/Models/Misc/Probe/Probe.nif")
Probe.SetDamageResolution(10.000000)
Probe.SetAffiliation(0)
Probe.SetStationary(0)
Probe.SetAIString("FedAttack")
Probe.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Probe)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Control System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Probe", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
