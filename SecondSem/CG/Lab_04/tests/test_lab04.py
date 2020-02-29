from SecondSem.CG.Lab_04.src.ExtremePoint import ExtremePoint
from SecondSem.CG.Lab_04.src.ExtremeEdge import ExtremeEdge
from SecondSem.CG.Lab_04.src.GiftWrap2D import GiftWrap2D
from SecondSem.CG.Lab_04.src.GrahamScan import GrahamScan
import pytest


@pytest.mark.cg_lab04
class TestLab04:

    convexHullData = [
        (
            # Input points
            [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)],
            # Output points
            [(0, 0), (3, 1), (4, 4), (0, 3)]
        ),
        (
            # Input points
            [(0, 3), (1, 1)],
            # Output points
            "Not Possible."
        ),

        (
            # Input points
            [(2, 2), (10, 2), (10, 10), (5, 5), (2, 10), (7, 5)],
            # Output points
            [(2, 2), (10, 2), (10, 10), (2, 10)]
        )
    ]
    @pytest.mark.parametrize("points,expected", convexHullData)
    def test_convex_hull_using_extreme_edges(self, points, expected):
        assert expected == ExtremeEdge(points).getHullPoints()

    @pytest.mark.parametrize("points,expected", convexHullData)
    def test_convex_hull_using_giftwrap2d(self, points, expected):
        assert expected == GiftWrap2D(points).getHull()

    @pytest.mark.parametrize("points,expected", convexHullData)
    def test_convex_hull_using_extreme_points(self, points, expected):
        assert expected == ExtremePoint(points).getHull()

    @pytest.mark.parametrize("points,expected", convexHullData)
    def test_convex_hull_using_graham_scan(self, points, expected):
        assert expected == GrahamScan(points).getHull()
