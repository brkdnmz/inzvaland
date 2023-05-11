from math import gcd
from random import randint
from typing import List, Tuple

from numba import njit

TestCase = Tuple[int, int, int]


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        a = randint(1, self.N)
        b = randint(1, self.N)
        return a, b, self.solve(a, b)

    def random_multiple(self) -> TestCase:
        k = randint(1, self.N)
        a = k * randint(1, self.N // k)
        b = k * randint(1, self.N // k)
        return a, b, self.solve(a, b)

    def random_adjacent(self) -> TestCase:
        a = randint(1, self.N - 1)
        b = a + 1
        return a, b, self.solve(a, b)

    def equal(self) -> TestCase:
        a = randint(1, self.N)
        b = a
        return a, b, self.solve(a, b)

    def consecutive_fibo(self) -> TestCase:
        a, b = 1, 1
        while a + b <= self.N:
            a, b = b, a + b
        return a, b, self.solve(a, b)

    def max(self) -> TestCase:
        a = self.N
        b = a
        return a, b, self.solve(a, b)

    def max_adjacent(self) -> TestCase:
        a = self.N - 1
        b = a + 1
        return a, b, self.solve(a, b)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        for _ in range(3):
            all.append(self.random())
        for _ in range(3):
            all.append(self.random_multiple())
        for _ in range(3):
            all.append(self.random_adjacent())
        for _ in range(3):
            all.append(self.equal())
        all.append(self.consecutive_fibo())
        all.append(self.max())
        all.append(self.max_adjacent())

        return all

    def solve(self, a: int, b: int) -> int:
        self.validate(a, b)
        ans = max(a, b) // gcd(a, b)
        return ans

    def validate(self, a: int, b: int) -> None:
        assert 1 <= a <= self.N and 1 <= b <= self.N
