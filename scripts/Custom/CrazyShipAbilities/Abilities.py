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
NO_ABILITIES_MODULE = Custom.CrazyShipAbilities.PerShip.NoAbilities

def Reset():
	for mod in SHIP_TO_ABILITY_MODULES.values():
		mod.Reset()

Reset()

def IsAvailable():
	return GetShipAbilityModule() != NO_ABILITIES_MODULE

def GetTitle():
	return GetShipAbilityModule().GetTitle()

def GetCooldownS():
	"""
	Returns the number of seconds until the ability is ready.
	If the cooldown is compound, then this is the time until the next is ready.
	"""
	return GetShipAbilityModule().GetCooldownS()

def GetNReady():
	"""
	Returns the number of available ability triggers.
	1 for simple cooldown, multiple for a compound.
	"""
	return GetShipAbilityModule().GetNReady()

def GetNCooldowns():
	return GetShipAbilityModule().GetNCooldowns()

def UseAbility():
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	return GetShipAbilityModule().UseAbility(pPlayer)

def GetShipAbilityModule():
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	if not pPlayer:
		return NO_ABILITIES_MODULE

	playerShipName = pPlayer.GetShipProperty().GetName().GetCString()
	return SHIP_TO_ABILITY_MODULES.get(playerShipName, NO_ABILITIES_MODULE)
