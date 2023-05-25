# ShipIcons.py
#
# Load Ship Icons for interface.
#
#

import App
import Foundation
import Registry

shipIconNames = {}
shipIconNums = {}
topSpecies = 0

class ShipIconDef:
	def __init__(self, name, dict = { 'x': 128, 'y': 128 }):
		global topSpecies, shipIcons
		self.name = name
		self.__dict__.update(dict)

		if not self.__dict__.has_key('file'):
			self.file = 'Data/Icons/Ships/' + name + '.tga'

		if self.__dict__.has_key('species'):
			if self.species > topSpecies:	topSpecies = self.species
		else:
			self.species = topSpecies + 1
			topSpecies = self.species

		shipIconNames[name] = self
		shipIconNums[self.species] = self

# Function to load LCARS icon group
def LoadShipIcons(ShipIcons = None):

	if ShipIcons is None:
		ShipIcons = App.g_kIconManager.CreateIconGroup("ShipIcons")
		# Add LCARS icon group to IconManager
		App.g_kIconManager.AddIconGroup(ShipIcons)

	# Glass for when no ship is selected
	TextureHandle = ShipIcons.LoadIconTexture('Data/Icons/Bridge/Background/ScreenBlock.tga')
	ShipIcons.SetIconLocation(App.SPECIES_UNKNOWN, TextureHandle, 0, 0, 8, 8)

	ShipIconDef('Sabre', { 'species': 109 } )
	ShipIconDef('Miranda', { 'species': 110 } )
	ShipIconDef('Nova', { 'species': 111 } )
	ShipIconDef('Norway', { 'species': 112 } )
	ShipIconDef('Steamrunner', { 'species': 113 } )
	ShipIconDef('Constellation', { 'species': 114 } )
	ShipIconDef('Centaur', { 'species': 115 } )
	ShipIconDef('Defiant', { 'species': 116 } )
	ShipIconDef('Intrepid', { 'species': 117 } )
	ShipIconDef('Excelsior', { 'species': 118 } )
	ShipIconDef('ExcelsiorR', { 'species': 119 } )
	ShipIconDef('Ambassador', { 'species': App.SPECIES_AMBASSADOR } )
	ShipIconDef('Luna', { 'species': 120 } )
	ShipIconDef('Akira', { 'species': App.SPECIES_AKIRA } )
	ShipIconDef('Nebula', { 'species': App.SPECIES_NEBULA } )
	ShipIconDef('Galaxy', { 'species': App.SPECIES_GALAXY } )
	ShipIconDef('Sovereign', { 'species': App.SPECIES_SOVEREIGN } )
	ShipIconDef('Prometheus', { 'species': 121} )
	ShipIconDef('SovereignR', { 'species': 122 } )
	ShipIconDef('BirdOfPrey', { 'species': App.SPECIES_BIRD_OF_PREY } )
	ShipIconDef('Kvort', { 'species': 403 } )
	ShipIconDef('KTinga', { 'species': 404 } )
	ShipIconDef('Vorcha', { 'species': App.SPECIES_VORCHA } )
	ShipIconDef('Neghvar', { 'species': 405 } )
	ShipIconDef('Talon', { 'species': 302 } )
	ShipIconDef('Falcon', { 'species': 303 } )
	ShipIconDef('Valdore', { 'species': 304 } )
	ShipIconDef('Warbird', { 'species': App.SPECIES_WARBIRD } )
	ShipIconDef('Scimitar', { 'species': 305 } )
	ShipIconDef('Hideki', { 'species': 205 } )
	ShipIconDef('Galor', { 'species': App.SPECIES_GALOR } )
	ShipIconDef('Keldon', { 'species': App.SPECIES_KELDON } )
	ShipIconDef('ObsidianKeldon', { 'species': 206 } )
	ShipIconDef('Hybrid', { 'species': App.SPECIES_CARDHYBRID } )
	ShipIconDef('Bug', { 'species': 801 } )
	ShipIconDef('BugRammer', { 'species': 1001, 'file': 'Data/Icons/Ships/Bug.tga' } )
	ShipIconDef('Breen', { 'species': 802 } )
	ShipIconDef('Vorta', { 'species': 803 } )
	ShipIconDef('Founder', { 'species': 804 } )
	ShipIconDef('Rectangle', { 'species': 901 } )
	ShipIconDef('Diamond', { 'species': 902 } )
	ShipIconDef('Sphere', { 'species': 903 } )
	ShipIconDef('Cube', { 'species': 904 } )
	ShipIconDef('CubeT', { 'species': 905 } )
	ShipIconDef('CubeA', { 'species': 906 } )
	ShipIconDef('Marauder', { 'species': App.SPECIES_MARAUDER } )
	ShipIconDef('KessokLight', { 'species': App.SPECIES_KESSOK_LIGHT } )
	ShipIconDef('KessokHeavy', { 'species': App.SPECIES_KESSOK_HEAVY } )
	ShipIconDef('SonaCruiser', { 'species': 805 } )
	ShipIconDef('SonaBattleship', { 'species': 806 } )
	ShipIconDef('Bioship', { 'species': 750 } )
	ShipIconDef('HirogenHunter', { 'species': 751 } )
	ShipIconDef('HirogenHoloship', { 'species': 752 } )
	ShipIconDef('HirogenVenatic', { 'species': 753 } )
	ShipIconDef('KazonRaider', { 'species': 754 } )
	ShipIconDef('KazonPredator', { 'species': 755 } )
	ShipIconDef('KrenimPatrol', { 'species': 756 } )
	ShipIconDef('KrenimWarship', { 'species': 757 } )
	ShipIconDef('KrenimTimeship', { 'species': 758 } )
	ShipIconDef('MalonFreighter', { 'species': 759 } )
	ShipIconDef('VidiianCruiser', { 'species': 760 } )
	ShipIconDef('FedShuttle', { 'species': App.SPECIES_SHUTTLE } )
	ShipIconDef('Fighter', { 'species': 123 } )
	ShipIconDef('Danube', { 'species': 124 } )
	ShipIconDef('DanubeR', { 'species': 125 } )
	ShipIconDef('DeltaFlyer', { 'species': 126 } )
	ShipIconDef('ArmoredIntrepid', { 'species': 127 } )
	ShipIconDef('NX', { 'species': 128 } )
	ShipIconDef('Constitution', { 'species': 129 } )
	ShipIconDef('ConstitutionR', { 'species': 130 } )
	ShipIconDef('Freighter', { 'species': App.SPECIES_FREIGHTER } )
	ShipIconDef('Transport', { 'species': App.SPECIES_TRANSPORT } )
	ShipIconDef('LifeBoat', { 'species': App.SPECIES_ESCAPEPOD } )
	ShipIconDef('CardFreighter', { 'species': App.SPECIES_CARDFREIGHTER } )
	ShipIconDef('Sunbuster', { 'species': App.SPECIES_SUNBUSTER } )
	ShipIconDef('OrbitalWeaponsPlatform', { 'species': 207 } )
	ShipIconDef('KessokMine', { 'species': App.SPECIES_KESSOKMINE } )
	ShipIconDef('FedOutpost', { 'species': App.SPECIES_FED_OUTPOST } )
	ShipIconDef('SpaceFacility', { 'species': App.SPECIES_SPACE_FACILITY } )
	ShipIconDef('FedComplex', { 'species': 761 } )
	ShipIconDef('FedStarbase', { 'species': App.SPECIES_FED_STARBASE } )
	ShipIconDef('DS9', { 'species': 762 } )
	ShipIconDef('CardOutpost', { 'species': App.SPECIES_CARD_OUTPOST } )
	ShipIconDef('CardStation', { 'species': App.SPECIES_CARD_STATION } )
	ShipIconDef('CardStarbase', { 'species': App.SPECIES_CARD_STARBASE } )
	ShipIconDef('CommArray', { 'species': App.SPECIES_COMMARRAY } )
	ShipIconDef('CommLight', { 'species': App.SPECIES_COMMLIGHT } )
	ShipIconDef('DryDock', { 'species': App.SPECIES_DRYDOCK } )
	ShipIconDef('Probe', { 'species': App.SPECIES_PROBE } )
	ShipIconDef('ProbeType2', { 'species': App.SPECIES_PROBETYPE2 } )
	ShipIconDef('Asteroid', { 'species': App.SPECIES_ASTEROID } )

	global topSpecies
	topSpecies = topSpecies + 100

	for shipDef in Foundation.shipList._keyList.values():
		if shipIconNames.has_key(shipDef.iconName):
			iconDef = shipIconNames[shipDef.iconName]
		else:
			iconDef = ShipIconDef(shipDef.iconName)
		shipDef.species = iconDef.species

	for i in shipIconNums.values():
		# print i.file, i.species, ' : ',
		TextureHandle = ShipIcons.LoadIconTexture(i.file)
		ShipIcons.SetIconLocation(i.species, TextureHandle, 0, 0, 128, 128)
