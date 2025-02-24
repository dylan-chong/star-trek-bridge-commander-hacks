import App
import MissionLib
import Custom.CrazyShipAbilities.Cooldowns
import Custom.CrazyShipAbilities.Utils

DASH_COOLDOWN_S = 0

ET_RECHARGE_CANNONS = App.UtopiaModule_GetNextEventType()
ET_RESET_FIRE_ALL_CANNONS = App.UtopiaModule_GetNextEventType()

def Initialize(OverrideExisting):
	global Cooldown
	if 'Cooldown' in globals().keys() and not OverrideExisting:
		return
	Cooldown = Custom.CrazyShipAbilities.Cooldowns.SimpleCooldown(DASH_COOLDOWN_S)

	Custom.CrazyShipAbilities.Utils.ReregisterEventHanders([
		(ET_RECHARGE_CANNONS, 'RechargePlayerCannons'),
		(ET_RESET_FIRE_ALL_CANNONS, 'ResetFireAllCannons'),
	], App.Game_GetCurrentGame(), __name__)

def GetTitle():
	return 'Charge'

def GetCooldownS():
	return Cooldown.GetCooldownS()

def GetNReady():
	return Cooldown.GetNReady()

def GetNCooldowns():
	return Cooldown.GetNCooldowns()

def UseAbility(pPlayer):
	if not Cooldown.IsReady():
		return

	Cooldown.Trigger()

	# velocity = pPlayer.GetVelocityTG()
	# velocity.Scale(20)
	# pPlayer.SetVelocity(velocity)

	# SetFireAllCannons(App.Game_GetCurrentPlayer(), GetEnemies(), 1)

	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_RESET_FIRE_ALL_CANNONS, 0.0)
	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_RECHARGE_CANNONS, 0.5)
	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_RESET_FIRE_ALL_CANNONS, 1.0)
	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_RECHARGE_CANNONS, 1.5)
	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_RESET_FIRE_ALL_CANNONS, 2.0)
	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_RECHARGE_CANNONS, 2.5)
	Custom.CrazyShipAbilities.Utils.EmitEventAfterDelay(ET_RESET_FIRE_ALL_CANNONS, 3.0)

def SetFireAllCannons(pShip, lTargets, shouldFire):
	pMatch = pShip.StartGetSubsystemMatch(App.CT_WEAPON_SYSTEM)
	pSystem = pShip.GetNextSubsystemMatch(pMatch)

	while pSystem != None:
		pWeapSystem = App.WeaponSystem_Cast(pSystem)
		weapProperty = pWeapSystem.GetProperty()

		isCannon = weapProperty.GetWeaponSystemType() == App.WeaponSystemProperty.WST_PULSE
		if isCannon:
			for pTarget in lTargets:
				if not pWeapSystem.IsInTargetList(pTarget) and shouldFire:
					weapProperty.SetSingleFire(0)
					pWeapSystem.StartFiring(pTarget)

				if not shouldFire:
					weapProperty.SetSingleFire(1)
					pWeapSystem.StopFiring()

		pSystem = pShip.GetNextSubsystemMatch(pMatch)

	pShip.EndGetSubsystemMatch(pMatch)

def ResetFireAllCannons(_pObject, _pEvent):
	SetFireAllCannons(App.Game_GetCurrentPlayer(), GetEnemies(), 0)
	RechargeCannons(App.Game_GetCurrentPlayer())

def RechargePlayerCannons(_pObject, _pEvent):
	SetFireAllCannons(App.Game_GetCurrentPlayer(), GetEnemies(), 1)

def RechargeCannons(pShip):
	pPulseSys = pShip.GetPulseWeaponSystem()
	if not pPulseSys:
		return
	for iPulseNum in range(pPulseSys.GetNumChildSubsystems()):
		pPulseWeapon = App.EnergyWeapon_Cast(pPulseSys.GetChildSubsystem(iPulseNum))
		pPulseWeapon.SetChargeLevel(pPulseWeapon.GetMaxCharge())

def GetEnemies():
	pGame = App.Game_GetCurrentGame()
	pSet = pGame.GetPlayerSet()
	enemies = MissionLib.GetEnemyGroup()
	return GetShipsInSet(enemies, pSet)

def GetShipsInSet(pGroup, pSet = None):
	# If pSet is not given, get player set
	if pSet == None:
		pGame = App.Game_GetCurrentGame()
		pSet = pGame.GetPlayerSet()

	ships = []
	pObject = pSet.GetFirstObject()
	pFirstObject = pObject
	while not (App.IsNull(pObject)):
		name = pObject.GetName()
		if pGroup.IsNameInGroup(name):
			ship = MissionLib.GetShip(name)
			ships.append(ship)

		pObject = pSet.GetNextObject(pObject.GetObjID())

		if (pObject.GetObjID() == pFirstObject.GetObjID()):
			# Exit loop
			pObject = None

	return ships
