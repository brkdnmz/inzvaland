from random import randint
from typing import List, Tuple

from numba import njit

Point = Tuple[float, float]
TestCase = Tuple[Point, Point, Point, float]


def dist(p1: Point, p2: Point):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        ilkkan = (randint(-self.N, self.N), randint(-self.N, self.N))
        yilmaz = (randint(-self.N, self.N), randint(-self.N, self.N))
        ersoy = (randint(-self.N, self.N), randint(-self.N, self.N))
        while self.two_same(ilkkan, yilmaz, ersoy) or self.are_collinear(ilkkan, yilmaz, ersoy):
            ilkkan = (randint(-self.N, self.N), randint(-self.N, self.N))
            yilmaz = (randint(-self.N, self.N), randint(-self.N, self.N))
            ersoy = (randint(-self.N, self.N), randint(-self.N, self.N))

        return ilkkan, yilmaz, ersoy, self.solve(ilkkan, yilmaz, ersoy)

    def max(self) -> TestCase:
        ilkkan = (self.N, -self.N)
        yilmaz = (self.N, self.N)
        ersoy = (-self.N, self.N)

        return ilkkan, yilmaz, ersoy, self.solve(ilkkan, yilmaz, ersoy)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        for i in range(5):
            all.append(self.random())
            print(f"random {i}/{4} done")

        all.append(self.max())
        print("max done")
        return all

    def solve(self, ilkkan: Point, yilmaz: Point, ersoy: Point) -> float:
        self.validate(ilkkan, yilmaz, ersoy)
        center = ((yilmaz[0] + ersoy[0]) / 2, (yilmaz[1] + ersoy[1]) / 2)
        radius = dist(yilmaz, ersoy) / 2
        distance = dist(center, ilkkan)
        ans = abs(radius - distance)
        return ans

    def are_collinear(self, ilkkan: Point, yilmaz: Point, ersoy: Point) -> bool:
        x_diffs = [ilkkan[0] - yilmaz[0], yilmaz[0] - ersoy[0]]
        y_diffs = [ilkkan[1] - yilmaz[1], yilmaz[1] - ersoy[1]]
        # x1/y1 == x2/y2
        return x_diffs[0] * y_diffs[1] == x_diffs[1] * y_diffs[0]

    def two_same(self, ilkkan: Point, yilmaz: Point, ersoy: Point) -> bool:
        return ilkkan == yilmaz or yilmaz == ersoy or ilkkan == ersoy

    def validate(self, ilkkan: Point, yilmaz: Point, ersoy: Point) -> None:
        for point in [ilkkan, yilmaz, ersoy]:
            assert abs(point[0]) <= 100 and abs(point[1]) <= 100
        assert not self.are_collinear(ilkkan, yilmaz, ersoy) and not self.two_same(
            ilkkan, yilmaz, ersoy
        )
