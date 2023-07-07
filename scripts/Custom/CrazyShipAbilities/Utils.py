import App

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