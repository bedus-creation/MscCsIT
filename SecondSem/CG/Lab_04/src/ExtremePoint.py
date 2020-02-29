from SecondSem.CG.Lab_03.src.Polygon import Polygon
from SecondSem.CG.Lab_03.src.Sorter import Sorter


class ExtremePoint:
    def __init__(self, points):
        self.points = points
        self.n = len(points)
        self.extrementPoint = [1] * self.n

    def getPoints(self):
        tmp = []
        for i in range(self.n):
            if(self.extrementPoint[i] == 1):
                tmp.append(self.points[i])
        points = Sorter().sortPoints(tmp)
        return points

    def processAlgo(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    for k in range(self.n):
                        if (i != j and i != k and j != k):
                            for l in range(self.n):
                                if (i != j and i != k and i != l and j != k and j != l and k != l):
                                    if Polygon([self.points[j], self.points[k], self.points[l]]).isInside(self.points[i]) == "Inside":
                                        self.extrementPoint[i] = 0

    def getHull(self):
        if (self.n < 3):
            return "Not Possible."
        self.processAlgo()
        return self.getPoints()
