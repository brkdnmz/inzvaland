from collections import defaultdict
from math import gcd
from random import choice, choices, randint
from typing import List, Tuple

from max_divisors import numbers_with_max_n_divisors
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


TestCase = Tuple[Tuple[int, int], int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        a = randint(1, self.N)
        b = randint(1, self.N)
        return self.solve(a, b)

    def max(self) -> TestCase:
        a = self.N
        b = self.N
        return self.solve(a, b)

    def b_zero(self) -> TestCase:
        a = randint(1, self.N)
        return self.solve(a, 0)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random,
            self.random,
            self.max,
            self.b_zero,
            self.b_zero,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, a: int, b: int) -> TestCase:
        self.validate(a, b)
        return (a, b), pow(a, b, MOD)

    def validate(self, a: int, b: int) -> None:
        assert 1 <= a <= self.N
        assert 0 <= b <= self.N
