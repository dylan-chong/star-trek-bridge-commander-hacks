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
AKIRA_BOOST_COOLDOWN_S = 10
VALDORE_WALL_COOLDOWN_S = 0#15

BUG_BOOST_COOLDOWN_S = 5
BUG_DRONE_HP = 1000 #2000
N_BUG_DRONES_TO_SPAWN = 1

WALL_LIFETIME_S = 4 # TODO this only applies when spawning a new wall

def Reset():
	global NDrones, LastSpawnDroneTime, DroneSpawnTimes, enemyGroup, LastBoostTime, WallSpawnTimes
	NDrones = 0
	LastSpawnDroneTime = 0
	DroneSpawnTimes = []
	enemyGroup = None
	LastBoostTime = 0
	WallSpawnTimes = []

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

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Akira':
			if LastBoostTime + AKIRA_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				velocity = pPlayer.GetVelocityTG()
				velocity.Scale(40)
				pPlayer.SetVelocity(velocity)
				LastBoostTime = App.g_kUtopiaModule.GetGameTime()

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Valdore':
			if LastBoostTime + VALDORE_WALL_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				LastBoostTime = App.g_kUtopiaModule.GetGameTime()
				# Not actually boost
				
				target = pPlayer.GetTarget()
				if target:
					global WallSpawnTimes, WALL_LIFETIME_S

					for (wallName, spawnTime) in WallSpawnTimes:
						if spawnTime + WALL_LIFETIME_S > App.g_kUtopiaModule.GetGameTime():
							continue
					
						wall = MissionLib.GetShip(wallName)
						if not wall:
							continue

						wall.SetScale(0.001)
						
						pSystem = wall.GetHull()
						pSystem.SetConditionPercentage(0)

						# translate = App.TGPoint3()
						# translate.SetXYZ(999999999, 0, 0)
						# pos = wall.GetWorldLocation()
						# pos.Add(translate)
						# wall.SetTranslate(pos)

					shipName = 'Wall ' + str(NDrones)
					NDrones = NDrones + 1
					
					pShip = SpawnDroneShip('Wall', shipName, distance=0.0, pPlayer=pPlayer, group = MissionLib.GetMission().GetNeutralGroup())
					pShip.SetScale(30)

					direction = target.GetWorldLocation()
					direction.Subtract(pPlayer.GetWorldLocation())
					direction.Scale(0.8)
					
					kPoint = App.TGPoint3()
					kPoint.Set(pPlayer.GetWorldLocation())
					kPoint.Add(direction)

					pShip.SetTranslate(kPoint)
		
					directionUnit = App.TGPoint3()
					directionUnit.Set(direction)
					directionUnit.Unitize()

					perpendicular = GetAnyPerpendicularVector(directionUnit, pPlayer)
					pShip.AlignToVectors(directionUnit, perpendicular)

					# pShip.EnableCollisionsWith(pPlayer, 0)

					WallSpawnTimes.append((shipName, App.g_kUtopiaModule.GetGameTime()))

					# TODO distance check (dont spawn wall if too close)

		if pPlayer.GetShipProperty().GetName().GetCString() == 'BugRammer':
			targetName = GetCurrentTargetName(pPlayer)

			if LastBoostTime + BUG_BOOST_COOLDOWN_S < App.g_kUtopiaModule.GetGameTime():
				velocity = pPlayer.GetVelocityTG()
				velocity.Scale(1.6)
				pPlayer.SetVelocity(velocity)
			
				for i in range(0, N_BUG_DRONES_TO_SPAWN):
					LastBoostTime = App.g_kUtopiaModule.GetGameTime()
					
					if not targetName:
						continue

					pTorpSys = pPlayer.GetTorpedoSystem()
					torpType = 0
					if pTorpSys.GetNumAvailableTorpsToType(torpType) == 0:
						continue

					if pTorpSys.GetNumAvailableTorpsToType(torpType) <= 1:
						isBeefyDrone = 1
					else:
						isBeefyDrone = 0

					pTorpSys.LoadAmmoType(torpType, -1)

					global NDrones
					shipName = "Drone " + str(NDrones)
					NDrones = NDrones + 1

					SetEnemyGroup(pPlayer)
					pShip = SpawnDroneShip('BugRammer', shipName, 30, pPlayer, group = MissionLib.GetMission().GetNeutralGroup())
					
					if not isBeefyDrone:
						pShip.SetMass(100)
						pShip.DamageSystem(pShip.GetHull(), pShip.GetHull().GetMaxCondition() - BUG_DRONE_HP)
						pShip.GetHull().GetProperty().SetMaxCondition(BUG_DRONE_HP)

			for i in range(0, NDrones):
				pDrone = MissionLib.GetShip("Drone " + str(i))
				if pDrone and targetName:
					pKamakaze = App.PlainAI_Create(pDrone, 'MoveIn')
					pKamakaze.SetScriptModule('FollowObject')
					pKamakaze.SetInterruptable(1)
					pScript = pKamakaze.GetScriptInstance()
					pScript.SetFollowObjectName(targetName)
					pScript.SetRoughDistances(0.0, 2.0, 4.0)
					pScript.fGoMedSpeed = 0.0
					
					pDrone.SetAI(pKamakaze)
				elif pDrone:
					pDrone.SetAI(None)

		if pPlayer.GetShipProperty().GetName().GetCString() == 'Nova':
			global LastSpawnDroneTime
			global DroneSpawnTimes
			global MAX_DRONES_IN_PERIOD
			global PERIOD_S

			for i in range(0, len(DroneSpawnTimes)):
				if DroneSpawnTimes[0] + PERIOD_S < App.g_kUtopiaModule.GetGameTime():
					del DroneSpawnTimes[0]

			# if time.clock() - LastSpawnDroneTime > 2:
			NDronesSpawned = 0
			while len(DroneSpawnTimes) < MAX_DRONES_IN_PERIOD :
				# LastSpawnDroneTime = time.clock()
				DroneSpawnTimes.append(App.g_kUtopiaModule.GetGameTime())
				NDronesSpawned = NDronesSpawned + 1

				randomShipNum = App.g_kSystemWrapper.GetRandomNumber(100)
				if randomShipNum < 2:
					shipType = "Rectangle"
				elif randomShipNum < 9:
					shipType = "Asteroid"
				elif randomShipNum < 15:
					shipType = "Nova"
				elif randomShipNum < 18:
					shipType = "Sabre"
				elif randomShipNum < 47:
					shipType = "Fighter"
				else:
					shipType = "Transport"

				shipName = "Drone " + str(NDrones) + " (" + shipType + ")" 
				NDrones = NDrones + 1

				if shipType == 'Transport':
					distance = SPAWN_DISTANCE
				else:
					distance = SPAWN_DISTANCE * 2

				SetEnemyGroup(pPlayer)
				pShip = SpawnDroneShip(shipType, shipName, distance, pPlayer, group = MissionLib.GetMission().GetFriendlyGroup())

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
	kPoint.SetX( kPoint.GetX() + XOff )
	kPoint.SetY( kPoint.GetY() + YOff )
	kPoint.SetZ( kPoint.GetZ() + (App.g_kSystemWrapper.GetRandomNumber(201) - 100) / 100.0 * distance)
	pShip.SetTranslate(kPoint)
	
	group.AddName(shipName)
	
	return pShip

def SetEnemyGroup(pPlayer): # AAAAAAAAAAAAAA
	global enemyGroup
	# enemyGroup = MissionLib.GetMission().GetEnemyGroup()
	
	if not enemyGroup:
		enemyGroup = App.ObjectGroup()
	enemyGroup.RemoveAllNames()
	name = GetCurrentTargetName(pPlayer)
	if name:
		enemyGroup.AddName(name)


def GetCurrentTargetName(pPlayer): # AAAAAAAAAAAA
	target = pPlayer.GetTarget()
	if target:
		castedTarget = App.ShipClass_Cast(target)
		if castedTarget:
			return castedTarget.GetName()

def GetAnyPerpendicularVector(direction, pPlayer):
	perp = direction.UnitCross(pPlayer.GetWorldUpTG())

	if perp.Length() > 0.5: 
		return perp

	# direction must be [near] equal to up
	return direction.UnitCross(pPlayer.GetWorldForwardTG())
