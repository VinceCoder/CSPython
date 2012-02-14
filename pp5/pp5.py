from x_shape import *
from t_shape import *
from i_shape import *
from l_shape import *
from u_shape import *
from board import *
import itertools

def getPiece(pieceText):
	a = pieceText.split(' ')
	return (a[0],int(a[1]),a[2])

def getAllOrderings(inList):
	outList = []
	for l in itertools.permutations(inList):
		outList.append(list(l))
	return outList

def main():
	f = open('load.txt','r')
	boardLength =  (int(f.readline()))
	boardHeight =  (int(f.readline()))	
	boardPieces =  []
	for line in f:
		piece = getPiece(line.strip())
		if piece[0] == 'T_shape':
			boardPieces.append(T_shape(piece[1],boardLength,piece[2]))
		elif piece[0] == 'X_shape':
			boardPieces.append(X_shape(piece[1],boardLength,piece[2]))
		elif piece[0] == 'I_shape':
			boardPieces.append(I_shape(piece[1],piece[2]))
		elif piece[0] == 'L_shape':
			boardPieces.append(L_shape(piece[1],boardLength,piece[2]))
		elif piece[0] == 'U_shape':
			boardPieces.append(U_shape(piece[1],boardLength,piece[2]))
	
	puzzleBoard = Board(boardLength, boardHeight, boardPieces)
		
	for combo in getAllOrderings(boardPieces):
		for piece in combo:
			freePos = puzzleBoard.findFree()
			if freePos == -1:
				puzzleBoard.takeSnapShot()
				puzzleBoard.reset()
			else:
				shiftedPos = puzzleBoard.pieceFits(piece.getDefaultCoords(),freePos)
				if shiftedPos:
					for i in shiftedPos:
						puzzleBoard.setTile(i,piece.getLabel())
				else:
					puzzleBoard.reset()
					break;
	
	puzzleBoard.printSnapShots()
			
if __name__ == '__main__':
    main()
