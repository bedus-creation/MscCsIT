from SecondSem.CG.Lab_02.src.Area import Area
from SecondSem.CG.Lab_02.src.Point import Point
from SecondSem.CG.Lab_02.src.Between import Between


class Intersection():
    def __init__(self, p1, p2, q1, q2):
        self.p1 = p1
        self.p2 = p2
        self.q1 = q1
        self.q2 = q2
        self.a1 = Area(p1, p2, q1).calculateArea()
        self.a2 = Area(p1, p2, q2).calculateArea()

    def isIntersect(self):
        return (self.a1 * self.a2) < 0

    def isImproper(self):
        if Between(self.p1, self.p2, self.q1).isBetween() or Between(self.p1, self.p2, self.q2).isBetween():
            return True
        return False