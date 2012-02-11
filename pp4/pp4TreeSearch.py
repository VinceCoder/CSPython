import pp2
import pp3
import Queue

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
    for i in xrange(1,boardHeight*boardLength+1):
        if boardContents[i-1] != 1:
            shiftedLoc = pp2.pieceFits(boardLength,boardHeight,boardContents,defaultShape,i)
            if len(shiftedLoc):
                return shiftedLoc
    return []
    
# Given the board contents, determines if the board is completely filled.
def isBoardFilled(boardContents):
    return all(boardContents)
    
# Sometimes solutions can be repeated. This function takes a solution as a list (eg. [T,T,T]) 
# along with a list of previous solutions (eg. [[I,I,U],[T,T,T],[X,X,U]]). It checks
# whether the currentSolution exists in previousSolutions
def wasSolutionPreviouslyComputed(currentSolution,previousSolutions):
    return currentSolution in previousSolutions   

def doPiecesFit(node,pieces,boardHeight,boardLength):
    contents = [0]*boardHeight*boardLength
    fancyContents = ['']*boardHeight*boardLength
    for pieceLabel in node:
        shiftedShape = nextFreeSlot(pieces[pieceLabel],boardHeight,boardLength,contents)
        # If there are no free positions
        if len(shiftedShape) == 0:
               return 0
			            
	    #Place piece on the board by updating contents
        for i in shiftedShape:
            contents[i-1] = 1
            fancyContents[i-1] = pieceLabel
        
        if isBoardFilled(contents):
            return fancyContents
    return 1

def main():
    params = readParams('load.txt')
    boardHeight = params['boardHeight']
    boardLength = params['boardLength']
    boardMax    = boardHeight*boardLength
    pieces = convertPiecesToDict(params['boardPieces'],boardLength)
    
    # We do a breath-first search across the combinations.
    # Branches where a piece does not fit are not pursued saving
    # computations. This approach is better for larger puzzles.
    
    numSolutions = 0
    solutions = []
    frontier = Queue.Queue()
    
    #Initialize the frontier
    for i in pieces.keys():
        frontier.put(i)
        
    explored = set()
    options = ''.join(pieces.keys())

    while True:
        if frontier.empty():
            break
        node = frontier.get()
        ret = doPiecesFit(node,pieces,boardHeight,boardLength)
        explored.add(node)
        if type(ret) is int and ret == 1:
            # Expand the viable node.
            cl = options.translate(None,node)
            for x in cl:
                newnode = node+x
                # Add the resulting new nodes to frontier.
                if newnode not in explored:
                    frontier.put(newnode)
        elif type(ret) is list:
            if not wasSolutionPreviouslyComputed(ret,solutions):
                fancyPrintBoard(boardLength,boardHeight,ret)
                numSolutions = numSolutions+1
                solutions.append(ret[:])
                		
    print 'Number of solutions: %d' % (numSolutions)

if __name__ == '__main__':
    main()
	
