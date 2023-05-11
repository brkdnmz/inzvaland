from collections import defaultdict
from math import gcd
from random import choice, choices, randint
from typing import List, Tuple

from numba import njit


@njit
def is_prime(num: int) -> bool:
    for i in range(2, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


@njit
def prev_prime(n: int) -> int:
    n -= 1
    while not is_prime(n):
        n -= 1
    return n


@njit
def next_prime(n: int) -> int:
    n += 1
    while not is_prime(n):
        n += 1
    return n


TestCase = Tuple[Tuple[int, List[int]], int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int, A: int) -> None:
        self.N = N
        self.A = A

    def random(self) -> TestCase:
        n = randint(1, self.N)
        a = choices(range(self.A + 1), k=n)
        return self.solve(n, a)

    def multiple_of_small(self) -> TestCase:
        n = self.N
        x = randint(1, 100)
        limit = self.A // x
        a = [x * randint(0, limit) for _ in range(n)]
        return self.solve(n, a)

    def multiple_of_large(self) -> TestCase:
        n = self.N
        x = randint(self.A // 1000, self.A)
        limit = self.A // x
        a = [x * randint(0, limit) for _ in range(n)]
        return self.solve(n, a)

    def largest_prime(self) -> TestCase:
        n = self.N
        x = prev_prime(self.A)
        a = [x] * n
        return self.solve(n, a)

    def max(self) -> TestCase:
        n = self.N
        x = self.A
        a = [x] * n
        return self.solve(n, a)

    def min(self) -> TestCase:
        n = self.N
        a = [1] * n
        return self.solve(n, a)

    def all_but_one_zero(self) -> TestCase:
        n = self.N
        a = [0] * n
        a[randint(0, n - 1)] = randint(self.A // 10, self.A)
        return self.solve(n, a)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.multiple_of_small,
            self.multiple_of_small,
            self.multiple_of_small,
            self.multiple_of_large,
            self.multiple_of_large,
            self.multiple_of_large,
            self.largest_prime,
            self.max,
            self.min,
            self.all_but_one_zero,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, a: List[int]) -> TestCase:
        self.validate(n, a)
        ans = 0
        for x in a:
            ans = gcd(ans, x)
        return (n, a), ans

    def validate(self, n: int, a: List[int]) -> None:
        assert 1 <= n <= self.N
        assert n == len(a)
        for x in a:
            assert 0 <= x <= self.A
        assert sum(a) > 0
