import App

import Custom.CrazyShipAbilities.PerShip.NoAbilities

import Custom.CrazyShipAbilities.PerShip.Akira
import Custom.CrazyShipAbilities.PerShip.BugRammer
import Custom.CrazyShipAbilities.PerShip.Defiant
import Custom.CrazyShipAbilities.PerShip.Nova
import Custom.CrazyShipAbilities.PerShip.Prometheus
import Custom.CrazyShipAbilities.PerShip.Scimitar
import Custom.CrazyShipAbilities.PerShip.Shuttle
import Custom.CrazyShipAbilities.PerShip.Valdore

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
	pPlayer = pGame.GetPlayer()
	if not pPlayer:
		return Custom.CrazyShipAbilities.PerShip.NoAbilities

	playerShipName = pPlayer.GetShipProperty().GetName().GetCString()

	mod = SHIP_TO_ABILITY_MODULES.get(playerShipName)
	return mod or Custom.CrazyShipAbilities.PerShip.NoAbilities
