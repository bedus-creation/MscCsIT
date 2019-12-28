import math
from SecondSem.CG.Lab_02.src.Point import Point

class Distance:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getDistance(self):
        return math.sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2)
