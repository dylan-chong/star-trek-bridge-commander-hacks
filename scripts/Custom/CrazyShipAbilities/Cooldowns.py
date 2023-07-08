import App

class SimpleCooldown:
	def __init__(self, cooldown):
		self.cooldown = cooldown
		self.lastTriggeredAt = -9999999
	
	def Trigger(self):
		if self.GetCooldownS() > 0:
			raise "Unexpectedly triggered when still in cooldown for " + str(self.GetCooldownS()) + " seconds"

		self.lastTriggeredAt = Now()
	
	def GetCooldownS(self):
		readyAt = self.lastTriggeredAt + self.cooldown
		return max(0, readyAt - Now())
	
	def GetNReady(self):
		return self.GetCooldownS() == 0

	def GetNCooldowns(self):
		return 1

	def IsReady(self):
		return self.GetNReady() == 1

class ParallelCooldown:
	"""
	Multiple cooldowns that can be triggered all at the same time, and be charged all at the same time
	"""

	def __init__(self, cooldown, nCooldowns):
		if nCooldowns <= 0:
			raise "Unexpected nCooldowns: " + str(nCooldowns)
		self.cooldown = cooldown

		self.simpleCooldowns = []
		for _ in range(0, nCooldowns):
			self.simpleCooldowns.append(SimpleCooldown(cooldown))
	
	def Trigger(self):
		oldestCooldown = self.GetAnyReadyCooldown()
		if not oldestCooldown:
			raise "Unexpectedly triggered when not ready"
		
		oldestCooldown.Trigger()

	def GetCooldownS(self):
		minCooldownS = None

		for simpleCooldown in self.simpleCooldowns:
			cooldownS = simpleCooldown.GetCooldownS()
			if not minCooldownS or cooldownS < minCooldownS:
				minCooldownS = cooldownS

		return minCooldownS
	
	def GetNReady(self):
		nReady = 0
		for simpleCooldown in self.simpleCooldowns:
			if not simpleCooldown.IsReady():
				continue
			nReady = nReady + 1

		return nReady

	def GetNCooldowns(self):
		return len(self.simpleCooldowns)

	def IsReady(self):
		return self.GetNReady() >= 1

	def GetAnyReadyCooldown(self):
		for simpleCooldown in self.simpleCooldowns:
			if simpleCooldown.IsReady():
				return simpleCooldown
		return None


def Now():
	return App.g_kUtopiaModule.GetGameTime()