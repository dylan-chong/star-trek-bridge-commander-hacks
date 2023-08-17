import App

CORE_SIZE = 0.7
GLOW_SIZE = 0.9

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 255.0 / 255.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(150.0 / 255.0, 180.0 / 255.0, 255.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, CORE_SIZE, 1.3, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 3.0, GLOW_SIZE, 0.6, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, 8, 0.2, 0.2)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.022212)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.WEAPONDRAINORB)
    return 0


def GetLaunchSpeed():
    return 50.0


def GetLaunchSound():
    return 'Positron Torpedo'


def GetPowerCost():
    return 40.0


def GetName():
    return 'Weapon Drain Orb'


def GetDamage():
    return 1.0


def GetGuidanceLifetime():
    return 0.05


def GetMaxAngularAccel():
    return 1.8