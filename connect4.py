class Connect4:

    def __init__(self):

        self.row = 6
        self.col = 7
        self.currentPlayer = 'x'  # initialized to player X
        self.isOver = False
        self.boardArray = [
            ['-' for i in range(self.col)] for j in range(self.row)]

    def playGame(self):
        print("Welcome to Connect 4! Let's get started!")

        while not self.isOver:
            self.switchPlayers()
            self.printBoard()
            self.placeMove()
            self.isOver = self.checkWinner() or self.checkTie()

        if self.checkTie():
            print("It's a tie!")
            self.printBoard()
        else:
            print(f"Congrats, {self.currentPlayer}! You win!")
            self.printBoard()

    def printBoard(self):
        print("\n")
        for row in self.boardArray:
            print(" ".join(row))
        print("\n")

    def updateBoard(self, inputCol):
        self.boardArray[self.findEmptyRow(
            inputCol)][inputCol-1] = self.currentPlayer

    def placeMove(self):
        while True:
            userCol = input(
                f"Player {self.currentPlayer}, enter a column to place piece in: ")
            if not userCol.isnumeric():
                print("Invalid input. Try again.")
            else:
                if (int(userCol) < 1 or int(userCol) > 7) or self.findEmptyRow(int(userCol)) == -1:
                    print("Invalid input. Try again.")
                    continue
                self.updateBoard(int(userCol))
                break

    def switchPlayers(self):

        if self.currentPlayer == 'x':
            self.currentPlayer = 'o'
        else:
            self.currentPlayer = 'x'

        return self.currentPlayer

    def findEmptyRow(self, inputCol):
        for i in range(self.row - 1, -1, -1):
            #rows = 6
            if self.boardArray[i][inputCol-1] == '-':
                return i
        return -1

    def checkWinner(self):
        if self.verticalCheck() or self.horizontalCheck() or self.negativeDiagnonalCheck() or self.positiveDiagonalCheck():
            return True
        return False

    # finds the columns with openings

    def validColumns(self):
        legal_moves = []

        for i in range(self.col):
            if self.boardArray[0][i] == '-':
                legal_moves.append(i)
        return legal_moves

    def checkTie(self):

        # if there are no more legal moves and there is no winner -- its a tie
        if len(self.validColumns()) == 0 and self.checkWinner() == False:
            return True
        return False

    def verticalCheck(self):
        for i in range(self.col):
            for j in range(self.row-3):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j+1][i] == self.currentPlayer and self.boardArray[j+2][i] == self.currentPlayer and self.boardArray[j+3][i] == self.currentPlayer:
                    self.boardArray[j][i] = self.boardArray[j][i].upper()
                    self.boardArray[j+1][i] = self.boardArray[j+1][i].upper()
                    self.boardArray[j+2][i] = self.boardArray[j+2][i].upper()
                    self.boardArray[j+3][i] = self.boardArray[j+3][i].upper()
                    return True
        return False

    def horizontalCheck(self):
        for i in range(self.col-3):
            for j in range(self.row):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j][i+1] == self.currentPlayer and self.boardArray[j][i+2] == self.currentPlayer and self.boardArray[j][i+3] == self.currentPlayer:
                    self.boardArray[j][i] = self.boardArray[j][i].upper()
                    self.boardArray[j+1][i] = self.boardArray[j+1][i].upper()
                    self.boardArray[j+2][i] = self.boardArray[j+2][i].upper()
                    self.boardArray[j+3][i] = self.boardArray[j+3][i].upper()
                    return True
        return False

    def negativeDiagnonalCheck(self):
        for i in range(self.col-3):
            for j in range(3, self.row):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j-1][i+1] == self.currentPlayer and self.boardArray[j-2][i+2] == self.currentPlayer and self.boardArray[j-3][i+3] == self.currentPlayer:
                    self.boardArray[j][i] = self.boardArray[j][i].upper()
                    self.boardArray[j+1][i] = self.boardArray[j+1][i].upper()
                    self.boardArray[j+2][i] = self.boardArray[j+2][i].upper()
                    self.boardArray[j+3][i] = self.boardArray[j+3][i].upper()
                    return True
        return False

    def positiveDiagonalCheck(self):
        for i in range(self.col-3):
            for j in range(self.row-3):
                if self.boardArray[j][i] == self.currentPlayer and self.boardArray[j+1][i+1] == self.currentPlayer and self.boardArray[j+2][i+2] == self.currentPlayer and self.boardArray[j+3][i+3] == self.currentPlayer:
                    self.boardArray[j][i] = self.boardArray[j][i].upper()
                    self.boardArray[j+1][i] = self.boardArray[j+1][i].upper()
                    self.boardArray[j+2][i] = self.boardArray[j+2][i].upper()
                    self.boardArray[j+3][i] = self.boardArray[j+3][i].upper()
                    return True
        return False
