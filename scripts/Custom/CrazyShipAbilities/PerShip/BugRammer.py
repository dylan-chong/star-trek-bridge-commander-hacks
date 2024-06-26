"""
BugRammer - highly maneuverable ship that uses collisions as it's primary attack method.
Upon colliding with a ship with sufficient speed, does damage to the enemy ship, and any damage done to the rammer itself is reversed.
Healing over a short time is also triggered, and also the rammer is increased in size temporarily to increase speed and collision damage.

Damage done to the shields is bled-through as a balancing mechanism.
The rammer can collide with enemies to heal and offset this damage, therefore allowing this ship to fulfill the role as a tank.
"""

import math
import App
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils
import Custom.CrazyShipAbilities.Constants

ET_STOP_BUFF = App.UtopiaModule_GetNextEventType()
ET_RECORD_RAMMER_HEALTH = App.UtopiaModule_GetNextEventType()

BUFF_DURATION_S = 6

HEALING_FROM_DAMAGE_FACTOR = 1.5 * Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER

MIN_SCALE_BOOST = 0.1
MAX_SCALE_BOOST = 0.5
DAMAGE_BOOST_FROM_SCALE = 0.2

# 7.5 force is pretty normal for a impulse 6 impact (a pretty reasonable speed to get an impact)
BASE_RAM_DAMAGE_VELOCITY = 7.5
BASE_RAM_DAMAGE = 1000.0
# 20 force is pretty normal for a impulse 9 impact. Do triple damage
HIGH_BASE_RAM_DAMAGE_VELOCITY = 20.0
HIGH_BASE_RAM_DAMAGE = BASE_RAM_DAMAGE * 3.0
# Ram limits
MIN_BASE_RAM_DAMAGE_VELOCITY = 2.0
MIN_BASE_RAM_DAMAGE = 100
MAX_BASE_RAM_DAMAGE = BASE_RAM_DAMAGE * 4.0

# Prevent grinding collisions (many tiny collisions) from damaging enemy / healing too much
MIN_COLLISION_PERIOD_S = 0.333

SHIELD_DAMAGE_BLEEDTHROUGH = 0.85

def Initialize(OverrideExisting):
	global RammerNames, Buffs, RecordHealthTimerId, LastUsedCollisionTime, LastRammerHealth
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	RammerNames = []
	Buffs = []
	LastUsedCollisionTime = None
	LastRammerHealth = None

	Custom.CrazyShipAbilities.Utils.ReregisterEventHanders([
		(App.ET_OBJECT_COLLISION, 'ObjectCollisionHandler'),
		(App.ET_WEAPON_HIT, 'WeaponHitHandler'),
		(ET_STOP_BUFF, 'BuffFinished'),
		(ET_RECORD_RAMMER_HEALTH, 'RecordRammerHealth'),
	], App.Game_GetCurrentGame(), __name__)

	if 'RecordHealthTimerId' in globals().keys():
		App.g_kTimerManager.DeleteTimer(RecordHealthTimerId)
	RecordHealthTimerId = CreateHealthRecorderTimer()

def GetTitle():
	return ''

def GetCooldownS():
	return -1

def GetNReady():
	return 0

def GetNCooldowns():
	return 0

def UseAbility(_pPlayer):
	pass

def CreateHealthRecorderTimer():
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(ET_RECORD_RAMMER_HEALTH)
	pEvent.SetDestination(App.Game_GetCurrentGame())

	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 0.125)
	pTimer.SetDelay(0.125)
	pTimer.SetDuration(-1)
	pTimer.SetEvent(pEvent)
	return App.g_kTimerManager.AddTimer(pTimer)

def RecordRammerHealth(_pObject = None, _pEvent = None):
	global LastRammerHealth
	if not IsPlayerRammer(): return

	player = App.Game_GetCurrentPlayer()
	hull = player.GetHull()
	if not hull: return
	LastRammerHealth = hull.GetCondition()

def ObjectCollisionHandler(pObject, pEvent):
	source = App.ShipClass_Cast(pEvent.GetSource())
	target = App.ShipClass_Cast(pEvent.GetDestination())

	if not source or not Custom.CrazyShipAbilities.Utils.IsPlayer(source) or not IsRammer(source):
		return

	ReversePlayerRammingDamage()
	RecordRammerHealth() # Prevent 2 close collisions from reverting healing

	if not target: return
	damage = CalcRamDamage(target, source)

	if not CanUseCollisionYet(): return
	SetCollisionUsed()

	DamageHull(damage, target)
	HealAndBuffFromDamageDealt(damage)

def CanUseCollisionYet():
	if not LastUsedCollisionTime: return 1
	return App.g_kUtopiaModule.GetGameTime() > LastUsedCollisionTime + MIN_COLLISION_PERIOD_S

def SetCollisionUsed():
	global LastUsedCollisionTime
	LastUsedCollisionTime = App.g_kUtopiaModule.GetGameTime()

def WeaponHitHandler(pObject, pEvent):
	target = App.ShipClass_Cast(pEvent.GetTargetObject())
	if not IsRammer(target): return

	if pEvent.IsHullHit():
		damageMultiplier = Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER - 1
	else:
		damageMultiplier = SHIELD_DAMAGE_BLEEDTHROUGH * Custom.CrazyShipAbilities.Constants.BUG_RAMMER_HEALTH_MULTIPLIER

	DamageHull(damageMultiplier * pEvent.GetDamage(), target)

def DamageHull(damage, ship):
	hull = ship.GetHull()
	hull.SetCondition(hull.GetCondition() - damage)

def ReversePlayerRammingDamage():
	player = App.Game_GetCurrentPlayer()
	hull = player.GetHull()
	if not hull or not LastRammerHealth: return

	hull.SetCondition(LastRammerHealth)
	if hull.GetCondition() == hull.GetMaxCondition():
		player.RemoveVisibleDamage()

def CalcRamDamage(target, source):
	GRADIENT = (HIGH_BASE_RAM_DAMAGE - BASE_RAM_DAMAGE) / (HIGH_BASE_RAM_DAMAGE_VELOCITY - BASE_RAM_DAMAGE_VELOCITY)

	velocityLength = CalcVelocityDiffLength(target, source)
	if velocityLength < MIN_BASE_RAM_DAMAGE_VELOCITY: return 0

	baseDamage = GRADIENT * (velocityLength - BASE_RAM_DAMAGE_VELOCITY) + BASE_RAM_DAMAGE

	cappedBaseDamage = max(MIN_BASE_RAM_DAMAGE, min(MAX_BASE_RAM_DAMAGE, baseDamage))

	return CalcBoostedDamageFromScale(source, cappedBaseDamage) * CalcRamDamageNerfFactor(target)

def CalcVelocityDiffLength(target, source):
	# Velocities are not the ramming velocities, but the bounce away velocities.
	# The bigger the ramming, the bigger the bounce away velocities.
	#
	# The reason we use the velocity diff between the two ships is because when the mass of the
	# rammer is small and the target big, the force on the collision event always is 0.
	# This would result in 0 damage being done to large ships.
	velocityDiff = Custom.CrazyShipAbilities.Utils.CloneVector(source.GetVelocityTG())
	velocityDiff.Subtract(target.GetVelocityTG())
	return velocityDiff.Length()

def CalcRamDamageNerfFactor(target):
	# With the formula: nerfFactor = 1.0 / (math.log(target.GetMass()) / math.log(2) / 11)
	# - large bases and borg cubes are around 0.5
	# - warbird and lighter bases like ds9 are 0.7
	# - galaxy is 0.89
	# - sovereign, keldon, and most ships are a little over 1.0 but this is capped
	nerfFactor = 1.0 / (math.log(target.GetMass()) / math.log(2) / 11)
	return min(1.0, nerfFactor)

def CalcBoostedDamageFromScale(source, damage):
	return damage + damage * (source.GetScale() - 1) * DAMAGE_BOOST_FROM_SCALE

def HealAndBuffFromDamageDealt(damageDealt):
	if damageDealt == 0: return

	healing = CalcHealingBoost(damageDealt)
	scale = CalcScaleBoost(damageDealt)
	Buffs.insert(0, (healing, scale))

	ChangePlayerScale(scale)
	Custom.CrazyShipAbilities.Utils.ChangePlayerRepairPointsBy(healing)

	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_STOP_BUFF, BUFF_DURATION_S)

def CalcScaleBoost(damageDealt):
	GRADIENT = (MAX_SCALE_BOOST - MIN_SCALE_BOOST) / (MAX_BASE_RAM_DAMAGE - MIN_BASE_RAM_DAMAGE)
	baseScaleBoost =  GRADIENT * (damageDealt - MIN_BASE_RAM_DAMAGE) + MIN_SCALE_BOOST
	return max(MIN_SCALE_BOOST, min(MAX_SCALE_BOOST, baseScaleBoost))

def CalcHealingBoost(damageDealt):
	REPAIR_TICKS_PER_SECOND = 3
	N_REPAIR_TICKS = BUFF_DURATION_S * REPAIR_TICKS_PER_SECOND

	totalHealing = damageDealt * HEALING_FROM_DAMAGE_FACTOR
	return totalHealing / N_REPAIR_TICKS

def BuffFinished(_pObject, _pEvent):
	if not App.Game_GetCurrentPlayer(): return
	if len(Buffs) == 0: return

	healing, scale = Buffs.pop()
	Custom.CrazyShipAbilities.Utils.ChangePlayerRepairPointsBy(-healing)
	ChangePlayerScale(-scale)

def IsPlayerRammer():
	return 'BugRammer' == Custom.CrazyShipAbilities.Utils.GetPlayerShipType()

def IsRammer(ship):
	return 'BugRammer' == Custom.CrazyShipAbilities.Utils.GetShipType(ship)

def ChangePlayerScale(amount):
	player = App.Game_GetCurrentPlayer()
	player.SetScale(player.GetScale() + amount)