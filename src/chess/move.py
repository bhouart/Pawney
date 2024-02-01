class Move:
    def __init__(self, start, end, enPassant, doublePawnMove):
        self.start = start
        self.end = end
        self.enPassant = enPassant
        self.doublePawnMove = doublePawnMove
    
    def __str__(self):
        return str(self.end)