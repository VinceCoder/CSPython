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

def nextFreeSlot(defaultShape,boardHeight,boardLength,boardContents):
	for i in range(1,boardHeight*boardLength+1):
		shiftedLoc = pp2.pieceFits(boardLength,boardHeight,boardContents,defaultShape,i)
		if len(shiftedLoc):
			return shiftedLoc
	return []

def isBoardFilled(boardContents):
	for i in boardContents:
		if i == 0:
			return False
	return True
	
def main():
	params = readParams('load.txt')
	boardHeight = params['boardHeight']
	boardLength = params['boardLength']
	boardMax    = boardHeight*boardLength
	pieces = convertPiecesToDict(params['boardPieces'])
	print 'hi'
	#So we start off with all the different combinations to brute force
	for combo in pp3.getAllOrderings(pieces.keys()):
		#Now for each combination, we will place each piece one by one using next free slot.
		contents = [0]*boardMax
		for pieceName in combo:
			#Place piece in next free slot
			
			
			
			

main()	
	
	
