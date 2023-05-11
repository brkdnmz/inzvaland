from typing import Tuple

Point = Tuple[float, float]


def dist(p1: Point, p2: Point):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


coords = list(map(int, input().split()))

ilkkan: Point = (coords[0], coords[1])
yilmaz: Point = (coords[2], coords[3])
ersoy: Point = (coords[4], coords[5])

center: Point = (yilmaz[0] + ersoy[0]) / 2, (yilmaz[1] + ersoy[1]) / 2
radius = dist(yilmaz, ersoy) / 2

print(radius, center, ilkkan)

print(f"{abs(radius - dist(center, ilkkan)):.4f}")
