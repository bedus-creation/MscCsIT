from SecondSem.CG.Lab_02.src.TurnTest import TurnTest
from SecondSem.CG.Lab_03.src.Sorter import Sorter
import math


class GrahamScan:
    def __init__(self, points):
        self.length = len(points)
        self.points = points

    def getMinYPoint(self):
        index = 0
        minY = self.points[0][1]
        minPoint = self.points[0]
        for i in range(1, self.length):
            if (self.points[i][1] < minY):
                index = i
                minY = self.points[i][1]
                minPoint = self.points[i]
        return minPoint, index

    def getHull(self):
        if (self.length < 3):
            return "Not Possible."
        minPoint, index = self.getMinYPoint()
        self.points.pop(index)
        tmp = ([minPoint]+Sorter().setCenterPoint(
            minPoint).sortPoints(self.points))
        self.points = tmp
        stack = tmp[0:2]
        i = 2
        while i < self.length:
            if len(stack) > 1 and not TurnTest(stack[-2], stack[-1], self.points[i]).isLeft():
                stack.pop()
            else:
                stack.append(self.points[i])
                i += 1
        return stack
