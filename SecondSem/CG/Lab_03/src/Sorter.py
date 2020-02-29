import math


class Sorter:
    def setCenterPoint(self, center):
        self.center = center
        return self

    def getCenterPoint(self, points):
        x, y = zip(*points)
        l = len(x)
        self.center = (sum(x) / l, sum(y) / l)

    def sortPoints(self, points):
        self.getCenterPoint(points)
        xy_sorted = sorted(
            points, key=lambda point: math.atan2((point[1]-self.center[1]), (point[0]-self.center[0])))
        return xy_sorted
