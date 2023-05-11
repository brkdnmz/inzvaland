from math import gcd


def is_square(x: int) -> bool:
    sqrt = int(x**0.5)
    while sqrt**2 > x:
        sqrt -= 1
    while (sqrt + 1) ** 2 <= x:
        sqrt += 1
    return sqrt**2 == x


def solve(x: int, y: int) -> str:
    g = gcd(x, y)
    x //= g
    y //= g
    return "Yes" if is_square(x) and is_square(y) else "No"

q = int(input())
while q:
    q -= 1
    x, y = map(int, input().split())
    print(solve(x, y))