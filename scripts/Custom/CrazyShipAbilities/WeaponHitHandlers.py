import App
import Custom.CrazyShipAbilities.Utils

TORP_RADIUS_TO_TORP_HANDLER = {
    0.022211: 'HealthDrainTorpHitHandler',
    0.022212: 'WeaponDrainTorpHitHandler',
}
TORP_RADIUS_MOE = TORP_RADIUS_TO_TORP_HANDLER.keys()[0] * 0.01

SHIELD_DRAIN = 300
SHIELD_GAIN_FACTOR = 2.0
HULL_DRAIN = 300
HULL_GAIN_FACTOR = 1.2

SENSOR_DRAIN = 300
WEAPON_GAIN = 0.3

HasSetUpHitHandler = 0

def Reset():
    global HasSetUpHitHandler
    if HasSetUpHitHandler:
        return

    HasSetUpHitHandler = 1
    pGame = App.Game_GetCurrentGame()
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pGame, __name__ + '.WeaponHitHandler')
    # TODO what happens on a second game. does this still work?
    # TODO do i need reset function here, or can you call event manager immediately
    # TODO can change the key handler so it doesnt require a set up
    # TODO what happens when hits happen when a ship dies.


def WeaponHitHandler(_pObject, pEvent):
    print('weapon hit ' + str(pEvent.GetWeaponType()))
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
    targetShields = TargetShip.GetShields()

    shieldSides = [ 
        App.ShieldClass.FRONT_SHIELDS,
        App.ShieldClass.REAR_SHIELDS,
        App.ShieldClass.TOP_SHIELDS,
        App.ShieldClass.BOTTOM_SHIELDS,
        App.ShieldClass.LEFT_SHIELDS,
        App.ShieldClass.RIGHT_SHIELDS,
    ]

    totalDrain = 0

    for side in shieldSides:
        current = targetShields.GetCurShields(side)
        drained = max(0.0, current - SHIELD_DRAIN)
        targetShields.SetCurShields(side, drained)
        totalDrain = totalDrain + (current - drained)

    if not ShouldUpdateFiringShip(FiringShip):
        return

    firersShields = FiringShip.GetShields()
    shieldGain = totalDrain / len(shieldSides) * SHIELD_GAIN_FACTOR

    for side in shieldSides:
        current = firersShields.GetCurShields(side)
        limit = firersShields.GetMaxShields(side)

        gained = min(limit, current + shieldGain)
        firersShields.SetCurShields(side, gained)

def HullDrainTorpHitHandler(TargetShip, FiringShip):
    targetHull = TargetShip.GetHull()
    if not targetHull:
        return

    targetCurrent = targetHull.GetCondition()
    targetDrained = max(0, targetCurrent - HULL_DRAIN)
    targetHull.SetCondition(targetDrained)

    targetDrain = targetCurrent - targetDrained

    # TODO can you temporarily boost the repair speed of the firing ship instead?

    if not ShouldUpdateFiringShip(FiringShip):
        return

    firerHull = FiringShip.GetHull()
    firerCurrent = firerHull.GetCondition()
    firerGained = min(firerHull.GetMaxCondition(), firerCurrent + targetDrain * HULL_GAIN_FACTOR)
    firerHull.SetCondition(firerGained)

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