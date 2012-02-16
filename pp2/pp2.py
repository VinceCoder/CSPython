#PP2    


def shift(shape,freeSlot):
    """ 
    Takes a shape (eg. [1,2,6,11]) and the final
    slot position, and returns the coordinates of the shape
    shifted to that position
    """
    diff = freeSlot-shape[0]
    return [e+diff for e in shape]

def getColumnfromPosition(pos,length):
	""" 
	Given a position on a puzzle board and the length
	of that board, the function returns the column position
	of that point. eg. a position of 5 on length 3 board will
	give a column of 2
	"""
    a = pos % length
    if a:
        return a
    else: 
        return length
    
def areShiftsHorizontallyBounded(shape,freeSlot,length):
    """ 
    The function determines whether a shape shifted to a
    certain freeslot will cause portions of that shape to 
    get cut in the horizontal direction. 
    
    Algorithm: We know that the default shape is in the left 
    most position on the board, therefore any proper shift should
    only cause the column value of each piece to be greater (or 
    equal to in the case of no shift).
    """     
    diff = freeSlot-shape[0]
    for i in shape:
        c = getColumnfromPosition(i,length)
        c2 = getColumnfromPosition(i+diff,length)
        if c2 < c:
            return False
    return True

def isThereFreeSpace(shape,freeSlot,contents,boardMax):
	""" 
	This function serves two purposes. First it checks whether
	the shifted piece has space to be placed (i.e slots are not filled).
	It also checks whether the shifted shape has not exceed the vertical
	limit of the board
	"""
    shifted = shift(shape,freeSlot)
    for i in shifted:
        if i > boardMax:
            return False
        elif contents[i-1]: 
            return False
    return True

#MAIN
def main():
    #START

    length   = input('Enter the length of the board: ')
    height   = input('Enter the height of the board: ')
    contents = input('Enter thes contents of the board, as a list (i.e. [0,1,....,0,0]): ')
    shape    = input('Enter the shape, in terms of default coordinates (i.e. [1,2,6,11]): ')
    freeSlot = input('Enter the next free slot: ') 
    
    if isThereFreeSpace(shape,freeSlot,contents,height*length):
        if areShiftsHorizontallyBounded(shape, freeSlot, length):
            print shift(shape,freeSlot)
            return 
    
    print 'Failed!'
    
    #YOU MAY NOT WRITE/CHANGE ANYTHING BELOW HERE
    
#THIS WILL ALLOW YOUR CODE TO RUN   
main()
