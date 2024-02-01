from board import Board
from moves_controller import MoveController
from pieces import *
import os

def stringToCoord(string):  # should have format like "A1"
    if len(string) != 2:
        return None
    col = ord(string[0]) - ord('A')
    row = int(string[1]) - 1
    if col < 0 or col > 7 or row < 0 or row > 7:
        return None
    return [row, col]

def coordToString(coord):
    return chr(ord('A') + coord[1]) + str(coord[0]+1)

def main():
    board = Board()
    whiteTurn = True
    
    while(True):    
        os.system("clear") if os.name == "posix" else os.system("cls")
        print(board)
        print("White turn" if whiteTurn else "Black turn")
        
        # get start cell
        start = input("Enter cell to move: ")
        start = stringToCoord(start)
        if start == None:
            continue
        
        # check if start cell is valid
        if isinstance(board.board[start[0]][start[1]], EmptyCell) or board.board[start[0]][start[1]].isWhite() != whiteTurn:
            continue
        
        # get possible moves
        moves = board.getMoves(start[0], start[1])
        for i in range(len(moves)):
            print(str(i) + ": " + coordToString(moves[i].end))
        choice = input("Enter selected move: ")
        if not choice.isdigit():
            continue
        choice = int(choice)
        if choice < 0 or choice >= len(moves):
            continue
        
        # apply move
        board.applyMove(moves[choice])
        whiteTurn = not whiteTurn
        
    
if __name__ == "__main__":
    main()