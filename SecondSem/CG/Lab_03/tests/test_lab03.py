from SecondSem.CG.Lab_03.src.Polygon import Polygon
import pytest

@pytest.mark.cg_lab03
class TestLab03:

    convexTestData = [
        ([(10, 40), (20, 20), (30, 50), (15, 70)], True),
        ([(18, 60), (15, 40),(20, 25), (10, 10),(50,20)], False)
    ]

    pointInclusionTestData = [
        ([(10, 40), (20, 20), (30, 50), (15, 70)], True),    
    ]

    @pytest.mark.parametrize("points,expected", convexTestData)
    def test_polygon_is_convex(self, points, expected):
        assert Polygon(points).isConvex() == expected

    # @pytest.mark.parametrize("points,expected", pointInclusionTestData)
    # def test_polygon__point_inclusion(self, points, expected):
    #     assert Polygon(points).isConvex() == expected
