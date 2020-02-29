from SecondSem.CG.Lab_03.src.Polygon import Polygon


class RayCasting:
    def __init__(self, points):
        self.points = points
        self._count = 0

    def isInside(self, qPoint):
        count = Polygon(self.points).countCross(qPoint)
        if count % 2 == 0:
            return "Outside"
        return "Inside"
