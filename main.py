from board import Board
from moves_controller import MoveController
from pieces import Knight


def main():
    board = Board()
    moveController = MoveController()
    
    while(True):
        
        print(board)
        start = input("Enter cell to move: ")
        start = [int(start[0]), int(start[1])]
        moves = moveController.getMoves(board, start[0], start[1])
        for move in moves:
            print(move)
        choice = input("Enter selected move: ")
        choice = int(choice)
        board.applyMove(moves[choice])
        
    
if __name__ == "__main__":
    main()