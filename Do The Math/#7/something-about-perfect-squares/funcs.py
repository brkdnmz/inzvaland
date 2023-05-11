from math import gcd
from random import choices, randint
from typing import List, Tuple

from numba import njit


def is_square(x: int) -> bool:
    sqrt = int(x**0.5)
    while sqrt**2 > x:
        sqrt -= 1
    while (sqrt + 1) ** 2 <= x:
        sqrt += 1
    return sqrt**2 == x


TestCase = List[Tuple[int, int, str]]


class Generator:
    def __init__(self, N: int, Q: int) -> None:
        self.N = N
        self.Q = Q

    def random(self) -> TestCase:
        q = randint(1, self.Q)
        queries = []
        for _ in range(q):
            x = randint(1, self.N)
            y = randint(1, self.N)
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def random_large(self) -> TestCase:
        q = randint(1, self.Q)
        queries = []
        for _ in range(q):
            x = randint(self.N // 2, self.N)
            y = randint(self.N // 2, self.N)
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def random_large_same(self) -> TestCase:
        q = randint(1, self.Q)
        queries = []
        for _ in range(q):
            x = randint(99 * self.N // 100, self.N)
            y = x
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def random_squares(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = randint(1, int(self.N**0.5)) ** 2
            y = randint(1, int(self.N**0.5)) ** 2
            assert self.solve(x, y) == "Yes"
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def random_squares_with_gcd(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = randint(1, int(self.N**0.5)) ** 2
            y = randint(1, int(self.N**0.5)) ** 2
            g = randint(1, self.N // max(x, y))
            x *= g
            y *= g
            assert self.solve(x, y) == "Yes"
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def random_squares_with_large_gcd(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = randint(1, int(self.N**0.3)) ** 2
            y = randint(1, int(self.N**0.3)) ** 2
            g = randint(1, self.N // max(x, y))
            x *= g
            y *= g
            assert self.solve(x, y) == "Yes"
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def max_consecutive_fibo(self) -> TestCase:
        q = self.Q
        queries = []
        x, y = 0, 1
        while x + y <= self.N:
            x, y = y, x + y
        for _ in range(q):
            if randint(0, 1):
                x, y = y, x
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def min(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = 1
            y = 1
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def max(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = self.N
            y = self.N
            queries.append((x, y, self.solve(x, y)))
        self.validate(queries)
        return queries

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.random_large())
        print("random_large done")
        all.append(self.random_large_same())
        print("random_large_same done")
        all.append(self.random_squares())
        print("random_squares done")
        all.append(self.random_squares_with_gcd())
        print("random_squares_with_gcd done")
        all.append(self.random_squares_with_large_gcd())
        print("random_squares_with_large_gcd done")
        all.append(self.max_consecutive_fibo())
        print("max_consecutive_fibo done")
        all.append(self.min())
        print("min done")
        all.append(self.max())
        print("max done")

        return all

    def solve(self, x: int, y: int) -> str:
        g = gcd(x, y)
        x //= g
        y //= g
        return "Yes" if is_square(x) and is_square(y) else "No"

    def validate(self, queries: TestCase) -> None:
        assert 1 <= len(queries) <= self.Q
        for (x, y, ans) in queries:
            assert 1 <= x <= self.N
            assert 1 <= y <= self.N
            assert ans == self.solve(x, y)
