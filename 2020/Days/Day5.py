import	math,\
		\
		CoreLib

class BinaryBoarding(CoreLib.BasePuzzle):
	def __init__(self):
		super().__init__()

	def ParseInput(self, input):
		self.inputData = CoreLib.InputLineSplit(input)

	def Run(self, args):
		part = args
		if part == 1:
			self.allSeatIDs = [int(combo.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), 2) for combo in self.inputData]
			return max(self.allSeatIDs)
		self.allSeatIDs.sort()
		for index, ID in enumerate(self.allSeatIDs):
			if self.allSeatIDs[index + 1] - ID == 2:
				return ID + 1

class Day5(CoreLib.BaseDay):
	def __init__(self):
		self.puzzles = [(BinaryBoarding, 0, [1, 2])]