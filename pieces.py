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
        return "p" if self.white else "P"

class Rook(Piece):
    
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "r" if self.white else "R"
    
class Knight(Piece):    
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "n" if self.white else "N"
    
class Bishop(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "b" if self.white else "B"

class Queen(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "q" if self.white else "Q"

class King(Piece):
    def __init__(self, isWhite):
        super().__init__(isWhite)
    
    def __str__(self):
        return "k" if self.white else "K"