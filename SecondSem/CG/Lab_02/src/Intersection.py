from SecondSem.CG.Lab_02.src.Area import Area
from SecondSem.CG.Lab_02.src.Point import Point
from SecondSem.CG.Lab_02.src.Between import Between
from SecondSem.CG.Lab_02.src.TurnTest import TurnTest


class Intersection():
    def __init__(self, p1, p2, q1, q2):
        self.p1 = p1
        self.p2 = p2
        self.q1 = q1
        self.q2 = q2
        self.a1 = Area(p1, p2, q1).calculateArea()
        self.a2 = Area(p1, p2, q2).calculateArea()

    def isRayIntersect(self):
        if (
                (TurnTest(self.p1, self.p2, self.q1).getTurn() is 0 and Between(self.p1, self.p2, self.q1).isBetween()) or
                (TurnTest(self.p1, self.p2, self.q2).getTurn() is 0 and Between(self.p1, self.p2, self.q2).isBetween()) or
                (TurnTest(self.q1, self.q2, self.p1).getTurn() is 0 and Between(self.q1, self.q2, self.p1).isBetween()) or
                (TurnTest(self.q1, self.q2, self.p2).getTurn()
                 is 0 and Between(self.q1, self.q2, self.p2).isBetween())
        ):
            return True
        if (
                (TurnTest(self.p1, self.p2, self.q1).getTurn() != TurnTest(self.p1, self.p2, self.q2).getTurn()) and
                (TurnTest(self.q1, self.q2, self.p1).getTurn() !=
                 TurnTest(self.q1, self.q2, self.p2).getTurn())
        ):
            return 1
        else:
            return 0

    def isIntersect(self):
        return (self.a1 * self.a2) < 0

    def isImproper(self):
        if Between(self.p1, self.p2, self.q1).isBetween() or Between(self.p1, self.p2, self.q2).isBetween():
            return True
        return False
