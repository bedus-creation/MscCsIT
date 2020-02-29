from SecondSem.CG.Lab_02.src.TurnTest import TurnTest
from SecondSem.CG.Lab_03.src.LinkList import LinkList
from SecondSem.CG.Lab_02.src.Intersection import Intersection
from SecondSem.CG.Lab_03.src.Sorter import Sorter


class Polygon:
    def __init__(self, points):
        self.lst = LinkList()
        self.points = points
        points = Sorter().sortPoints(points)
        for point in points:
            self.lst.append(point)

    def countCross(self, qPoint):
        count = 0
        first = self.lst.head
        qPointEnd = self.getHighestCoordinate()
        while (first.next is not self.lst.head):
            if Intersection(first.data, first.next.data,
                            qPoint, qPointEnd).isRayIntersect():
                print(first.data, first.next.data,
                      qPoint, qPointEnd)
                count = count + 1
            first = first.next
        return count

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
    def isInside(self, qPoint):
        # print(self.points, qPoint)
        # return "ok"
        if self.isConvex() == False:
            return "NotConvex"
        first = self.lst.head
        while (first.next is not self.lst.head):
            if TurnTest(qPoint, first.data, first.next.data).isLeft() == False:
                return "Outside"
            first = first.next
        if TurnTest(qPoint, first.data, first.next.data).isLeft() == False:
            return "Outside"
        return "Inside"

    def getHighestCoordinate(self):
        first = self.lst.head.next
        y = self.lst.head.data[0]
        if self.lst.head.data[1] > y:
            y = self.lst.head.data[1]
        while (first.next is not self.lst.head):
            if first.data[0] > y:
                y = first.data[0]
            if first.data[0] > y:
                y = first.data[1]
            first = first.next

        if first.data[0] > y:
            y = first.data[0]
        if first.data[1] > y:
            y = first.data[1]

        return (y+10, y+10)
