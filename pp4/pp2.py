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

def areShiftsVerticallyBounded(shape,freeSlot,height,length):
	shifted = shift(shape,freeSlot)
	maxIndex = height*length
	for i in shifted:
		if i > maxIndex:
			return False
	return True

def isThereFreeSpace(shape,freeSlot,contents):
	shifted = shift(shape,freeSlot)
	for i in shifted:
		if contents[i-1]: 
			return False
	return True

def pieceFits(boardLength,boardHeight,boardContents,defaultShape,freeSlot):
	if areShiftsVerticallyBounded(defaultShape,freeSlot,boardHeight,boardLength):
			if areShiftsHorizontallyBounded(defaultShape, freeSlot, boardLength):
				if isThereFreeSpace(defaultShape,freeSlot,boardContents):
					return shift(defaultShape,freeSlot) 
	return []

