class Connect4:

    def __init__(self):

        self.moveCounter = 0
        self.row = 6
        self.col = 7
        self.currentPlayer = 1  # initialized to player 1
        self.isValid = True
        self.pieces = []
        self.isPlaying = True
        self.boardArray = [
            ['-' for i in range(self.col)] for j in range(self.row)]

    def playGame(self):
        print("Welcome to Connect 4! Let's get started!")

    def printBoard(self):
        print("\n")
        for row in self.boardArray:
            print(" ".join(row))
        print("\n")

    def updateBoard(self):
        pass

    def placeMove(self):
        userCol = input("Enter a column to place piece in: ")
        while (not userCol.isnumeric()) or (userCol < 1 or userCol > 7):
            print("Invalid input. Try again.")
            userCol = input("Enter a column to place piece in: ")

        self.boardArray[self.row][self.col] = self.currentPlayer

    def switchPlayers(self):

        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'

        return self.currentPlayer

    def findEmptyRow(self):
        for i in range(self.row):
            #rows = 6
            if self.boardArray[i][self.col] == ' ':
                return i

    def checkWinner(self):
        if self.verticalCheck() or self.horizontalCheck() or self.negativeDiagnonalCheck() or self.positiveDiagonalCheck():
            return True
        return False

    # finds the columns with openings

    def validColumns(self):
        legal_moves = []

        for i in range(self.col):
            if self.boardArray[self.row-1][i] == ' ':
                legal_moves.append(i)
        return legal_moves

    def checkTie(self):

        # if there are no more legal moves and there is no winner -- its a tie
        if len(validColumns(self.boardArray)) == 0 or checkWinner(self.boardArray, self.currentPlayer) == False:
            return True
        return False

    def verticalCheck(self):
        for i in range(self.col):
            for j in range(self.row-3):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j+1][i] == self.currentPlayer and self.boardArray[j+2][i] == self.currentPlayer and self.boardArray[j+3][i] == self.currentPlayer:
                    return True
        return False

    def horizontalCheck(self):
        for i in range(self.col-3):
            for j in range(self.row):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j][i+1] == self.currentPlayer and self.boardArray[j][i+2] == self.currentPlayer and self.boardArray[j][j+3] == self.currentPlayer:
                    return True
        return False

    def negativeDiagnonalCheck(self):
        for i in range(self.col-3):
            for j in range(3, self.row):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j-1][i+1] == self.currentPlayer and self.boardArray[j-2][i+2] == self.currentPlayer and self.boardArray[j-3][j+3] == self.currentPlayer:
                    return True
        return False

    def positiveDiagonalCheck(self):
        for i in range(self.col-3):
            for j in range(self.row-3):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j+1][i+1] == self.currentPlayer and self.boardArray[j+2][i+2] == self.currentPlayer and self.boardArray[j+3][j+3] == self.currentPlayer:
                    return True
        return False
