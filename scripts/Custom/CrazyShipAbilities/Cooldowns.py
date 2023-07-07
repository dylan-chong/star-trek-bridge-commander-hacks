import App

def now():
	return App.g_kUtopiaModule.GetGameTime()

class SimpleCooldown:
	def __init__(self, cooldown):
		self.cooldown = cooldown
		self.lastTriggeredAt = -9999999
	
	def IsReady(self):
		return self.GetRemainingCooldown() == 0
	
	def GetRemainingCooldown(self):
		earliestAvailableTriggerTime = self.lastTriggeredAt + self.cooldown
		return max(0, earliestAvailableTriggerTime - now())
	
	def Trigger(self):
		if not self.IsReady():
			raise "Unexpectedly triggered ability when it is still in cooldown for " + str(self.GetRemainingCooldown()) + ' seconds'
		self.lastTriggeredAt = now()