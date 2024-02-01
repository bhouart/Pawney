from pieces import *
from move import Move
from moves_controller import MoveController
class Board:
    
    def __init__(self):
        
        self.board = [[EmptyCell() for __ in range(8)] for _ in range(8)]
        self.initialBoard()
        self.enPassant = None
        self.boardColumns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.moveController = MoveController()
    
    def __str__(self):
        result = "   "
        for i in range(8):
            result += self.boardColumns[i] + " "
        result += "\n\n"
        for i in range(7, -1, -1):
            result += str(i+1) + "  "
            for j in range(8):
                result += str(self.board[i][j]) + " "
            result += "\n"
        return result
    def initialBoard(self):
        # white pieces
        self.board[0][0] = Rook(True)
        self.board[0][1] = Knight(True)
        self.board[0][2] = Bishop(True)
        self.board[0][3] = Queen(True)
        self.board[0][4] = King(True)
        self.board[0][5] = Bishop(True)
        self.board[0][6] = Knight(True)
        self.board[0][7] = Rook(True)
        
        # white pawns
        for i in range(8):
            self.board[1][i] = Pawn(True)
        
        # black pieces
        self.board[7][0] = Rook(False)
        self.board[7][1] = Knight(False)
        self.board[7][2] = Bishop(False)
        self.board[7][3] = Queen(False)
        self.board[7][4] = King(False)
        self.board[7][5] = Bishop(False)
        self.board[7][6] = Knight(False)
        self.board[7][7] = Rook(False)
        
        # black pawns
        for i in range(8):
            self.board[6][i] = Pawn(False)
    
    def getMoves(self, row, col):
        return self.moveController.getMoves(self.board, row, col, self.enPassant)
    
    def applyMove(self, move: Move):
                
        self.board[move.end[0]][move.end[1]] = self.board[move.start[0]][move.start[1]]
        self.board[move.start[0]][move.start[1]] = EmptyCell()
        if move.enPassant:
            self.board[move.enPassant[0]][move.enPassant[1]] = EmptyCell()
        if move.doublePawnMove:
            self.enPassant = [move.end[0]-1, move.end[1]] if self.board[move.end[0]][move.end[1]].isWhite() else [move.end[0]+1, move.end[1]]
        else:
            self.enPassant = None
            
    
    def isCellAttacked(self, row, col, whiteTurn):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j].isWhite() != whiteTurn:
                    moves += MoveController().getMoves(self, i, j)
        for move in moves:
            if move.end == [row, col]:
                return True
        return False