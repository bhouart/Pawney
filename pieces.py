from abc import ABC

class Piece(ABC):
    
    def __init__(self, isWhite):
        self.white = isWhite
        
    def isWhite(self):
        return self.white

class EmptyCell(Piece):    
    def __init__(self):
        super().__init__(False)
    
    def __str__(self):
        return "-"

class Pawn(Piece):
    
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "P" if self.white else "p"

class Rook(Piece):
    
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "R" if self.white else "r"
    
class Knight(Piece):    
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "N" if self.white else "n"
    
class Bishop(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "B" if self.white else "b"

class Queen(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "Q" if self.white else "q"

class King(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "K" if self.white else "k"