import App

TORP_RADIUS_TO_TORP_HANDLER = {
    0.022211: 'ShieldDrainTorpHitHandler',
    0.022212: 'HullDrainTorpHitHandler',
}
TORP_RADIUS_MOE = TORP_RADIUS_TO_TORP_HANDLER.keys()[0] * 0.01

SHIELD_DRAIN = 300
SHIELD_GAIN_FACTOR = 2.0

HULL_DRAIN = 1000
HULL_GAIN_FACTOR = 2.0

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
        return

    
def ShieldDrainTorpHitHandler(TargetShip, FiringShip, IsHullHit):
    targetShields = TargetShip.GetShields()
    firersShields = FiringShip.GetShields()

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

    shieldGain = totalDrain / len(shieldSides) * SHIELD_GAIN_FACTOR

    for side in shieldSides:
        current = firersShields.GetCurShields(side)
        limit = firersShields.GetMaxShields(side)

        gained = min(limit, current + shieldGain)
        firersShields.SetCurShields(side, gained)

def HullDrainTorpHitHandler(TargetShip, FiringShip, IsHullHit):
    if not IsHullHit:
        return

    targetHull = TargetShip.GetHull()
    if not targetHull:
        return

    targetCurrent = targetHull.GetCondition()
    targetDrained = max(0, targetCurrent - HULL_DRAIN)
    targetHull.SetCondition(targetDrained)

    targetDrain = targetCurrent - targetDrained

    import MissionLib
    player = MissionLib.GetPlayer()
    if not player or FiringShip.GetObjID() != player.GetObjID():
        # In multiplayer, both the client and server will be a
        return

    playerHull = player.GetHull()
    playerCurrent = playerHull.GetCondition()
    playerGained = min(playerHull.GetMaxCondition(), playerCurrent + targetDrain * HULL_GAIN_FACTOR)