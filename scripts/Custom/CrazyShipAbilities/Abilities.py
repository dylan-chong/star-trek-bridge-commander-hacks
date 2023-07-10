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
		ModuleForShipName(ship).Initialize(OverrideExisting=1)

def IsAvailable():
	return GetShipAbilityModule() != Custom.CrazyShipAbilities.PerShip.NoAbilities

def GetTitle():
	return GetShipAbilityModule(Initialize=1).GetTitle()

def GetCooldownS():
	"""
	Returns the number of seconds until the ability is ready.
	If the cooldown is compound, then this is the time until the next is ready.
	"""
	return GetShipAbilityModule(Initialize=1).GetCooldownS()

def GetNReady():
	"""
	Returns the number of available ability triggers.
	1 for simple cooldown, multiple for a compound.
	"""
	return GetShipAbilityModule(Initialize=1).GetNReady()

def GetNCooldowns():
	return GetShipAbilityModule(Initialize=1).GetNCooldowns()

def UseAbility():
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	return GetShipAbilityModule(Initialize=1).UseAbility(pPlayer)

def GetShipAbilityModule(Initialize=0):
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	if not pPlayer:
		return Custom.CrazyShipAbilities.PerShip.NoAbilities

	playerShipName = pPlayer.GetShipProperty().GetName().GetCString()

	if playerShipName not in SHIPS_WITH_ABILITIES:
		return Custom.CrazyShipAbilities.PerShip.NoAbilities

	mod = ModuleForShipName(playerShipName)
	if Initialize:
		# We need this here becuase it appears that serialization of the game in the campaign can
		# delete the global variables that have already been initialized
		mod.Initialize(OverrideExisting=0)
	return mod

def ModuleForShipName(shipName):
	return __import__('Custom.CrazyShipAbilities.PerShip.' + shipName)
