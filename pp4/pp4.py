import pp2
import pp3

# Identical to the printBoard function in pp3 with the difference
# that it allows use of strings in contents. This is so we can print
# the labels of the shapes.
def fancyPrintBoard(length, height, contents):
	if len(contents) != length*height:
		print 'Invalid board!'
	elif not (type(contents) is list):
		print 'Invalid board!'
	else:
		print '|'+'-'*(2*length+1)+'|'
		for i in range(0,height):
			print '| '+' '.join(map(str,contents[length*i:length*i+length]))+' |'
		print '|'+'-'*(2*length+1)+'|'

# Reads the input text file and parses out the height, length, and pieces
# It expects a file with the first line containing length, second line
# containing height, and the next lines containing a shape in the format
# shape_type shape_length shape_label
# eg. T_shape 5 T
def readParams(fileName):
	f = open(fileName,'r')
	paramsList = {}
	paramsList['boardLength'] = (int(f.readline()))
	paramsList['boardHeight'] = (int(f.readline()))	
	paramsList['boardPieces'] = []
	for line in f:
		paramsList['boardPieces'].append(line.strip())
	return paramsList

# This function takes a list of tuples with shape information
# as input: eg. [(L_shape,4,L), (T_shape,4,T)] and converts them
# them to dictionary eg. : {'L':[1,2,6,10], 'T':[2,6,7,8,9]}
def convertPiecesToDict(pieces,boardLength):
	outDict = {}
	for piece in pieces:
		splitUp = pp3.getPiece(piece)
		outDict[splitUp[2]]=pp3.createShape(splitUp[0],splitUp[1],boardLength)
	return outDict

# Given a shape, board sizes, and the board's contents, the function
# goes through all positions starting from 1 and determines
# the next free position where the shape would fit.
def nextFreeSlot(defaultShape,boardHeight,boardLength,boardContents):
	for i in range(1,boardHeight*boardLength+1):
		if boardContents[i-1] != 1:
			shiftedLoc = pp2.pieceFits(boardLength,boardHeight,boardContents,defaultShape,i)
			if len(shiftedLoc):
				return shiftedLoc
	return []

# Given the board contents, determines if the board is completely filled.
def isBoardFilled(boardContents):
    for i in boardContents:
    	if i == 0:
    		return False
    return True

# Sometimes solutions can be repeated. This function takes a solution as a list (eg. [T,T,T])
# along with a list of previous solutions (eg. [[I,I,U],[T,T,T],[X,X,U]]). It checks
# whether the currentSolution exists in previousSolutions
def wasSolutionPreviouslyComputed(currentSolution,previousSolutions):
    return currentSolution in previousSolutions

def main():
	params = readParams('load.txt')
	boardHeight = params['boardHeight']
	boardLength = params['boardLength']
	boardMax    = boardHeight*boardLength
	pieces = convertPiecesToDict(params['boardPieces'],boardLength)
	numSolutions = 0
	solutions = []
	
	# We need to use sorted keys to keep the output order identical to professor's.
	for combo in pp3.getAllOrderings(sorted(pieces.keys())):
	
		# Start with a fresh board for each combination
		contents = [0]*boardMax
		fancyContents = ['']*boardMax
		
		# Go through each piece and place in the next available free slot on the board
		for pieceLabel in combo:
			shiftedShape = nextFreeSlot(pieces[pieceLabel],boardHeight,boardLength,contents)
			
			# If a certain shape doesn't fit, go to the next combo.
			if len(shiftedShape) == 0:
				break;
			
			#Place piece on the board by updating contents
			for i in shiftedShape:
			    contents[i-1] = 1
			    fancyContents[i-1] = pieceLabel
			
			#Check whether we have a solution
			if isBoardFilled(contents) and not wasSolutionPreviouslyComputed(fancyContents,solutions):
			    fancyPrintBoard(boardLength,boardHeight,fancyContents)
			    solutions.append(fancyContents[:])
			    numSolutions = numSolutions + 1
			
	print 'Number of solutions: %d' % (numSolutions)

if __name__ == '__main__':
    main()
