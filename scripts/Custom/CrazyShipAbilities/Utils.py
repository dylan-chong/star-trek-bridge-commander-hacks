import App

def GenChildShipName(prefix, i, pPlayer):
	return prefix + ' ' + str(i + 1) + ' (' + pPlayer.GetName() + ')'

def KphToInternalGameSpeed(kph):
	return kph / 600.0

def Unitized(vector):
	unitVector = CloneVector(vector)
	unitVector.Unitize()
	return unitVector

def CloneVector(vector):
	copy = App.TGPoint3()
	copy.Set(vector)
	return copy

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

def SetSameVelocityAndDirectionAsPlayer(pShip, pPlayer):
	up = pPlayer.GetWorldUpTG()
	forward = pPlayer.GetWorldForwardTG()
	pShip.AlignToVectors(forward, up)

	pShip.SetVelocity(pPlayer.GetVelocityTG())

def GetCurrentTarget(pPlayer):
	target = pPlayer.GetTarget()
	if target:
		castedTarget = App.ShipClass_Cast(target)
		if castedTarget:
			return castedTarget

	return None

def SpawnDroneShip(shipType, shipName, distance, pPlayer, group):
	import MissionLib
	import loadspacehelper
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

def GetSubsystemByName(pShip, name):
	pPropSet = pShip.GetPropertySet()
	pPropList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	iNumItems = pPropList.TGGetNumItems()

	desiredSubsystem = None

	pPropList.TGBeginIteration()
	for i in range(iNumItems):
		pInstance = pPropList.TGGetNext()
		pProperty = App.SubsystemProperty_Cast(pInstance.GetProperty())
		pSubsystem = pShip.GetSubsystemByProperty(pProperty)

		if pSubsystem.GetName() != name:
			continue

		desiredSubsystem = pSubsystem
		break

	pPropList.TGDoneIterating()
	return desiredSubsystem

def EmitEventAfterDelay(eType, delayS):
	"""
	Schedules a timer on the current game object.
	Assumes that you have already registered an event handler on the game object to call your function using:

		pGame.AddPythonFuncHandlerForInstance(eType, 'Module.FnName')
	"""
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(App.Game_GetCurrentGame())
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + delayS)
	pTimer.SetEvent(pEvent)
	App.g_kTimerManager.AddTimer(pTimer)

def ReregisterEventHanders(handlers, target, handlerModuleName):
	for eventType, funcName in handlers:
		App.g_kEventManager.RemoveBroadcastHandler(eventType, target, handlerModuleName + '.' + funcName)
		App.g_kEventManager.AddBroadcastPythonFuncHandler(eventType, target, handlerModuleName + '.' + funcName)

def ChangePlayerRepairPointsBy(amount):
	player = App.Game_GetCurrentPlayer()
	if not player:
		return

	repairSubsystem = player.GetRepairSubsystem()
	if not repairSubsystem:
		return

	repair = repairSubsystem.GetProperty()
	currentPoints = repair.GetMaxRepairPoints()
	repair.SetMaxRepairPoints(currentPoints + amount)

def GetShipType(ship):
	return ship.GetShipProperty().GetName().GetCString()

def GetPlayerShipType():
	pPlayer = App.Game_GetCurrentPlayer()

	if not pPlayer:
		return None

	return GetShipType(pPlayer)
