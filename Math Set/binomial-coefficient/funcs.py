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


TestCase = Tuple[Tuple[int, int], int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(0, self.N)
        k = randint(0, n)
        return self.solve(n, k)

    def n_max_k_random(self) -> TestCase:
        n = self.N
        k = randint(0, n)
        return self.solve(n, k)

    def n_k_max(self) -> TestCase:
        n = self.N
        k = n
        return self.solve(n, k)

    def n_max_k_half(self) -> TestCase:
        n = self.N
        k = n // 2
        return self.solve(n, k)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random,
            self.n_max_k_random,
            self.n_max_k_random,
            self.n_max_k_random,
            self.n_max_k_random,
            self.n_k_max,
            self.n_max_k_half,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, k: int) -> TestCase:
        self.validate(n, k)
        numer, denom = 1, 1
        for i in range(1, n + 1):
            numer *= i
            numer %= MOD
        for i in range(1, k + 1):
            denom *= i
            denom %= MOD
        for i in range(1, n - k + 1):
            denom *= i
            denom %= MOD
        ans = numer * pow(denom, MOD - 2, MOD) % MOD
        return (n, k), ans

    def validate(self, n: int, k: int) -> None:
        assert 0 <= k <= n <= self.N
