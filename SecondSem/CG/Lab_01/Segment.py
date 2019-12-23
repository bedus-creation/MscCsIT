from Point import Point
class Segment:
    def __init__(self):
        self.p1 = []
        self.p2 = []
        
    def setPoints(self):
        self.p1 = Point().set2DPoint()
        self.p2 = Point().set2DPoint()
        return self.getPoints()

    def getPoints(self):
        return [self.p1, self.p2]
