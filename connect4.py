class Connect4:

    def __init__(self, moveCounter, row, col, currentPlayer, isValid, pieces, isPlaying, boardArray):

        self.moveCounter = 0
        self.row = 6
        self.col = 7
        self.currentPlayer = 1  # initialized to player 1
        self.isValid = True
        self.pieces = []
        self.isPlaying
        self.boardArray = [['' for i in range(col)] for j in range(row)]

    def printBoard(self):
        pass

    def updateBoard(self):
        pass

    def placeMove(self):
        pass

    def switchPlayers(self):
        pass

    def findEmptyRow(self):
        pass

    def checkWinner(self):
        pass

    def checkTie(self):
        pass

    def verticalCheck(self):
        pass

    def horizontalCheck(self):
        pass

    def negativeDiagnonalCheck(self):
        pass

    def positiveDiagonalCheck(self):
        pass
