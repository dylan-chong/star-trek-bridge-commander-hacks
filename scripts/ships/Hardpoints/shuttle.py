#####  Created by:
#####  Tactical Display Icon Editor



import App
import GlobalPropertyTemplates

AAAAAAAAASubSystemHealthFactor = 3.0

# Local Templates
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(2.0000 * 1000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(63.000000, 74.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 500.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -0.020000, 0.020000)
ShieldGenerator.SetPosition2D(42.000000, 52.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(10 * 0.040000)
ShieldGenerator.SetNormalPowerPerSecond(30.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.250000, 0.500000, 1.000000, 1.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 4 * 500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 1.5 * 500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 1.5 * 500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 1.5 * 500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 1.5 * 500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 1.5 * 500.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 10 * 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 10 * 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 10 * 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 10 * 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 10 * 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 10 * 1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 500.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.020000, -0.007000)
SensorArray.SetPosition2D(85.000000, 49.000000)
SensorArray.SetRepairComplexity(0.400000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.030000)
SensorArray.SetNormalPowerPerSecond(15.000000)
SensorArray.SetBaseSensorRange(10 * 600.000000)
SensorArray.SetMaxProbes(1000 * 4)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ProbeLauncher = App.ObjectEmitterProperty_Create("Probe Launcher")

ProbeLauncherForward = App.TGPoint3()
ProbeLauncherForward.SetXYZ(0.000000, 1.000000, 0.000000)
ProbeLauncherUp = App.TGPoint3()
ProbeLauncherUp.SetXYZ(0.000000, 0.000000, 1.000000)
ProbeLauncherRight = App.TGPoint3()
ProbeLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
ProbeLauncher.SetOrientation(ProbeLauncherForward, ProbeLauncherUp, ProbeLauncherRight)
ProbeLauncherPosition = App.TGPoint3()
ProbeLauncherPosition.SetXYZ(0.000000, 0.575000, -0.023000)
ProbeLauncher.SetPosition(ProbeLauncherPosition)
ProbeLauncher.SetEmittedObjectType(ProbeLauncher.OEP_PROBE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ProbeLauncher)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 500.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(52.000000, 59.000000)
ImpulseEngines.SetRepairComplexity(1.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.003000)
ImpulseEngines.SetNormalPowerPerSecond(20.000000)
ImpulseEngines.SetMaxAccel(1000000000 * 6.000000)
ImpulseEngines.SetMaxAngularAccel(3 * 0.790000)
ImpulseEngines.SetMaxAngularVelocity(5 * 0.790000)
ImpulseEngines.SetMaxSpeed(4 * 9.523810)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 250.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.025000, -0.040000, 0.017000)
PortImpulse.SetPosition2D(25.000000, 81.000000)
PortImpulse.SetRepairComplexity(1.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.030000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 250.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.025000, -0.040000, 0.017000)
StarImpulse.SetPosition2D(102.000000, 79.000000)
StarImpulse.SetRepairComplexity(1.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.030000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 500.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.030000, -0.015000)
WarpCore.SetPosition2D(66.000000, 100.000000)
WarpCore.SetRepairComplexity(1.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.040000)
WarpCore.SetMainBatteryLimit(10000.000000)
WarpCore.SetBackupBatteryLimit(10000.000000)
WarpCore.SetMainConduitCapacity(113.000000)
WarpCore.SetBackupConduitCapacity(13.000000)
WarpCore.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 500.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, -0.010000)
WarpEngines.SetPosition2D(79.000000, 59.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.010000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 250.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.036000, -0.020000, -0.017000)
PortWarp.SetPosition2D(9.000000, 94.000000)
PortWarp.SetRepairComplexity(1.000000)
PortWarp.SetDisabledPercentage(0.500000)
PortWarp.SetRadius(0.030000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 250.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.036000, -0.020000, -0.017000)
StarWarp.SetPosition2D(124.000000, 93.000000)
StarWarp.SetRepairComplexity(1.000000)
StarWarp.SetDisabledPercentage(0.500000)
StarWarp.SetRadius(0.030000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
AAAAAAPhaserDamageFactor = 5

Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 250.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000175, 0.015236, -0.000475)
Phasers.SetPosition2D(79.000000, 59.000000)
Phasers.SetRepairComplexity(1.000000)
Phasers.SetDisabledPercentage(0.750000)
Phasers.SetRadius(0.002500)
Phasers.SetNormalPowerPerSecond(10.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(1)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
ForwardPhaser1 = App.PhaserProperty_Create("Forward Phaser 1")

ForwardPhaser1.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 250.000000)
ForwardPhaser1.SetCritical(0)
ForwardPhaser1.SetTargetable(1)
ForwardPhaser1.SetPrimary(1)
ForwardPhaser1.SetPosition(-0.012500, 0.055000, 0.000000)
ForwardPhaser1.SetPosition2D(42.000000, 16.000000)
ForwardPhaser1.SetRepairComplexity(1.000000)
ForwardPhaser1.SetDisabledPercentage(0.500000)
ForwardPhaser1.SetRadius(10 * 0.034000)
ForwardPhaser1.SetDumbfire(0)
ForwardPhaser1.SetWeaponID(1)
ForwardPhaser1.SetGroups(1)
ForwardPhaser1.SetDamageRadiusFactor(0.100000)
ForwardPhaser1.SetIconNum(364)
ForwardPhaser1.SetIconPositionX(37.000000)
ForwardPhaser1.SetIconPositionY(31.000000)
ForwardPhaser1.SetIconAboveShip(1)
ForwardPhaser1.SetFireSound("Galaxy Phaser")
ForwardPhaser1.SetMaxCharge(1.000000)
ForwardPhaser1.SetMaxDamage(AAAAAAPhaserDamageFactor * 320.000000)
ForwardPhaser1.SetMaxDamageDistance(1.5 * 100.000000)
ForwardPhaser1.SetMinFiringCharge(1.000000)
ForwardPhaser1.SetNormalDischargeRate(200.000000)
ForwardPhaser1.SetRechargeRate(0.500000)
ForwardPhaser1.SetIndicatorIconNum(510)
ForwardPhaser1.SetIndicatorIconPositionX(33.000000)
ForwardPhaser1.SetIndicatorIconPositionY(26.000000)
ForwardPhaser1Forward = App.TGPoint3()
ForwardPhaser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardPhaser1Up = App.TGPoint3()
ForwardPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardPhaser1.SetOrientation(ForwardPhaser1Forward, ForwardPhaser1Up)
ForwardPhaser1.SetWidth(0.001000)
ForwardPhaser1.SetLength(0.001000)
ForwardPhaser1.SetArcWidthAngles(-0.959931, 0.959931)
ForwardPhaser1.SetArcHeightAngles(-1.047198, 0.610865)
ForwardPhaser1.SetPhaserTextureStart(0)
ForwardPhaser1.SetPhaserTextureEnd(7)
ForwardPhaser1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
ForwardPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
ForwardPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
ForwardPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
ForwardPhaser1.SetInnerCoreColor(kColor)
ForwardPhaser1.SetNumSides(6)
ForwardPhaser1.SetMainRadius(0.020000)
ForwardPhaser1.SetTaperRadius(0.010000)
ForwardPhaser1.SetCoreScale(0.500000)
ForwardPhaser1.SetTaperRatio(0.250000)
ForwardPhaser1.SetTaperMinLength(5.000000)
ForwardPhaser1.SetTaperMaxLength(30.000000)
ForwardPhaser1.SetLengthTextureTilePerUnit(0.500000)
ForwardPhaser1.SetPerimeterTile(1.000000)
ForwardPhaser1.SetTextureSpeed(2.500000)
ForwardPhaser1.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardPhaser1)
#################################################
ForwardPhaser2 = App.PhaserProperty_Create("Forward Phaser 2")

ForwardPhaser2.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 250.000000)
ForwardPhaser2.SetCritical(0)
ForwardPhaser2.SetTargetable(1)
ForwardPhaser2.SetPrimary(1)
ForwardPhaser2.SetPosition(0.012500, 0.055000, 0.000000)
ForwardPhaser2.SetPosition2D(90.000000, 16.000000)
ForwardPhaser2.SetRepairComplexity(1.000000)
ForwardPhaser2.SetDisabledPercentage(0.500000)
ForwardPhaser2.SetRadius(10 * 0.034000)
ForwardPhaser2.SetDumbfire(0)
ForwardPhaser2.SetWeaponID(1)
ForwardPhaser2.SetGroups(1)
ForwardPhaser2.SetDamageRadiusFactor(0.100000)
ForwardPhaser2.SetIconNum(364)
ForwardPhaser2.SetIconPositionX(89.000000)
ForwardPhaser2.SetIconPositionY(31.000000)
ForwardPhaser2.SetIconAboveShip(1)
ForwardPhaser2.SetFireSound("Galaxy Phaser")
ForwardPhaser2.SetMaxCharge(3 * 1.000000)
ForwardPhaser2.SetMaxDamage(AAAAAAPhaserDamageFactor * 320.000000)
ForwardPhaser2.SetMaxDamageDistance(1.5 * 100.000000)
ForwardPhaser2.SetMinFiringCharge(1.000000)
ForwardPhaser2.SetNormalDischargeRate(200.000000)
ForwardPhaser2.SetRechargeRate(0.500000)
ForwardPhaser2.SetIndicatorIconNum(510)
ForwardPhaser2.SetIndicatorIconPositionX(85.000000)
ForwardPhaser2.SetIndicatorIconPositionY(26.000000)
ForwardPhaser2Forward = App.TGPoint3()
ForwardPhaser2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardPhaser2Up = App.TGPoint3()
ForwardPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardPhaser2.SetOrientation(ForwardPhaser2Forward, ForwardPhaser2Up)
ForwardPhaser2.SetWidth(0.001000)
ForwardPhaser2.SetLength(0.001000)
ForwardPhaser2.SetArcWidthAngles(-0.959931, 0.959931)
ForwardPhaser2.SetArcHeightAngles(-1.047198, 0.610865)
ForwardPhaser2.SetPhaserTextureStart(0)
ForwardPhaser2.SetPhaserTextureEnd(7)
ForwardPhaser2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
ForwardPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
ForwardPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
ForwardPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
ForwardPhaser2.SetInnerCoreColor(kColor)
ForwardPhaser2.SetNumSides(6)
ForwardPhaser2.SetMainRadius(0.020000)
ForwardPhaser2.SetTaperRadius(0.010000)
ForwardPhaser2.SetCoreScale(0.500000)
ForwardPhaser2.SetTaperRatio(0.250000)
ForwardPhaser2.SetTaperMinLength(5.000000)
ForwardPhaser2.SetTaperMaxLength(30.000000)
ForwardPhaser2.SetLengthTextureTilePerUnit(0.500000)
ForwardPhaser2.SetPerimeterTile(1.000000)
ForwardPhaser2.SetTextureSpeed(2.500000)
ForwardPhaser2.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardPhaser2)


#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(1500.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(64.000000, 10.000000)
Torpedoes.SetRepairComplexity(1.000000)
Torpedoes.SetDisabledPercentage(0.500000)
Torpedoes.SetRadius(0.060000)
Torpedoes.SetNormalPowerPerSecond(10.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 50)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.Photon 9001")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
ForwardTube1 = App.TorpedoTubeProperty_Create("Forward Tube 1")

AAAAAAAAAAAATorpedoReloadDelay = 30#40.000000
ForwardTube1.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 3000.000000)
ForwardTube1.SetCritical(0)
ForwardTube1.SetTargetable(1)
ForwardTube1.SetPrimary(1)
ForwardTube1.SetPosition(0.000000, 0.340000, 0.017000)
ForwardTube1.SetPosition2D(41.000000, 26.000000)
ForwardTube1.SetRepairComplexity(1.000000)
ForwardTube1.SetDisabledPercentage(0.500000)
ForwardTube1.SetRadius(500 * 0.050000)
ForwardTube1.SetDumbfire(1)
ForwardTube1.SetWeaponID(0)
ForwardTube1.SetGroups(1)
ForwardTube1.SetDamageRadiusFactor(0.100000)
ForwardTube1.SetIconNum(370)
ForwardTube1.SetIconPositionX(61.000000)
ForwardTube1.SetIconPositionY(51.000000)
ForwardTube1.SetIconAboveShip(1)
ForwardTube1.SetImmediateDelay(0.250000)
ForwardTube1.SetReloadDelay(AAAAAAAAAAAATorpedoReloadDelay)
ForwardTube1.SetMaxReady(1)
ForwardTube1Direction = App.TGPoint3()
ForwardTube1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTube1.SetDirection(ForwardTube1Direction)
ForwardTube1Right = App.TGPoint3()
ForwardTube1Right.SetXYZ(-1.000000, 0.000000, 0.000000)
ForwardTube1.SetRight(ForwardTube1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTube1)


#################################################
Shuttle = App.ShipProperty_Create("Shuttle")

Shuttle.SetGenus(1)
Shuttle.SetSpecies(106)
Shuttle.SetMass(0.035000)
Shuttle.SetRotationalInertia(3.500000)
Shuttle.SetShipName("Shuttle")
Shuttle.SetModelFilename("data/Models/Ships/Shuttle/Shuttle.nif")
Shuttle.SetDamageResolution(10.000000)
Shuttle.SetAffiliation(0)
Shuttle.SetStationary(0)
Shuttle.SetAIString("NonFedAttack")
Shuttle.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Shuttle)
#################################################
Repair = App.RepairSubsystemProperty_Create("Repair")

Repair.SetMaxCondition(AAAAAAAAASubSystemHealthFactor * 5000.000000)
Repair.SetCritical(0)
Repair.SetTargetable(1)
Repair.SetPrimary(1)
Repair.SetPosition(0.000000, 0.000000, 0.000000)
Repair.SetPosition2D(62.000000, 48.000000)
Repair.SetRepairComplexity(1.000000)
Repair.SetDisabledPercentage(0.500000)
Repair.SetRadius(0.250000)
Repair.SetNormalPowerPerSecond(1.000000)
Repair.SetMaxRepairPoints(100 * 1.000000)
Repair.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)
#################################################
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000000, 0.110000, 0.020000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, -0.120000, 0.020000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
ViewscreenLeft = App.PositionOrientationProperty_Create("ViewscreenLeft")

ViewscreenLeftForward = App.TGPoint3()
ViewscreenLeftForward.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeftUp = App.TGPoint3()
ViewscreenLeftUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenLeftRight = App.TGPoint3()
ViewscreenLeftRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenLeft.SetOrientation(ViewscreenLeftForward, ViewscreenLeftUp, ViewscreenLeftRight)
ViewscreenLeftPosition = App.TGPoint3()
ViewscreenLeftPosition.SetXYZ(-0.060000, 0.060000, 0.020000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.060000, 0.060000, 0.020000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 0.080000, 0.040000)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000000, 0.080000, -0.030000)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
FirstPersonCamera = App.PositionOrientationProperty_Create("FirstPersonCamera")

FirstPersonCameraForward = App.TGPoint3()
FirstPersonCameraForward.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonCameraUp = App.TGPoint3()
FirstPersonCameraUp.SetXYZ(0.000000, 0.000000, 1.000000)
FirstPersonCameraRight = App.TGPoint3()
FirstPersonCameraRight.SetXYZ(1.000000, 0.000000, 0.000000)
FirstPersonCamera.SetOrientation(FirstPersonCameraForward, FirstPersonCameraUp, FirstPersonCameraRight)
FirstPersonCameraPosition = App.TGPoint3()
FirstPersonCameraPosition.SetXYZ(0.000000, 0.110000, 0.020000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)



Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(1500.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, 0.000000, 0.000000)
Tractors.SetPosition2D(0.000000, 0.000000)
Tractors.SetRepairComplexity(1.000000)
Tractors.SetDisabledPercentage(0.500000)
Tractors.SetRadius(0.050000)
Tractors.SetNormalPowerPerSecond(550.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(0)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")

ForwardTractor.SetMaxCondition(1500.000000)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(1)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(-0.000500, 0.575000, -0.023000)
ForwardTractor.SetPosition2D(41.000000, 57.000000)
ForwardTractor.SetRepairComplexity(1.000000)
ForwardTractor.SetDisabledPercentage(0.500000)
ForwardTractor.SetRadius(0.050000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(1)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.300000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(0.000000)
ForwardTractor.SetIconPositionY(0.000000)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Tractor Beam")
ForwardTractor.SetMaxCharge(6.000000)
ForwardTractor.SetMaxDamage(750.000000)
ForwardTractor.SetMaxDamageDistance(90.000000)
ForwardTractor.SetMinFiringCharge(3.000000)
ForwardTractor.SetNormalDischargeRate(1.000000)
ForwardTractor.SetRechargeRate(0.300000)
ForwardTractor.SetIndicatorIconNum(0)
ForwardTractor.SetIndicatorIconPositionX(0.000000)
ForwardTractor.SetIndicatorIconPositionY(0.000000)
ForwardTractorForward = App.TGPoint3()
ForwardTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractorUp = App.TGPoint3()
ForwardTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor.SetOrientation(ForwardTractorForward, ForwardTractorUp)
ForwardTractor.SetArcWidthAngles(-0.872665, 0.872665)
ForwardTractor.SetArcHeightAngles(-1.047198, 0.349066)
ForwardTractor.SetTractorBeamWidth(0.400000)
ForwardTractor.SetTextureStart(0)
ForwardTractor.SetTextureEnd(0)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
ForwardTractor.SetInnerCoreColor(kColor)
ForwardTractor.SetNumSides(12)
ForwardTractor.SetMainRadius(0.060000)
ForwardTractor.SetTaperRadius(0.000000)
ForwardTractor.SetCoreScale(0.450000)
ForwardTractor.SetTaperRatio(0.200000)
ForwardTractor.SetTaperMinLength(1.000000)
ForwardTractor.SetTaperMaxLength(5.000000)
ForwardTractor.SetLengthTextureTilePerUnit(0.250000)
ForwardTractor.SetPerimeterTile(1.000000)
ForwardTractor.SetTextureSpeed(0.200000)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTractor)
#################################################
ShuttleBay = App.ObjectEmitterProperty_Create("Shuttle Bay")

ShuttleBayForward = App.TGPoint3()
ShuttleBayForward.SetXYZ(0.000000, 0.000000, -10.000000)
ShuttleBayUp = App.TGPoint3()
ShuttleBayUp.SetXYZ(0.000000, 1.000000, 0.000000)
ShuttleBayRight = App.TGPoint3()
ShuttleBayRight.SetXYZ(1.000000, 0.000000, 0.000000)
ShuttleBay.SetOrientation(ShuttleBayForward, ShuttleBayUp, ShuttleBayRight)
ShuttleBayPosition = App.TGPoint3()
ShuttleBayPosition.SetXYZ(0.000000, 0.030000, -0.023000)
ShuttleBay.SetPosition(ShuttleBayPosition)
ShuttleBay.SetEmittedObjectType(ShuttleBay.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay)

# Property Set
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenLeft", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenRight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenUp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenDown", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FirstPersonCamera", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tube 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Probe Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)