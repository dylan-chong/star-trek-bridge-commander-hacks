import App
import Custom.CrazyShipAbilities.Utils

# TODO incoming damage charges your n orbs
# TODO when torpedo used, decrement the count of the other one? Or don't

TORP_RADIUS_TO_TORP_HANDLER = {
    0.022211: 'HealthDrainTorpHitHandler',
    0.022212: 'WeaponDrainTorpHitHandler',
}
TORP_RADIUS_MOE = 0.0000001

SHIELD_DRAIN = 200
SHIELD_GAIN_FACTOR = 1.2
N_SHIELDS_TO_GAIN = 2
SHIELD_SIDES = [ 
    App.ShieldClass.FRONT_SHIELDS,
    App.ShieldClass.REAR_SHIELDS,
    App.ShieldClass.TOP_SHIELDS,
    App.ShieldClass.BOTTOM_SHIELDS,
    App.ShieldClass.LEFT_SHIELDS,
    App.ShieldClass.RIGHT_SHIELDS,
]

HULL_DRAIN = 300
REPAIR_GAIN = 100
REPAIR_GAIN_DURATION_S = 5

SENSOR_DRAIN = 100
WEAPON_GAIN = 0.35

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

        hitShip = App.ShipClass_Cast(pEvent.GetTargetObject())
        firingShip = App.ShipClass_Cast(pEvent.GetFiringObject())
        isHullHit = pEvent.IsHullHit()
        handlerFunc(hitShip, firingShip, isHullHit)

    # TODO if firer is player and  charge orbs on krenim orb ship
    
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
    import math
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
    if not IsHullHit:
        return

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