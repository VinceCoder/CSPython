class L_shape:
	def __init__(self, length, boardLength, label):
		self.length = length
		self.label = label
		self.defaultCoords = []
		self.defaultCoords.append(2)
		for i in range(1,length+1):
			self.defaultCoords.append(boardLength+i)
		self.defaultCoords.append(boardLength*2+2)
	
	def getDefaultCoords():
		return self.defaultCoords
		
	def getLabel():
		return self.label	
	
		
