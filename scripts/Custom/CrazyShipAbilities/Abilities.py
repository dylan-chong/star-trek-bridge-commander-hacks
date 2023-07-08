import App

import Custom.CrazyShipAbilities.PerShip.NoAbilities

SHIPS_WITH_ABILITIES = [
	'Akira',
	'BugRammer',
	'Defiant',
	'Nova',
	'Prometheus',
	'Scimitar',
	'Shuttle',
	'Valdore'
]

def Reset():
	for ship in SHIPS_WITH_ABILITIES:
		ModuleForShipName(ship).Reset()

def IsAvailable():
	return GetShipAbilityModule() != Custom.CrazyShipAbilities.PerShip.NoAbilities

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
		return Custom.CrazyShipAbilities.PerShip.NoAbilities

	playerShipName = pPlayer.GetShipProperty().GetName().GetCString()

	if playerShipName not in SHIPS_WITH_ABILITIES:
		return Custom.CrazyShipAbilities.PerShip.NoAbilities

	return ModuleForShipName(playerShipName)

def ModuleForShipName(shipName):
	return __import__('Custom.CrazyShipAbilities.PerShip.' + shipName)