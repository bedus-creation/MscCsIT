from SecondSem.CG.Lab_02.src.Area import Area
class TurnTest(Area):
    def __init__(self, p1, p2, p3):
        super().__init__(p1,p2,p3)

    def isRight(self):
        return self.calculateArea()<0

    def isLeft(self):
        return self.calculateArea() > 0
