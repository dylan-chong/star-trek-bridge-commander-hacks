import App

TORP_RADIUS_TO_TORP_HANDLER = {
    0.022211: 'ShieldDrainTorpHitHandler',
}
# TODO
#  disable engines + knock away
#  disable sensors/stun
#  healing?

TORP_RADIUS_MOE = TORP_RADIUS_TO_TORP_HANDLER.keys()[0] * 0.01

SHIELD_DRAIN = 300
SHIELD_GAIN = SHIELD_DRAIN * 2.0

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

    shieldGain = totalDrain / (SHIELD_DRAIN * len(shieldSides)) * SHIELD_GAIN

    # TODO only once the ability activated
    for side in shieldSides:
        current = firersShields.GetCurShields(side)
        limit = firersShields.GetMaxShields(side)

        gained = min(limit, current + shieldGain)
        firersShields.SetCurShields(side, gained)