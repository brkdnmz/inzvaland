from collections import defaultdict
from math import gcd
from random import choice, choices, randint
from typing import List, Tuple

from max_divisors import numbers_with_max_n_divisors
from numba import njit
from sklearn import naive_bayes


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


TestCase = Tuple[int, int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(1, self.N)
        return self.solve(n)

    def max(self) -> TestCase:
        n = self.N
        return self.solve(n)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random,
            self.random,
            self.random,
            self.max,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int) -> TestCase:
        self.validate(n)
        ans = 1
        for i in range(1, n + 1):
            ans *= i
            ans %= MOD
        return n, ans

    def validate(self, n: int) -> None:
        assert 0 <= n <= self.N
