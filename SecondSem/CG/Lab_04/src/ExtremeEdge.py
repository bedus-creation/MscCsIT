from SecondSem.CG.Lab_03.src.Polygon import Polygon
from SecondSem.CG.Lab_03.src.Sorter import Sorter
from SecondSem.CG.Lab_02.src.TurnTest import TurnTest
from SecondSem.CG.Lab_02.src.Collinear import Collinear
from SecondSem.CG.Lab_03.src.Sorter import Sorter


class ExtremeEdge:
    def __init__(self, points):
        self.points = Sorter().sortPoints(points)
        self.n = len(points)
        self.extrementPoint = [1] * self.n

    def getPoints(self):
        tmp = []
        for i in range(self.n):
            if(self.extrementPoint[i] == 1):
                tmp.append(self.points[i])
        # points = Sorter.sortPoints(tmp)
        # return points
        return tmp

    def getHullPoints(self):
        if (self.n < 3):
            return "Not Possible."
        length = self.n

        extreme_edges = []
        for i in range(length):
            pi = self.points[i]
            for j in range(length):
                flag = 1
                if (i != j):
                    pj = self.points[j]
                    for k in range(length):
                        if (i != j and i != k and j != k):
                            pk = self.points[k]
                            turn = TurnTest(pi, pj, pk).getTurn()
                            if not (turn == 0 or turn == 1):
                                flag = 0
                    if (flag == 1):
                        print(f"Extreme Edges: {(i, j)}")
                        extreme_edges.append((i, j))
        temp = []
        for i in range(len(extreme_edges)):
            if (extreme_edges[i][0] not in temp):
                temp.append(extreme_edges[i][0])
            if (extreme_edges[i][1] not in temp):
                temp.append(extreme_edges[i][1])

        extreme_points = []

        for i in range(len(temp)):
            extreme_points.append(self.points[temp[i]])

        self.length = len(extreme_points)
        return extreme_points

    def processAlgo(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    for k in range(self.n):
                        if (i != j and i != k and j != k):
                            turn = TurnTest(
                                self.points[i], self.points[k], self.points[j])
                            collinear = Collinear(
                                self.points[i], self.points[k], self.points[j])
                            if not (turn.isLeft() or collinear.isCollinear()):
                                print(collinear.isCollinear())
                                print(self.points[i],
                                      self.points[k], self.points[j])
                                self.extrementPoint[i] = 0
                                self.extrementPoint[j] = 0
                                # print(self.points[i], self.points[j])

    def getHull(self):
        if (self.n < 3):
            return "Not Possible."
        self.processAlgo()
        return self.getPoints()
