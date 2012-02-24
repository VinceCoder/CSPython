import itertools

def printBoard(length, height, contents):
	if len(contents) != length*height:
		print 'Invalid board!'
	elif not (type(contents) is list):
		print 'Invalid board!'
	elif not (type(contents[0]) is int or type(contents[0]) is str):
		print 'Invalid board!'	
	else:
		print '|'+'-'*(2*length+1)+'|'
		for i in range(0,height):
			print '| '+' '.join(map(str,contents[length*i:length*i+length]))+' |'
		print '|'+'-'*(2*length+1)+'|'
		
def getPiece(pieceText):
	a = pieceText.split(' ')
	return (a[0],int(a[1]),a[2])

def createShape(shapeName, shapeLength, boardLength):
	outShape = []
	if shapeName == 'L_shape':
		#Generates the first two elements of the L.
		outShape.append(1)
		outShape.append(2)
		
		#Generates the long part of the L
		for i in range(1,shapeLength):
			outShape.append(boardLength*i+1)
			
	elif shapeName == 'T_shape':
		outShape.append(2)
		for i in range(1,shapeLength+1):
			outShape.append(boardLength+i)
	
	elif shapeName == 'X_shape':
		outShape.append(2)
		for i in range(1,shapeLength+1):
			outShape.append(boardLength+i)
		
		outShape.append(boardLength*2+2)
	
	elif shapeName == 'U_shape':
		outShape.append(1)
		outShape.append(2)
		for i in range(1,shapeLength):
			outShape.append(boardLength*i+2)
		outShape.append(boardLength*(shapeLength-1)+1)
		outShape.sort()
	
	elif shapeName == 'I_shape':
		outShape = range(1,shapeLength+1)
	
	else:
		print 'Invalid shape!'
		return
			
	return outShape

def getAllOrderings(inList):
	outList = []
	for l in itertools.permutations(inList):
		outList.append(list(l))
	return outList
