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

#MAIN
def main():
	#START

	length   = input('Enter the length of the board: ')
	height   = input('Enter the height of the board: ')
	contents = input('Enter the contents of the board, as a list (i.e. [0,1,....,0,0]): ')
	shape    = input('Enter the shape, in terms of default coordinates (i.e. [1,2,6,11]): ')
	freeSlot = input('Enter the next free slot: ') 
	
	if areShiftsVerticallyBounded(shape,freeSlot,height,length):
		if areShiftsHorizontallyBounded(shape, freeSlot, length):
			if isThereFreeSpace(shape,freeSlot,contents):
				print shift(shape,freeSlot)
				return 
	print 'Failed!'
	
	#YOU MAY NOT WRITE/CHANGE ANYTHING BELOW HERE
	
#THIS WILL ALLOW YOUR CODE TO RUN	
main()
