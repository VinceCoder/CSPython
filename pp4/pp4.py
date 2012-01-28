import pp2
import pp3

def readParams(fileName):
	f = open(fileName,'r')
	paramsList = {}
	paramsList['boardLength'] = (int(f.readline()))
	paramsList['boardHeight'] = (int(f.readline()))	
	paramsList['boardPieces'] = []
	for line in f:
		paramsList['boardPieces'].append(line.strip())
	return paramsList

def convertPiecesToDict(pieces):
	outDict = {}
	for piece in pieces:
		splitUp = pp3.getPiece(piece)
		outDict[splitUp[2]]=splitUp[0:2]
	return outDict

#Returns a list of list of all possible places a piece might fit
def getAllPossiblePlaces(defaultShape,boardHeight,boardLength, boardContents):
	possiblePlaces = []
	for i in boardHeight*boardLength:
		shiftedLoc = pp2.pieceFits(boardLength,boardHeight,boardContents,defaultShape,i)
		if len(shiftedLoc):
			possiblePlaces.append(shiftedLoc)
	return possiblePlaces

def main():
	params = readParams('load.txt')
	boardHeight = params['boardHeight']
	boardLength = params['boardLength']
	boardMax    = boardHeight*boardLength
	pieces = convertPiecesToDict(params['boardPieces'])
	
	#So we start off with all the different combinations to brute force
	for combo in pp3.getAllOrderings(pieces.keys()):
		#Now for each combination, we need to go through all the placements
		contents = [0]*boardMax
		for pieceName in combo:
			for loc in getAllPossiblePlaces(pp3.createShape(pieces[pieceName][0]),boardHeight,boardLength,contents):
				for pos in loc:
					contents[pos] = 1
			
			
	
	
