from SecondSem.CG.Lab_02.src.Point import Point
from SecondSem.CG.Lab_02.src.Area import Area


class Between:
    def __init__(self, p1, p2, q):
        self.p1 = Point(p1)
        self.p2 = Point(p2)
        self.q = Point(q)
        self.a = Area(p1, p2, q).calculateArea() == 0

    def isBetween(self):
        x = (max(self.p1.x, self.p2.x) > self.q.x) and (
            min(self.p1.x, self.p2.x) < self.q.x)
        y = (max(self.p1.y, self.p2.y) > self.q.y) and (
            min(self.p1.y, self.p2.y) < self.q.y)
        return (x or y) and self.a
