class Connect4:

    def __init__(self, moveCounter, row, col, currentPlayer, isValid, pieces, isPlaying, boardArray):

        self.moveCounter = 0
        self.row = 6
        self.col = 7
        self.currentPlayer = 1  # initialized to player 1
        self.isValid = True
        self.pieces = []
        self.isPlaying
        self.boardArray = [[' ' for i in range(col)] for j in range(row)]

    def printBoard(self):
        pass

    def updateBoard(self):
        pass

    def placeMove(currentPlayer, boardArray, row, column):
    	boardArray[row][column] = currentPlayer
        
    def switchPlayers(currentPlayer):

    	if currentPlayer == 'X':
    		currentPlayer = 'O'
    	else:
    		currentPlayer == 'X'

    	return currentPlayer
        

    def findEmptyRow(boardArray, column):
    	for i in range(row): 
    		#rows = 6
    		if boardArray[i][column] == ' ':
    			return i 

    def checkWinner(self):
    	if verticalCheck(boardArray, currentPlayer) or horizontalCheck(boardArray, currentPlayer) or negativeDiagnonalCheck(boardArray, currentPlayer) or positiveDiagonalCheck(boardArray, currentPlayer):
    		return True 
    	return False


    #finds the columns with openings 
    def validColumns(boardArray):
    	legal_moves = []

    	for i in range(col):
    		if boardArray[row-1][i] == ' ':
    			legal_moves.append(i)
    	return legal_moves
        

    def checkTie(self):

    	#if there are no more legal moves and there is no winner -- its a tie 
    	if len(validColumns(boardArray)) == 0 or checkWinner(boardArray, currentPlayer) == False:
    		return True
    	return False

    def verticalCheck(boardArray, currentPlayer):
    	for i in range(col):
    		for j in range(row-3):
    			if boardArray[j][i] == currentPlayer and boardArray[j+1][i] == currentPlayer and boardArray[j+2][i] == currentPlayer and boardArray[j+3][i] == currentPlayer:
    				return True
    	return False

    def horizontalCheck(boardArray, currentPlayer):
    	for i in range(col-3):
    		for j in range(row):
    			if boardArray[j][i] == currentPlayer and boardArray[j][i+1] == currentPlayer and boardArray[j][i+2] == currentPlayer and boardArray[j][j+3] == currentPlayer:
    				return True
    	return False 
        

    def negativeDiagnonalCheck(self):
        for i in range(col-3):
        	for j in range(3, row):
        		if boardArray[j][i] == currentPlayer and boardArray[j-1][i+1] == currentPlayer and boardArray[j-2][i+2] == currentPlayer and boardArray[j-3][j+3] == currentPlayer:
        			return True
        return False

    def positiveDiagonalCheck(self):
    	for i in range(col-3):
    		for j in range(row-3):
    			if boardArray[j][i] == currentPlayer and boardArray[j+1][i+1] == currentPlayer and boardArray[j+2][i+2] == currentPlayer and boardArray[j+3][j+3] == currentPlayer:
        			return True
        return False
        
