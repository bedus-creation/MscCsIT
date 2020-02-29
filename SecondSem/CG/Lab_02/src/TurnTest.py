from SecondSem.CG.Lab_02.src.Area import Area


class TurnTest(Area):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)

    def getTurn(self):
        area = self.calculateArea()
        if area > 0:
            return 1  # left
        elif area < 0:
            return -1  # right
        else:
            return 0  # collinear

    def isRight(self):
        return self.calculateArea() < 0

    def isLeft(self):
        return self.calculateArea() > 0
