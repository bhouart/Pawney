from pieces import *
from move import Move

class MoveController():
    
    def __init__(self):
        pass
    
    def getMoves(self, board, row, col, enPassant):
        piece = board[row][col]
        if isinstance(piece, EmptyCell):
            return []
        elif isinstance(piece, Pawn):
            return self.getPawnMoves(board, row, col, enPassant)
        elif isinstance(piece, Rook):
            return self.getRookMoves(board, row, col)
        elif isinstance(piece, Knight):
            return self.getKnightMoves(board, row, col)
        elif isinstance(piece, Bishop):
            return self.getBishopMoves(board, row, col)
        elif isinstance(piece, Queen):
            return self.getQueenMoves(board, row, col)
        elif isinstance(piece, King):
            return self.getKingMoves(board, row, col)
    
    def getPawnMoves(self, board, row, col, enPassant):
        piece = board[row][col]
        moves = []
        if piece.isWhite():
            if row < 7:
                if isinstance(board[row+1][col], EmptyCell):    # moves forward
                    moves.append(Move((row, col), (row+1, col), None, False))
                    if row == 1 and isinstance(board[row+2][col], EmptyCell):   # moves two squares forward
                        moves.append(Move((row, col), (row+2, col), None, True))
                if col > 0 and not isinstance(board[row+1][col-1], EmptyCell) and not board[row+1][col-1].isWhite():    # captures left
                    moves.append(Move((row, col), (row+1, col-1), None, False))
                if col < 7 and not isinstance(board[row+1][col+1], EmptyCell) and not board[row+1][col+1].isWhite():   # captures right
                    moves.append(Move((row, col), (row+1, col+1), None, False))
                
                # check en passant
                if row == 4 and col > 0 and isinstance(board[row][col-1], Pawn) and not board[row][col-1].isWhite() and [row+1, col-1] == enPassant:
                    moves.append(Move((row, col), (row+1, col-1), (row, col-1), False))
                if row == 4 and col < 7 and isinstance(board[row][col+1], Pawn) and not board[row][col+1].isWhite() and [row+1, col+1] == enPassant:
                    moves.append(Move((row, col), (row+1, col+1), (row, col+1), False))
        else:
            if row > 0:
                if isinstance(board[row-1][col], EmptyCell):   # moves forward
                    moves.append(Move((row, col), (row-1, col), None, False))
                    if row == 6 and isinstance(board[row-2][col], EmptyCell):   # moves two squares forward
                        moves.append(Move((row, col), (row-2, col), None, True))
                if col > 0 and not isinstance(board[row-1][col-1], EmptyCell) and board[row-1][col-1].isWhite():
                    moves.append(Move((row, col), (row-1, col-1), None, False))
                if col < 7 and not isinstance(board[row-1][col+1], EmptyCell) and board[row-1][col+1].isWhite():
                    moves.append(Move((row, col), (row-1, col+1), None, False))
                
                # check en passant
                if row == 3 and col > 0 and isinstance(board[row][col-1], Pawn) and board[row][col-1].isWhite() and [row-1, col-1] == enPassant:
                    moves.append(Move((row, col), (row-1, col-1), (row, col-1), False))
                if row == 3 and col < 7 and isinstance(board[row][col+1], Pawn) and board[row][col+1].isWhite() and [row-1, col+1] == enPassant:
                    moves.append(Move((row, col), (row-1, col+1), (row, col+1), False))
                  
        
          
        # TODO : handle promotion for South African chess
        return moves