

class MoveParameters:
    def __init__(self, AggregateHeight: int = 0, CompleteLines: int = 0, Holes: int = 0, Bumpiness: int = 0, VerticalDistance: int = 0, tickTime: int = 1):
        self.AggregateHeight = AggregateHeight
        self.CompleteLines = CompleteLines
        self.Holes = Holes
        self.Bumpiness = Bumpiness
        self.VerticalDistance = VerticalDistance
        self.tickTime = tickTime