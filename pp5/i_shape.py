class I_shape:
	def __init__(self, length, label):
		self.length = length
		self.label = label
		self.defaultCoords = range(1,length+1)
	
	def getDefaultCoords(self):
		return self.defaultCoords
		
	def getLabel(self):
		return self.label	
	
		
