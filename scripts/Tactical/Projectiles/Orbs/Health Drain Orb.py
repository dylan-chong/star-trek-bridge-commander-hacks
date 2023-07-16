import App

CORE_SIZE = 3.5
GLOW_SIZE = 2.0
FLARE_SIZE = 16.0

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(49.0 / 255.0, 190.0 / 255.0, 48.0 / 255., 1.000000)	
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(218.0 / 255.0, 250.0 / 255.0, 202.0 / 255.0, 1.000000)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, CORE_SIZE * 0.3, 1.3, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, GLOW_SIZE * 3.0, 0.3, 0.6, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, FLARE_SIZE * 8, 0.2, 0.2)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.0222011)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.SHIELDDRAINORB)
    return 0


def GetLaunchSpeed():
    return 50.0


def GetLaunchSound():
    return 'Positron Torpedo'


def GetPowerCost():
    return 40.0


def GetName():
    return 'Health Drain Orb'


def GetDamage():
    return 1.0


def GetGuidanceLifetime():
    return 0.05


def GetMaxAngularAccel():
    return 2.6