from Lab_01.Point import Point

class Segment:
    def setPoints(self):
        self.p1 = Point().set2DPoint()
        self.p2 = Point().set2DPoint()
        return self.getPoints()

    def getPoints(self):
        return [self.p1, self.p2]
