#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "BugRammer"
iconName = "Bug"
longName = "BugRammer"
shipFile = "BugRammer"
species = App.SPECIES_GALAXY
menuGroup = "Dominion Ships"
playerMenuGroup = "Dominion Ships"
Foundation.ShipDef.BugRammer = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.BugRammer.desc = "No information available."


# if menuGroup:           Foundation.ShipDef.BugRammer.RegisterQBShipMenu(menuGroup)
# if playerMenuGroup:     Foundation.ShipDef.BugRammer.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
