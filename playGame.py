from connect4 import *


def main():
    connect4 = Connect4()
    connect4.printBoard()
    
    isPlaying = True
    
    while(isPlaying):
        connect4.placeMove()
        connect4.checkWinner()
        
        if(isPlaying == False):
            break


if __name__ == "__main__":
    main()
