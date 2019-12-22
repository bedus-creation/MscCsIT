class Point:
    def __init__(self):
        self.points = []

    def getPoint(self):
        return self.points
        
    def set3DPoint(self):
        print("Enter 2D point: eg. 2,3,4")
        self.points = tuple(map(int, input().split(',')))
        return self.getPoint()

    def set2DPoint(self):
        print("Enter 2D point: eg. 2,3")
        self.points = tuple(map(int, input().split(',')))
        return self.getPoint()

        
    def displayPoint(self):
        print(self.points)