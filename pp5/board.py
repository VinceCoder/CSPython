class Board:
	def __init__(self, boardLength, boardHeight, pieces):
		self.boardLength = boardLength
		self.boardHeight = boardHeight
		self.pieces = pieces
		self.tiles = [0]*boardLength*boardHeight
		self.snapShots = []
	
	def reset(self):
		self.tiles = [0]*self.boardLength*self.boardHeight
		
	def takeSnapShot(self):
		if self.tiles not in self.snapShots:
			self.snapShots.append(list(self.tiles))
		return self.tiles
		
	def shift(self,shape,freeSlot):
		diff = freeSlot-shape[0]
		return [e+diff for e in shape]
	
	def getColumnfromPosition(self,pos):
		a = pos % self.boardLength
		if a:
			return a
		else: 
			return self.boardLength
	
	def areShiftsHorizontallyBounded(self,shape,freeSlot):
		diff = freeSlot-shape[0]
		for i in shape:
			c = self.getColumnfromPosition(i)
			c2 = self.getColumnfromPosition(i+diff)
			if c2 < c:
				return False
		return True

	def isThereFreeSpace(self,shape,freeSlot):
		shifted = self.shift(shape,freeSlot)
		boardMax = self.boardHeight*self.boardLength
		for i in shifted:
			if i > boardMax:
				return False
			elif self.tiles[i-1]: 
				return False
		return True

	def pieceFits(self,defaultShape,freeSlot):
		if self.isThereFreeSpace(defaultShape,freeSlot):
				if self.areShiftsHorizontallyBounded(defaultShape, freeSlot):
					return self.shift(defaultShape,freeSlot) 
		return []
	
	def findFree(self):
		for index,val in enumerate(self.tiles):
			if isinstance(val,int) and val == 0:
				return index+1
		return -1
	
	def setTile(self,index, value):
		self.tiles[index-1] = value
	
	def printBoard(self,snapshot):
		"""
		Identical to the printBoard function in pp3 with the difference
		that it allows use of strings in contents. This is so we can print
		the labels of the shapes.
		"""
		length = self.boardLength
		height = self.boardHeight
		if len(snapshot) != length*height:
			print 'Invalid board!'
		elif not (type(snapshot) is list):
			print 'Invalid board!'
		else:
			print '|'+'-'*(2*length+1)+'|'
			for i in range(0,height):
				print '| '+' '.join(map(str,snapshot[length*i:length*i+length]))+' |'
			print '|'+'-'*(2*length+1)+'|'
	
	def printSnapShots(self):
		for i in self.snapShots:
			self.printBoard(i)
		print 'Total number of solutions: %d' % (len(self.snapShots))
