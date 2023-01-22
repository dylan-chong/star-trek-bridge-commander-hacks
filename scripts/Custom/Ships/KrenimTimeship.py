#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "KrenimTimeship"
iconName = "KrenimTimeship"
longName = "Krenim Timeship"
shipFile = "KrenimTimeship"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.KrenimTimeship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.KrenimTimeship.desc = "No information available."


if menuGroup:           Foundation.ShipDef.KrenimTimeship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.KrenimTimeship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
