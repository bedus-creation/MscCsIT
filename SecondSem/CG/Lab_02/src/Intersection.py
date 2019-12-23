from SecondSem.CG.Lab_02.src.Area import Area
class Intersection():
    def __init__(self, p1, p2, q1, q2):
        self.a1 = Area(p1, p2, q1).calculateArea()
        self.a2 = Area(p1, p2, q2).calculateArea()

    def isIntersect(self):
        return (self.a1 * self.a2)<0