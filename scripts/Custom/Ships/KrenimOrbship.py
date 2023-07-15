#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "KrenimOrbship"
iconName = "KrenimWarship"
longName = "Krenim Orbship"
shipFile = "KrenimOrbship"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.KrenimOrbship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.KrenimOrbship.desc = "No information available."


if menuGroup:           Foundation.ShipDef.KrenimOrbship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.KrenimOrbship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
