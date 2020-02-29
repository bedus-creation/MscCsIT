from SecondSem.CG.Lab_03.src.Sorter import Sorter
import math


class GiftWrap2D:
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

    def calculateAngle(self, point, center):
        y = (point[1]-center[1])
        x = (point[0]-center[0])
        angle = math.atan2(y, x)
        if(angle < 0):
            angle += 2 * math.pi
        # if(x == 0 and y == 0):
        #     return 7888
        # if (x == 0 and y > 0):
        #     angle = angle + math.pi/2
        # elif (x == 0 and y < 0):
        #     angle -= math.pi/2
        # elif(x < 0 and y >= 0):
        #     angle += 2 * math.pi
        # elif(x < 0 and y < 0):
        #     angle -= 2 * math.pi
        print(center, point,  x, y, angle)
        return angle

    def getMinSlopePoint(self, center, points):
        return sorted(
            points, key=lambda point: self.calculateAngle(point, center))

    def getHull(self):
        # exit(self.getMinSlopePoint((0, 3),
        #                            [(0, 3), (3, 3), (4, 4), (0, 0), (1, 1), (1, 2), (3, 1), (2, 2)]))
        if (self.length < 3):
            return "Not Possible."
        minPoint, index = self.getMinYPoint()
        vertices = [minPoint]
        points = self.points.copy()
        points.pop(index)
        i = 1
        while i < len(self.points):
            points = self.getMinSlopePoint(minPoint, self.points)
            print(points, minPoint)
            if points[1] != minPoint:
                minPoint = points[1]
                points.pop(0)
                vertices.append(minPoint)
            else:
                break
            i += 1
        return vertices[0:4]
