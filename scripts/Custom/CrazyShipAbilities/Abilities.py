import App
import loadspacehelper

import Custom.CrazyShipAbilities.PerShip.NoAbilities
import Custom.CrazyShipAbilities.PerShip.Prometheus
import Custom.CrazyShipAbilities.PerShip.Defiant

SHIP_TO_ABILITY_MODULES = {
	'Akira': Custom.CrazyShipAbilities.PerShip.Akira,
	'BugRammer': Custom.CrazyShipAbilities.PerShip.BugRammer,
	'Defiant': Custom.CrazyShipAbilities.PerShip.Defiant,
	'Nova': Custom.CrazyShipAbilities.PerShip.Nova,
	'Prometheus': Custom.CrazyShipAbilities.PerShip.Prometheus,
	'Scimitar': Custom.CrazyShipAbilities.PerShip.Scimitar,
	'Shuttle': Custom.CrazyShipAbilities.PerShip.Shuttle,
	'Valdore': Custom.CrazyShipAbilities.PerShip.Valdore,
}

def Reset():
	LastBoostTime = -999999999

	for mod in SHIP_TO_ABILITY_MODULES.values():
		mod.Reset()

Reset()

def GetRemainingCooldown():
	return GetShipAbilityModule().GetRemainingCooldown()

def GetTitle():
	return GetShipAbilityModule().GetTitle()

def UseAbility():
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	return GetShipAbilityModule().UseAbility(pPlayer)

def GetShipAbilityModule():
	pGame = App.Game_GetCurrentGame()
	pPlayer = App.ShipClass_Cast(pGame.GetPlayer())
	playerShipName = pPlayer.GetShipProperty().GetName().GetCString()

	mod = SHIP_TO_ABILITY_MODULES[playerShipName]
	if not mod:
		return Custom.CrazyShipAbilities.NoAbilities

	return mod
