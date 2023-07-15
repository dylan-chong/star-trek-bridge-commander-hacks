import App

TORP_RADIUS_TO_TORP_HANDLER = {
    1.987001: 'ShieldDrainTorpHitHandler',
}
# TODO
#  hull damage
#  disable engines + knock away
#  healing?
#  disable sensors/stun

TORP_RADIUS_MOE = 0.00000001

SHIELD_SIDES = [ 
    App.ShieldClass.FRONT_SHIELDS,
    App.ShieldClass.REAR_SHIELDS,
    App.ShieldClass.TOP_SHIELDS,
    App.ShieldClass.BOTTOM_SHIELDS,
    App.ShieldClass.LEFT_SHIELDS,
    App.ShieldClass.RIGHT_SHIELDS,
]
SHIELD_DRAIN_FACTOR = 0.2

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
        isHullHit = pEvent.IsHullHit()
        handlerFunc(hitShip, isHullHit)
        return

    
def ShieldDrainTorpHitHandler(TargetShip, IsHullHit):
    pShieldSystem = TargetShip.GetShields()

    for side in SHIELD_SIDES:
        current = pShieldSystem.GetCurShields(side)
        max = pShieldSystem.GetMaxShields(side)
        drained = max(0, current - max * SHIELD_DRAIN_FACTOR)
        pShieldSystem.SetCurShields(side, drained)