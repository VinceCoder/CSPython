class U_shape:
	def __init__(self, length, boardLength, label):
		self.length = length
		self.label = label
		self.defaultCoords = []
		self.defaultCoords.append(1)
		self.defaultCoords.append(2)
		for i in range(1,length):
			self.defaultCoords.append(boardLength*i+2)
		self.defaultCoords.append(boardLength*(length-1)+1)
		self.defaultCoords.sort()
	
	def getDefaultCoords(self):
		return self.defaultCoords
		
	def getLabel(self):
		return self.label
