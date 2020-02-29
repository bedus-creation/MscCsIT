from SecondSem.CG.Lab_03.src.Polygon import Polygon
from SecondSem.CG.Lab_03.src.RayCasting import RayCasting
import pytest


@pytest.mark.cg_lab03
class TestLab03:

    convexTestData = [
        ([(10, 40), (20, 20), (30, 50), (15, 70)], True),
        ([(18, 60), (15, 40), (50, 25), (18, 10), (50, 20)], True),
        ([(18, 60), (15, 40), (20, 25), (18, 10), (50, 20)], False),
        ([(18, 60), (20, 25), (50, 20), (15, 40), (18, 10)], False)
    ]

    pointInclusionTestData = [
        ([(10, 40), (20, 20), (30, 50), (15, 70)], (20, 40), "Inside"),
        ([(10, 40), (20, 20), (30, 50), (15, 70)], (15, 20), "Outside"),
        ([(18, 60), (15, 40), (50, 25), (18, 10), (50, 20)], (18, 25), "Inside"),
        ([(18, 60), (15, 40), (20, 25), (18, 10), (50, 20)], (18, 25), "NotConvex"),
        ([(18, 60), (20, 25), (50, 20), (15, 40), (18, 10)], (18, 25), "NotConvex")
    ]

    rayCastTestdata = [
        ([(10, 40), (20, 20), (30, 50), (15, 70)], (20, 40), "Inside"),
        ([(10, 40), (20, 20), (30, 50), (15, 70)], (15, 20), "Outside"),
        ([(18, 60), (15, 40), (50, 25), (18, 10), (50, 20)], (18, 25), "Inside")
    ]

    # @pytest.mark.parametrize("points,expected", convexTestData)
    # def test_polygon_is_convex(self, points, expected):
    #     assert Polygon(points).isConvex() == expected

    # @pytest.mark.parametrize("points,query,expected", pointInclusionTestData)
    # def test_polygon__point_inclusion(self, points, query, expected):
    #     assert Polygon(points).isInside(query) == expected

    @pytest.mark.parametrize("points,query,expected", rayCastTestdata)
    def test_ray_casting(self, points, query, expected):
        assert RayCasting(points).isInside(query) == expected
