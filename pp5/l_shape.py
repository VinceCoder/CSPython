class L_shape:
	def __init__(self, length, boardLength, label):
		self.length = length
		self.label = label
		self.defaultCoords = []
		self.defaultCoords.append(1)
		self.defaultCoords.append(2)
		#Generates the long part of the L
		for i in range(1,length):
			self.defaultCoords.append(boardLength*i+1)
	
	def getDefaultCoords(self):
		return self.defaultCoords
		
	def getLabel(self):
		return self.label	
	
		
