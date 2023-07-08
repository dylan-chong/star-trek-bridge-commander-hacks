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