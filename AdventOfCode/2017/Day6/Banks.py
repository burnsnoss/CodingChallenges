class Banks:
	banks = []

	def __init__(self, _banks):
		self.banks = _banks

	def redistribute(self, index):
		blocks = self.banks[index]
		self.banks[index] = 0
		index += 1

		num_banks = len(self.banks)

		while blocks > 0:
			self.banks[index % num_banks] += 1

			blocks -= 1
			index += 1

		return

	def printBanks(self):
		print self.banks
		return

	def getConfiguration(self):
		return self.banks

	def getMaxBankIndex(self):
		max_value = max(self.banks)
		index = self.banks.index(max_value)
		return index
