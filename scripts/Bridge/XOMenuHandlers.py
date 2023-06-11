# File: X (Python 1.5)

import App
import BridgeUtils
import loadspacehelper

def CreateMenus():
	pTopWindow = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())
	pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
	pXOMenu = App.STTopLevelMenu_CreateW(pDatabase.GetString('Commander'))
	pXOPane = App.STStylizedWindow_CreateW('StylizedWindow', 'NoMinimize', pDatabase.GetString('Commander'), 0.0, 0.0)
	pXOPane.AddChild(pXOMenu, 0.0, 0.0, 0)
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, 'Bridge.BridgeMenus.ButtonClicked')
	import BridgeMenus
	pCommunicate = BridgeMenus.CreateCommunicateButton('XO', pXOMenu)
	pXOMenu.AddChild(pCommunicate, 0.0, 0.0, 0)
	pReport = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Damage Report'), App.ET_REPORT, 0, pXOMenu)
	pXOMenu.AddChild(pReport, 0.0, 0.0, 0)
	pXOMenu.AddChild(BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Green Alert'), App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_GREEN, pXOMenu), 0.0, 0.0, 0)
	pXOMenu.AddChild(BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Yellow Alert'), App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_YELLOW, pXOMenu), 0.0, 0.0, 0)
	pXOMenu.AddChild(BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Red Alert'), App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_RED, pXOMenu), 0.0, 0.0, 0)
	pObjectives = App.STCharacterMenu_CreateW(pDatabase.GetString('Objectives'))
	pXOMenu.AddChild(pObjectives, 0.0, 0.0, 0)
	pShowLog = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Show Mission Log'), App.ET_SHOW_MISSION_LOG, 0, pXOMenu)
	pXOMenu.AddChild(pShowLog, 0.0, 0.0, 0)
	pContactStarfleet = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Contact Starfleet'), App.ET_CONTACT_STARFLEET, 0, pXOMenu)
	pXOMenu.AddChild(pContactStarfleet, 0.0, 0.0, 0)
	pContactEngineering = BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString('Contact Engineering'), App.ET_CONTACT_ENGINEERING, 0, pXOMenu)
	pXOMenu.AddChild(pContactEngineering, 0.0, 0.0, 0)
	pContactEngineering.SetDisabled()
	if App.g_kUtopiaModule.IsMultiplayer():
		pReport.SetDisabled()
		pCommunicate.SetDisabled()
		pObjectives.SetDisabled()
		pShowLog.SetDisabled()
		pContactStarfleet.SetDisabled()
		pContactEngineering.SetDisabled()
	
	App.g_kLocalizationManager.Unload(pDatabase)
	pXOPane.SetNotVisible()
	pXOMenu.SetNotVisible()
	pXOMenu.SetNoSkipParent()
	pTacticalControlWindow.AddChild(pXOPane, 0.0, 0.0, 0)
	pTacticalControlWindow.AddMenuToList(pXOMenu)
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + '.SetAlertLevel')
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_OBJECTIVES, __name__ + '.Objectives')
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_CONTACT_ENGINEERING, 'Bridge.EngineerCharacterHandlers.ContactEngineering')
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_COMMUNICATE, 'Bridge.Characters.CommonAnimations.NothingToAdd')
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_SHOW_MISSION_LOG, __name__ + '.ShowLog')
	return pXOMenu

def GenChildShipName(prefix, i, pPlayer):
	return prefix + ' ' + str(i + 1) + ' (' + pPlayer.GetName() + ')'

DRONE_PREFIX = "Drone"
BEEFY_DRONE_PREFIX = "BeefyDrone"
DUD_DRONE_PREFIX = "DudDrone"
MAX_DRONES_IN_PERIOD = 2
PERIOD_S = 6
SPAWN_DISTANCE = 50
POSSIBLE_SHIPS = [
	"Rectangle",
	"Asteroid",
	"Nova",
	"Sabre",
	"Fighter",
	"Transport",
	"BugRammer"
]

DEFIANT_BOOST_COOLDOWN_S = 10
SCIMITAR_BOOST_COOLDOWN_S = 15
AKIRA_BOOST_COOLDOWN_S = 10

BUG_DRONE_COOLDOWN_S = 12
BUG_DRONE_HP = 50
BUG_DRONE_NAME_PREFIX = 'Ram'
EACH_N_DRONE_IS_BEEFY = 8
BUG_BEEFY_DRONE_NAME_PREFIX = 'BeefyRam'
BUG_BEEFY_DRONE_SCALE = 1.5
BUG_BEEFY_DRONE_SPEED_MULT = 0.5

VALDORE_WALL_COOLDOWN_S = 8
VALDORE_MAX_SIMULTANEOUS_WALLS = 1
WALL_LIFETIME_S = VALDORE_WALL_COOLDOWN_S * VALDORE_MAX_SIMULTANEOUS_WALLS - 1 # TODO this only applies when spawning a new wall

MAX_NUKES_PER_PERIOD = 3
SHUTTLE_NUKE_COOLDOWN_PERIOD = 24
NUKE_PREFIX = '42km Nuke'

def Reset():
	global DroneNames, LastSpawnDroneTime, DroneSpawnTimes, enemyGroup, LastBoostTime, WallNamesAndSpawnTimes, RammerNames, NukeNamesAndSpawnTimes
	DroneNames = []
	LastSpawnDroneTime = 0
	DroneSpawnTimes = []
	enemyGroup = None
	LastBoostTime = 0
	WallNamesAndSpawnTimes = []
	RammerNames = []
	NukeNamesAndSpawnTimes = []

Reset()

def SetAlertLevel(pObject, pEvent):
	iType = pEvent.GetInt()
	pGame = App.Game_GetCurrentGame()
	pPlayer = App.ShipClass_Cast(pGame.GetPlayer())
	if App.IsNull(pPlayer):
		pObject.CallNextHandler(pEvent)
		return None
	
	iLevel = 0
	if iType == App.CharacterClass.EST_ALERT_GREEN:
		iLevel = pPlayer.GREEN_ALERT
	
	if iType == App.CharacterClass.EST_ALERT_YELLOW:
		iLevel = pPlayer.YELLOW_ALERT
	
	if iType == App.CharacterClass.EST_ALERT_RED:
		# AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
		import MissionLib
		global LastBoostTime
		global NDrones
		
		if pPlayer.GetShipProperty().GetName().GetCString() == 'Defiant':
			if LastBoostTime + DEFIANT_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				velocity = pPlayer.GetVelocityTG()
				velocity.Scale(10) 
				pPlayer.SetVelocity(velocity)
				LastBoostTime = App.g_kUtopiaModule.GetGameTime()

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Scimitar':
			if LastBoostTime + SCIMITAR_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				velocity = pPlayer.GetVelocityTG()
				velocity.Scale(20) 
				pPlayer.SetVelocity(velocity)
				LastBoostTime = App.g_kUtopiaModule.GetGameTime()

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Akira':
			if LastBoostTime + AKIRA_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				velocity = pPlayer.GetVelocityTG()
				velocity.Scale(40)
				pPlayer.SetVelocity(velocity)
				LastBoostTime = App.g_kUtopiaModule.GetGameTime()

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Valdore':
			global WallNamesAndSpawnTimes
			if LastBoostTime + VALDORE_WALL_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				LastBoostTime = App.g_kUtopiaModule.GetGameTime()
				# Not actually boost
				
				target = pPlayer.GetTarget()
				if target:
					global WallNamesAndSpawnTimes, WALL_LIFETIME_S

					for (wallName, spawnTime) in WallNamesAndSpawnTimes:
						if spawnTime + WALL_LIFETIME_S > App.g_kUtopiaModule.GetGameTime():
							continue
					
						wall = MissionLib.GetShip(wallName)
						if not wall:
							continue

						wall.SetScale(0.001)
						wall.SetInvincible(0)
						
						pSystem = wall.GetHull()
						pSystem.SetConditionPercentage(0)

					shipName = GenChildShipName('Wall', len(WallNamesAndSpawnTimes), pPlayer)
					
					pShip = SpawnDroneShip('Wall', shipName, distance=0.0, pPlayer=pPlayer, group = MissionLib.GetMission().GetNeutralGroup())
					pShip.SetScale(25)
					pShip.SetInvincible(1)
					pShip.SetCollisionsOn(0)

					direction = target.GetWorldLocation()
					direction.Subtract(pPlayer.GetWorldLocation())
					direction.Scale(0.75)
					
					betweenPoint = App.TGPoint3()
					betweenPoint.Set(pPlayer.GetWorldLocation())
					betweenPoint.Add(direction)

					pShip.SetTranslate(betweenPoint)

					perpendicular = GetAnyPerpendicularVector(direction, pPlayer)
					pShip.AlignToVectors(Unitized(direction), Unitized(perpendicular))

					WallNamesAndSpawnTimes.append((shipName, App.g_kUtopiaModule.GetGameTime()))

		if pPlayer.GetShipProperty().GetName().GetCString() == 'BugRammer':
			global RammerNames
			target = GetCurrentTarget(pPlayer)
			targetName = target and target.GetName() or None

			if LastBoostTime + BUG_DRONE_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				velocity = pPlayer.GetVelocityTG()
				velocity.Scale(1.6)
				pPlayer.SetVelocity(velocity)
			
				LastBoostTime = App.g_kUtopiaModule.GetGameTime()
				
				if targetName:
					isBeefyDrone = len(RammerNames) % EACH_N_DRONE_IS_BEEFY == EACH_N_DRONE_IS_BEEFY - 1

					newShipNamePrefix = isBeefyDrone and BUG_BEEFY_DRONE_NAME_PREFIX or BUG_DRONE_NAME_PREFIX
					newShipName = GenChildShipName(newShipNamePrefix, len(RammerNames), pPlayer)

					SetEnemyGroup(pPlayer)
					pNewShip = SpawnDroneShip('BugRammer', newShipName, 30, pPlayer, group = MissionLib.GetMission().GetNeutralGroup())

					if isBeefyDrone:
						pNewShip.SetScale(BUG_BEEFY_DRONE_SCALE)
						pNewShip.SetMass(2000)
						# Scaling the ship also scales up the speed for some reason
						pNewShip.GetImpulseEngineSubsystem().SetPowerPercentageWanted(1.0 / BUG_BEEFY_DRONE_SCALE * BUG_BEEFY_DRONE_SPEED_MULT)
					else:
						pNewShip.SetMass(100)
						pNewShip.SetScale(0.8)
						pNewShip.DamageSystem(pNewShip.GetHull(), pNewShip.GetHull().GetMaxCondition() - BUG_DRONE_HP)
						pNewShip.GetHull().GetProperty().SetMaxCondition(BUG_DRONE_HP)
					
					pNewShip.EnableCollisionsWith(pPlayer, 0)

					for shipName in RammerNames:
						pExistingShip = MissionLib.GetShip(shipName)
						if not pExistingShip:
							continue
						pNewShip.EnableCollisionsWith(pExistingShip, 0)

					RammerNames.append(newShipName)

			for shipName in RammerNames:
				pShip = MissionLib.GetShip(shipName)
				if not pShip:
					continue
				if not target:
					pShip.SetAI(None)

				SetShipKamazakeAI(pShip, targetName)

				AlignShipToFaceTarget(pShip, target)

				vZero = App.TGPoint3()
				vZero.SetXYZ(0.0, 0.0, 0.0)
				pShip.SetVelocity(target.GetVelocityTG())
				pShip.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Shuttle':
			if CanLaunchNextNuke():
				global NNukes
				shipName = GenChildShipName(NUKE_PREFIX, len(NukeNamesAndSpawnTimes), pPlayer)
				NukeNamesAndSpawnTimes.append((shipName, App.g_kUtopiaModule.GetGameTime()))

				nuke = SpawnDroneShip('Probe', shipName, 0, pPlayer, group = MissionLib.GetMission().GetNeutralGroup())
				nuke.EnableCollisionsWith(pPlayer, 0)
				nuke.SetScale(160)

				# Allow the ship to drift
				nuke.GetImpulseEngineSubsystem().SetPowerPercentageWanted(0)
				nuke.GetShields().SetPowerPercentageWanted(0)

				originalPlayerVelocity = pPlayer.GetVelocityTG()

				nukeVelocity = Unitized(pPlayer.GetWorldForwardTG())
				nukeVelocity.Scale(8000.0 / 600) # scale 1 == 600kph

				playerVelocityKnockback = Unitized(nukeVelocity)
				playerVelocityKnockback.Scale(-150)

				newPlayerVelocity = CloneVector(playerVelocityKnockback)
				newPlayerVelocity.Add(originalPlayerVelocity)
				pPlayer.SetVelocity(newPlayerVelocity)

				nuke.SetVelocity(nukeVelocity)
				nuke.AlignToVectors(pPlayer.GetWorldForwardTG(), pPlayer.GetWorldUpTG())

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Nova':
			global LastSpawnDroneTime, DroneSpawnTimes, MAX_DRONES_IN_PERIOD, PERIOD_S, DroneNames

			for i in range(0, len(DroneSpawnTimes)):
				if DroneSpawnTimes[0] + PERIOD_S < App.g_kUtopiaModule.GetGameTime():
					del DroneSpawnTimes[0]

			# if time.clock() - LastSpawnDroneTime > 2:
			NDronesSpawned = 0
			while len(DroneSpawnTimes) < MAX_DRONES_IN_PERIOD :
				DroneSpawnTimes.append(App.g_kUtopiaModule.GetGameTime())
				NDronesSpawned = NDronesSpawned + 1

				randomShipNum = App.g_kSystemWrapper.GetRandomNumber(100)
				shipNamePrefix = DRONE_PREFIX
				if randomShipNum < 2:
					shipType = "Rectangle"
					shipNamePrefix = BEEFY_DRONE_PREFIX
				elif randomShipNum < 9:
					shipType = "Asteroid"
					shipNamePrefix = DUD_DRONE_PREFIX
				elif randomShipNum < 15:
					shipType = "Nova"
				elif randomShipNum < 18:
					shipType = "Sabre"
					shipNamePrefix = BEEFY_DRONE_PREFIX
				elif randomShipNum < 47:
					shipType = "Fighter"
				else:
					shipType = "Transport"

				shipName = GenChildShipName(shipNamePrefix, len(DroneNames), pPlayer)
				DroneNames.append(shipName)

				if shipType == 'Transport':
					distance = SPAWN_DISTANCE
				else:
					distance = SPAWN_DISTANCE * 2

				SetEnemyGroup(pPlayer)
				pShip = SpawnDroneShip(shipType, shipName, distance, pPlayer, group = MissionLib.GetMission().GetFriendlyGroup())
				SetVelocityAndDirectionAsPlayer(pShip, pPlayer)

				dynamicGroup = App.ObjectGroup_FromModule("Bridge.XOMenuHandlers", "enemyGroup")
				import QuickBattle.QuickBattleFriendlyAI
				try:
					pAI = QuickBattle.QuickBattleFriendlyAI.CreateDroneAI(pShip, groupToAttack = dynamicGroup)
					pShip.SetAI(pAI)
				except:
					print('Failed to create AI. Probably because there isnt any enemy ships yet or something')

			if NDronesSpawned > 0:
				velocity = pPlayer.GetVelocityTG()
				velocity.Scale(18)
				pPlayer.SetVelocity(velocity)

		iLevel = pPlayer.RED_ALERT
	
	if iLevel != pPlayer.GetAlertLevel():
		if iType == App.CharacterClass.EST_ALERT_GREEN:
			App.TGSoundAction_Create('GreenAlertSound').Play()
		
		if iType == App.CharacterClass.EST_ALERT_YELLOW:
			App.TGSoundAction_Create('YellowAlertSound').Play()
		
		if iType == App.CharacterClass.EST_ALERT_RED:
			App.TGSoundAction_Create('RedAlertSound').Play()
		
		pAlertEvent = App.TGIntEvent_Create()
		pAlertEvent.SetSource(pObject)
		pAlertEvent.SetDestination(pPlayer)
		pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
		pAlertEvent.SetInt(iLevel)
		App.g_kEventManager.AddEvent(pAlertEvent)
	
	pObject.CallNextHandler(pEvent)

def Objectives(pObject, pEvent):
	pObject.CallNextHandler(pEvent)


def SetContactEngineeringEnabled(bEnabled):
	pBridge = App.g_kSetManager.GetSet('bridge')
	pXO = App.CharacterClass_GetObject(pBridge, 'XO')
	pMenu = pXO.GetMenu()
	pDatabase = App.g_kLocalizationManager.Load('data/TGL/Bridge Menus.tgl')
	pButton = pMenu.GetButtonW(pDatabase.GetString('Contact Engineering'))
	if pButton:
		if bEnabled:
			pButton.SetEnabled()
		else:
			pButton.SetDisabled()
	
	App.g_kLocalizationManager.Unload(pDatabase)


def ShowLog(pObject, pEvent):
	pLog = App.STMissionLog_GetMissionLog()
	pTopWindow = App.TopWindow_GetTopWindow()
	App.g_kUtopiaModule.Pause(1)
	pWindow = App.STStylizedWindow_Cast(pLog.GetFirstChild())
	if pWindow != None:
		pWindow.ScrollToBottom()
	
	pTopWindow.MoveToFront(pLog)
	pLog.SetVisible()
	pTopWindow.SetFocus(pLog)
	pObject.CallNextHandler(pEvent)


def SpawnDroneShip(shipType, shipName, distance, pPlayer, group): # AAAAAAAAAAAA
	import MissionLib
	pSetName = MissionLib.GetPlayerSet().GetName()
	pSet = App.g_kSetManager.GetSet(pSetName)

	pShip = loadspacehelper.CreateShip(shipType, pSet, shipName, None, 0, 1)

	kPoint = App.TGPoint3()
	kPoint.Set(pPlayer.GetWorldLocation())
	import math
	rads = (App.g_kSystemWrapper.GetRandomNumber(201) - 100) / 100.0 * 6.28
	
	XOff = distance * math.sin(rads)
	YOff = distance * math.cos(rads)
	kPoint.SetX(kPoint.GetX() + XOff)
	kPoint.SetY(kPoint.GetY() + YOff)
	kPoint.SetZ(kPoint.GetZ() + (App.g_kSystemWrapper.GetRandomNumber(201) - 100) / 100.0 * distance)
	pShip.SetTranslate(kPoint)

	group.AddName(shipName)
	
	return pShip

def SetVelocityAndDirectionAsPlayer(pShip, pPlayer):
	up = pPlayer.GetWorldUpTG()
	forward = pPlayer.GetWorldForwardTG()
	pShip.AlignToVectors(forward, up)

	pShip.SetVelocity(pPlayer.GetVelocityTG())

def SetEnemyGroup(pPlayer): # AAAAAAAAAAAAAA
	global enemyGroup
	
	if not enemyGroup:
		enemyGroup = App.ObjectGroup()
	enemyGroup.RemoveAllNames()
	target = GetCurrentTarget(pPlayer)
	if target:
		enemyGroup.AddName(target.GetName())

def GetCurrentTarget(pPlayer): # AAAAAAAAAAAA
	target = pPlayer.GetTarget()
	if target:
		castedTarget = App.ShipClass_Cast(target)
		if castedTarget:
			return castedTarget

	return None

def GetAnyPerpendicularVector(direction, anyShip):
	up = Unitized(anyShip.GetWorldUpTG())
	perp = Unitized(direction).UnitCross(up)

	if perp.Length() > 0.5: 
		return perp

	# direction must be equal to up, as cross product will return invalid result (0,0,0)
	forward = Unitized(anyShip.GetWorldForwardTG())
	return Unitized(direction).UnitCross(forward)

def AlignShipToFaceTarget(pShip, target):
	direction = target.GetWorldLocation()
	direction.Subtract(pShip.GetWorldLocation())
	perpendicular = GetAnyPerpendicularVector(direction, target)
	pShip.AlignToVectors(direction, perpendicular)

def Unitized(vector):
	unitVector = CloneVector(vector)
	unitVector.Unitize()
	return unitVector

def CloneVector(vector):
	copy = App.TGPoint3()
	copy.Set(vector)
	return copy

def SetShipKamazakeAI(pShip, targetName):
	pKamakaze = App.PlainAI_Create(pShip, 'MoveIn')
	pKamakaze.SetScriptModule('Ram')
	pKamakaze.SetInterruptable(1)
	pScript = pKamakaze.GetScriptInstance()
	pScript.SetTargetObjectName(targetName)
	pShip.SetAI(pKamakaze)

def CanLaunchNextNuke():
	now = App.g_kUtopiaModule.GetGameTime()
	nNukesLaunchedInPeriod = 0

	for (NukeName, NukeSpawnTime) in NukeNamesAndSpawnTimes:
		if NukeSpawnTime + SHUTTLE_NUKE_COOLDOWN_PERIOD >= now:
			nNukesLaunchedInPeriod = nNukesLaunchedInPeriod + 1

	return nNukesLaunchedInPeriod < MAX_NUKES_PER_PERIOD