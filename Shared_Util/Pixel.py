from Shared_Util.Colors import Colors

class Pixel:
    def __init__(self,
                 filled: bool = False,
                 color: Colors = Colors.I):
        self.filled = filled
        self.color = color