from SecondSem.CG.Lab_02.src.TurnTest import TurnTest
from SecondSem.CG.Lab_03.src.LinkList import LinkList

class Polygon:
    def __init__(self, points):
        self.lst = LinkList()
        for point in points:
            self.lst.append(point)

    # Check Polygon is convex
    def isConvex(self):
        first = self.lst.head
        while (first.next is not self.lst.head):
            if TurnTest(first.data, first.next.data, first.next.next.data).isLeft() == False:
                return False
            first = first.next

        if TurnTest(first.data, first.next.data, first.next.next.data).isLeft() == False:
                return False
        return True

    # Check point inclusion
    def checkPointInclusion(self, qPoint):
        first = self.lst.head
        while (first.next is not self.lst.head):
            if TurnTest(qPoint, first.data, first.next.data).isLeft() == False:
                return False
            first = first.next
        if TurnTest(qPoint, first.data, first.next.data).isLeft() == False:
            return False
        return True

