from SecondSem.CG.Lab_02.src.TurnTest import TurnTest
from SecondSem.CG.Lab_02.src.Collinear import Collinear
from SecondSem.CG.Lab_02.src.Intersection import Intersection

import pytest

@pytest.mark.cg_lab02
class TestLab02:
    leftTestData = [((10, 20), (20, 20), (15, 30), True)]
    rightTestData = [((10, 20), (20, 20), (15, 10), True)]
    collinearTestData = [
        ((2,4),(4,6),(6,8), True)
    ]
    intersectionTestData = [
        ((10, 20), (20, 20), (15, 30), (15, 10), True),
        ((10, 20), (20, 20), (15, 30), (15, 35), False)
    ]

    @pytest.mark.parametrize("p1,p2,p3,expected", collinearTestData)
    def test_collinear_is_perfect(self, p1, p2, p3, expected):
        assert Collinear(p1, p2, p3).isCollinear() == expected

    @pytest.mark.parametrize("p1,p2,tp1,tp2,expected", intersectionTestData)
    def test_line_segment_intersection(self, p1, p2, tp1, tp2, expected):
        assert Intersection(p1, p2, tp1, tp2).isIntersect() == expected

    @pytest.mark.parametrize("p1,p2,testPoint,expected", leftTestData)
    def test_left_turn_is_perfect(self, p1, p2, testPoint, expected):
        assert TurnTest(p1, p2, testPoint).isLeft() == expected

    @pytest.mark.parametrize("p1,p2,testPoint,expected", rightTestData)
    def test_right_turn_is_perfect(self, p1, p2, testPoint, expected):
        assert TurnTest(p1, p2, testPoint).isRight() == expected
