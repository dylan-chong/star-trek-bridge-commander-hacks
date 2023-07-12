# File: Q (Python 1.5)

# Modification of Quantum 2.py

import App

SIZE = 6.0

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(150.0 / 255.0, 180.0 / 255.0, 255.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 255.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, SIZE * 0.3, 1.3, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, SIZE * 3.0, 0.3, 0.6, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, SIZE * 8, 0.2, 0.2)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.FULLIMPULSEBLOCKER)
    return 0


def GetLaunchSpeed():
    return 5.0


def GetLaunchSound():
    return 'Positron Torpedo'


def GetPowerCost():
    return 40.0


def GetName():
    return 'Full Impulse Blocker'


def GetDamage():
    return 4000.0


def GetGuidanceLifetime():
    return 0.0


def GetMaxAngularAccel():
    return 0.0