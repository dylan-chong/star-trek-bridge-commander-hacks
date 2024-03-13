import App

import Custom.CrazyShipAbilities.PerShip.NoAbilities
import Custom.CrazyShipAbilities.Utils

SHIPS_WITH_ABILITIES = [
	'Akira',
	'BugRammer',
	'Defiant',
	'Founder',
	'KrenimOrbship',
	'Nova',
	'Prometheus',
	'Scimitar',
	'Shuttle',
	'Valdore'
]

def Reset():
	for ship in SHIPS_WITH_ABILITIES:
		ModuleForShipName(ship).Initialize(OverrideExisting=1)

def IsSupported():
	"""Are abilities supported"""
	mod = GetShipAbilityModule()
	if mod == Custom.CrazyShipAbilities.PerShip.NoAbilities:
		return 0

	isSupportedResult = ExecModuleFuncIfExists(mod, 'IsSupported')
	if isSupportedResult == None:
		return 1
	return isSupportedResult

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
	shipType = Custom.CrazyShipAbilities.Utils.GetPlayerShipType()
	if not shipType:
		return Custom.CrazyShipAbilities.PerShip.NoAbilities

	if shipType not in SHIPS_WITH_ABILITIES:
		return Custom.CrazyShipAbilities.PerShip.NoAbilities

	mod = ModuleForShipName(shipType)
	if Initialize:
		# We need this here becuase it appears that serialization of the game in the campaign can
		# delete the global variables that have already been initialized
		mod.Initialize(OverrideExisting=0)
	return mod

def ExecModuleFuncIfExists(mod, funcName, *args):
	if not hasattr(mod, funcName):
		return None
	func = getattr(mod, funcName)

	if len(args) == 0:
		return func()
	if len(args) == 1:
		return func(args[0])
	if len(args) == 2:
		return func(args[0], args[1])

def ModuleForShipName(shipName):
	return __import__('Custom.CrazyShipAbilities.PerShip.' + shipName)
