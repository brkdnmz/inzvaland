from math import cos, pi, sin
from random import randint
from typing import List, Tuple, Union

from numba import njit


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, p: "Point") -> "Point":
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p: "Point") -> "Point":
        return Point(self.x - p.x, self.y - p.y)

    def __rmul__(self, factor: float) -> "Point":
        return Point(factor * self.x, factor * self.y)

    def __truediv__(self, to_div: float) -> "Point":
        return Point(self.x / to_div, self.y / to_div)

    def dist(self, p: "Point") -> float:
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

    def __eq__(self, p: "Point") -> bool:
        return self.x == p.x and self.y == p.y


class Points:
    def __init__(self, ilkkan: Point, yilmaz: Point, ersoy: Point) -> None:
        self.ilkkan = ilkkan
        self.yilmaz = yilmaz
        self.ersoy = ersoy


def are_collinear(points: "Points") -> bool:
    x_diffs = [points.ilkkan.x - points.yilmaz.x, points.yilmaz.x - points.ersoy.x]
    y_diffs = [points.ilkkan.y - points.yilmaz.y, points.yilmaz.y - points.ersoy.y]
    # x1/y1 == x2/y2
    return x_diffs[0] * y_diffs[1] == x_diffs[1] * y_diffs[0]


def two_same(points: "Points") -> bool:
    return (
        points.ilkkan == points.yilmaz
        or points.yilmaz == points.ersoy
        or points.ilkkan == points.ersoy
    )


TestCase = Tuple[Points, int, float]


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        points = Points(
            ilkkan=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            yilmaz=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            ersoy=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
        )

        alpha = randint(1, 89)

        while two_same(points) or are_collinear(points):
            points = Points(
                ilkkan=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
                yilmaz=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
                ersoy=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            )

        return points, alpha, self.solve(points, alpha)

    def max(self) -> TestCase:
        points = Points(
            ilkkan=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            yilmaz=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            ersoy=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
        )

        alpha = 89

        while two_same(points) or are_collinear(points):
            points = Points(
                ilkkan=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
                yilmaz=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
                ersoy=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            )

        return points, alpha, self.solve(points, alpha)

    def min(self) -> TestCase:
        points = Points(
            ilkkan=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            yilmaz=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            ersoy=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
        )

        alpha = 1

        while two_same(points) or are_collinear(points):
            points = Points(
                ilkkan=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
                yilmaz=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
                ersoy=Point(randint(-self.N, self.N), randint(-self.N, self.N)),
            )

        return points, alpha, self.solve(points, alpha)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        for _ in range(5):
            all.append(self.random())
        for _ in range(5):
            all.append(self.max())
        for _ in range(5):
            all.append(self.min())
        return all

    def solve(self, points: "Points", alpha: int) -> float:
        self.validate(points, alpha)
        segment_center = (points.ilkkan + points.ersoy) / 2
        segment_half_length = points.ilkkan.dist(points.ersoy) / 2

        # 180 deg = pi
        # 1 deg = pi / 180
        radius = segment_half_length / sin(alpha * pi / 180)
        segment_center_to_circle_center_dist = radius * cos(alpha * pi / 180)
        factor = segment_center_to_circle_center_dist / segment_half_length
        vector = segment_center - points.ilkkan
        vector = Point(-vector.y, vector.x)

        circle_centers = [segment_center + factor * vector, segment_center - factor * vector]

        dists = [points.yilmaz.dist(circle_centers[0]), points.yilmaz.dist(circle_centers[1])]
        return min(abs(dists[0] - radius), abs(dists[1] - radius))

    def validate(self, points: "Points", alpha: int) -> None:
        assert abs(points.yilmaz.x) <= 100 and abs(points.yilmaz.y) <= 100
        assert abs(points.ilkkan.x) <= 100 and abs(points.ilkkan.y) <= 100
        assert abs(points.ersoy.x) <= 100 and abs(points.ersoy.y) <= 100
        assert not are_collinear(points) and not two_same(points)
        assert 0 < alpha < 90
