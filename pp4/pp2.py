#PP2	


def shift(shape,freeSlot):
	diff = freeSlot-shape[0]
	return [e+diff for e in shape]

def getColumnfromPosition(pos,length):
	a = pos % length
	if a:
		return a
	else: 
		return length
	
def areShiftsHorizontallyBounded(shape,freeSlot,length):
	diff = freeSlot-shape[0]
	for i in shape:
		c = getColumnfromPosition(i,length)
		c2 = getColumnfromPosition(i+diff,length)
		if c2 < c:
			return False
	return True

def isThereFreeSpace(shape,freeSlot,contents,boardMax):
	shifted = shift(shape,freeSlot)
	for i in shifted:
		if i > boardMax:
			return False
		elif contents[i-1]: 
			return False
	return True

def pieceFits(boardLength,boardHeight,boardContents,defaultShape,freeSlot):
	if isThereFreeSpace(defaultShape,freeSlot,boardContents,boardHeight*boardLength):
			if areShiftsHorizontallyBounded(defaultShape, freeSlot, boardLength):
				return shift(defaultShape,freeSlot) 
	return []

