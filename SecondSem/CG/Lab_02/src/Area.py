import numpy as np

class Area:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def calculateArea(self):
        a = np.array([
            [self.p1[0], self.p1[1], 1],
            [self.p2[0], self.p2[1], 1],
            [self.p3[0], self.p3[1], 1]
        ])
        return 0.5 * np.linalg.det(a)