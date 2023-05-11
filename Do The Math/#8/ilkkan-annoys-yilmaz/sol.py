from math import cos, pi, sin


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


def solve(ilkkan: Point, yilmaz: Point, ersoy: Point, alpha: int) -> float:
    segment_center = (ilkkan + ersoy) / 2
    segment_half_length = ilkkan.dist(ersoy) / 2

    # 180 deg = pi
    # 1 deg = pi / 180
    radius = segment_half_length / sin(alpha * pi / 180)
    segment_center_to_circle_center_dist = radius * cos(alpha * pi / 180)
    factor = segment_center_to_circle_center_dist / segment_half_length
    vector = segment_center - ilkkan
    vector = Point(-vector.y, vector.x)

    circle_centers = [segment_center + factor * vector, segment_center - factor * vector]

    dists = [yilmaz.dist(circle_centers[0]), yilmaz.dist(circle_centers[1])]
    return min(abs(dists[0] - radius), abs(dists[1] - radius))


coords = list(map(int, input().split()))
alpha = int(input())

ilkkan = Point(coords[0], coords[1])
yilmaz = Point(coords[2], coords[3])
ersoy = Point(coords[4], coords[5])


print(f"{solve(ilkkan, yilmaz, ersoy, alpha):.4f}")
