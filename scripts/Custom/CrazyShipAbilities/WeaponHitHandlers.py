import math
import App
import Custom.CrazyShipAbilities.Utils

# TODO generate orb over time, or outgoing damage generates orbs

TORP_RADIUS_TO_TORP_HANDLER = {
    0.022211: 'HealthDrainTorpHitHandler',
    0.022212: 'WeaponDrainTorpHitHandler',
}
TORP_RADIUS_MOE = 0.0000001

SHIELD_DRAIN = 122
SHIELD_GAIN_FACTOR = 1.55
N_SHIELDS_TO_GAIN = 3
SHIELD_SIDES = [ 
    App.ShieldClass.FRONT_SHIELDS,
    App.ShieldClass.REAR_SHIELDS,
    App.ShieldClass.TOP_SHIELDS,
    App.ShieldClass.BOTTOM_SHIELDS,
    App.ShieldClass.LEFT_SHIELDS,
    App.ShieldClass.RIGHT_SHIELDS,
]
SHIELD_GAIN_PER_ORB = SHIELD_DRAIN * len(SHIELD_SIDES) * SHIELD_GAIN_FACTOR

HULL_DRAIN = 800
REPAIR_GAIN = 70
REPAIR_GAIN_DURATION_S = 4

SENSOR_DRAIN = 350
WEAPON_GAIN = 0.40

"""
Player should hit EXPECTED_USER_ORB_HIT_ACCURACY of orbs (as health orbs) on target with enough shields in order to break even with orb charge from incoming damage.
Note that even if the player's accuracy is below this mark, due to damage done to the enemy shields, the exchange is likely still positive.
"""
EXPECTED_PLAYER_ORB_HIT_ACCURACY = 0.90
HEALTH_ORBS_GAINED_PER_DAMAGE_POINT = 1.0 / (SHIELD_GAIN_PER_ORB * EXPECTED_PLAYER_ORB_HIT_ACCURACY)
# You mainly fire the health orbs so you don't need so many of the weapon orbs. They will charge up over time
WEAPON_ORBS_GAINED_PER_DAMAGE_POINT = HEALTH_ORBS_GAINED_PER_DAMAGE_POINT * 0.5

ET_DECREMENT_BUFFED_REPAIR_POINTS = App.Episode_GetNextEventType()

HasSetUpHitHandler = 0

def Reset():
    global HasSetUpHitHandler
    if HasSetUpHitHandler:
        return

    HasSetUpHitHandler = 1
    pGame = App.Game_GetCurrentGame()
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pGame, __name__ + '.WeaponHitHandler')

    pGame.AddPythonFuncHandlerForInstance(ET_DECREMENT_BUFFED_REPAIR_POINTS, __name__ + '.DecrementPlayerRepairPoints')

    # TODO what happens on a second game. does this still work?
    # TODO do i need reset function here, or can you call event manager immediately
    # TODO can change the key handler so it doesnt require a set up
    # TODO what happens when hits happen when a ship dies.


def WeaponHitHandler(_pObject, pEvent):
    targetShip = App.ShipClass_Cast(pEvent.GetTargetObject())
    firingShip = App.ShipClass_Cast(pEvent.GetFiringObject())
    isHullHit = pEvent.IsHullHit()

    if not isHullHit and IsKrenimOrbship(targetShip):
        GainOrbs(targetShip, pEvent.GetDamage())

    if pEvent.GetWeaponType() != App.WeaponHitEvent.TORPEDO:
        return

    damageRadius = pEvent.GetRadius()

    for torpRadius in TORP_RADIUS_TO_TORP_HANDLER.keys():
        if damageRadius < torpRadius - TORP_RADIUS_MOE:
            continue 
        if damageRadius > torpRadius + TORP_RADIUS_MOE:
            continue 

        funcName = TORP_RADIUS_TO_TORP_HANDLER[torpRadius]
        handlerFunc = getattr(__import__(__name__), funcName)

        handlerFunc(targetShip, firingShip, isHullHit)

def IsKrenimOrbship(Ship):
    return Ship.GetShipProperty().GetName().GetCString() == 'KrenimOrbship'
    
def GainOrbs(TargetShip, Damage):
    if not ShouldUpdateFiringShip(TargetShip) or Damage == 0:
        return

    pTorpSys = TargetShip.GetTorpedoSystem()
    if not pTorpSys:
        return

    for i in range(pTorpSys.GetNumAmmoTypes()):
        script = pTorpSys.GetProperty().GetTorpedoScript(i)
        if script == "Tactical.Projectiles.Orbs.Health Drain Orb":
            nOrbs = NumberOfOrbsToGain(Damage, HEALTH_ORBS_GAINED_PER_DAMAGE_POINT)
            pTorpSys.LoadAmmoType(i, nOrbs)
        elif script == "Tactical.Projectiles.Orbs.Weapon Drain Orb":
            nOrbs = NumberOfOrbsToGain(Damage, WEAPON_ORBS_GAINED_PER_DAMAGE_POINT)
            pTorpSys.LoadAmmoType(i, nOrbs)
    
def NumberOfOrbsToGain(Damage, OrbsPerDamage):
    NOrbs = Damage * OrbsPerDamage
    if NOrbs >= 1:
        return (NOrbs)

    ChanceOfGettingOrb = NOrbs * 1000.0
    Roll = App.g_kSystemWrapper.GetRandomNumber(1000)
    return Roll < ChanceOfGettingOrb
    
def HealthDrainTorpHitHandler(TargetShip, FiringShip, IsHullHit):
    if IsHullHit:
        return HullDrainTorpHitHandler(TargetShip, FiringShip)
    return ShieldDrainTorpHitHandler(TargetShip, FiringShip)

    # TODO animation for drain (electric line between ship)
    
def ShieldDrainTorpHitHandler(TargetShip, FiringShip):
    if not ShouldUpdateFiringShip(FiringShip):
        return
    
    totalDrain = DrainShields(TargetShip)
    BoostShields(FiringShip, totalDrain)


def DrainShields(TargetShip):
    targetShields = TargetShip.GetShields()
    totalDrain = 0

    for side in SHIELD_SIDES:
        current = targetShields.GetCurShields(side)
        drained = max(0.0, current - SHIELD_DRAIN)
        targetShields.SetCurShields(side, drained)
        totalDrain = totalDrain + (current - drained)

    return totalDrain

def BoostShields(Ship, totalDrain):
    shields = Ship.GetShields()
    perShieldGain = totalDrain * SHIELD_GAIN_FACTOR / N_SHIELDS_TO_GAIN
    
    shieldSidesWithPercents = []
    for side in SHIELD_SIDES:
        current = shields.GetCurShields(side)
        limit = shields.GetMaxShields(side)
        shieldSidesWithPercents.append((side, current / limit))

    shieldSidesWithPercents.sort(CompareForLowestShield)

    for (side, _percent) in shieldSidesWithPercents[0:N_SHIELDS_TO_GAIN]:
        current = shields.GetCurShields(side)
        limit = shields.GetMaxShields(side)

        gained = min(limit, current + perShieldGain)
        shields.SetCurShields(side, gained)


def CompareForLowestShield(ShieldTupleA, ShieldTupleB):
    (SideA, PercentA) = ShieldTupleA
    (SideB, PercentB) = ShieldTupleB
    return int(math.ceil(PercentA * 1000 - PercentB * 1000))

def CreateGetShieldPercentageTupleFunc(Shields):
    def GetShieldPercentageTuple(Side):
        current = Shields.GetCurShields(Side)
        limit = Shields.GetMaxShields(Side)
        return (Side, current / limit)
    return GetShieldPercentageTuple

def HullDrainTorpHitHandler(TargetShip, FiringShip):
    targetHull = TargetShip.GetHull()
    if not targetHull:
        return

    targetCurrent = targetHull.GetCondition()
    targetDrained = max(0, targetCurrent - HULL_DRAIN)
    targetHull.SetCondition(targetDrained)

    targetDrain = targetCurrent - targetDrained

    if not ShouldUpdateFiringShip(FiringShip) or targetDrain == 0:
        return
    
    ChangePlayerRepairPointsBy(REPAIR_GAIN)
    Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_DECREMENT_BUFFED_REPAIR_POINTS, REPAIR_GAIN_DURATION_S)


def ChangePlayerRepairPointsBy(amount):
    import MissionLib
    player = MissionLib.GetPlayer()
    if not player:
        return

    repairSubsystem = player.GetRepairSubsystem()
    if not repairSubsystem:
        return

    repair = repairSubsystem.GetProperty()
    currentPoints = repair.GetMaxRepairPoints()
    repair.SetMaxRepairPoints(currentPoints + amount)

def DecrementPlayerRepairPoints(_pObject, _pEvent):
    ChangePlayerRepairPointsBy(-REPAIR_GAIN)

def WeaponDrainTorpHitHandler(TargetShip, FiringShip, IsHullHit):
    sensorArray = TargetShip.GetSensorSubsystem()
    if not sensorArray:
        return

    current = sensorArray.GetCondition()
    drained = max(0, current - SENSOR_DRAIN)
    diff = current - drained

    if diff == 0:
        return

    sensorArray.SetCondition(drained)

    if not ShouldUpdateFiringShip(FiringShip):
        return

    deathBeamSubsystem = Custom.CrazyShipAbilities.Utils.GetSubsystemByName(FiringShip, "Death Beam")
    deathBeam = App.EnergyWeapon_Cast(deathBeamSubsystem)

    maxCharge = deathBeam.GetMaxCharge()
    currentCharge = deathBeam.GetChargeLevel()
    deathBeam.SetChargeLevel(min(maxCharge, currentCharge + WEAPON_GAIN))

def ShouldUpdateFiringShip(FiringShip):
    """
    The event handling will happen on all clients and the host. Changes to non player ships are not propagated
    As the server needs to process the target's changes and the client needs to manage it's own firer's changes
    """
    # TODO Test in multiplayer. Should we just not handle the events at all on clients?
    import MissionLib
    player = MissionLib.GetPlayer()
    return player and player.GetObjID() == FiringShip.GetObjID()