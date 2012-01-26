def printBoard(length, height, contents):
	if len(contents) != length*height:
		print 'Invalid board!'
	#elif (type(contents) not list) or (type(contents[0]) not int):
#		print 'Invalid board!'
	else:
		print '|'+'-'*(2*length+1)+'|'
		for i in range(0,height):
			print '| '+' '.join(map(str,contents[length*i:length*i+length]))+' |'
		print '|'+'-'*(2*length+1)+'|'
		
			 
		
				 
	
