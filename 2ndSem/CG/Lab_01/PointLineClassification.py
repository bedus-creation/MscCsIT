from Lab_01.Segment import Segment
from Lab_01.Point import Point

class PointLineClassification:
    def __init__(self):
        self.p1, self.p2 = Segment().setPoints()
        self.testPoint = Point().set2DPoint()
        
    def classify(self):
        if (self.p1[0] == self.testPoint[0] & self.p1[1] == self.testPoint[1]):
           print("Test point is start point.")
        elif (self.p2[0] == self.testPoint[0] & self.p2[1] == self.testPoint[1]):
            print("Test point is end point.")
        if (self.p1[1] > self.testPoint[1]):
            print("Test point is beyond line segment.")
        elif (self.p2[1] < self.testPoint[1]):
            print("Test point is behind line segment.")
        elif (self.p1[1] < self.testPoint[1] & self.p2[1] < self.testPoint[1]):
            print("Test point is between the line segment.")

        if self.testPoint[0] > self.p2[0]:
            print("Test Point  is Beyond Line Segment")
        elif self.testPoint[0] < self.p1[0]:
            print("Test Point  is Behind Line Segment")
        elif self.testPoint[0] > self.p1[0] and self.testPoint[0] < self.p2[1]:
            print("Test Point  is between Start and Terminal Point")

        
