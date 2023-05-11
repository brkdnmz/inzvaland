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
MOD = 998244353


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random_small_k(self) -> TestCase:
        n = randint(0, self.N)
        k = randint(0, min(n, 10**6))
        return self.solve(n, k)

    def random_large_k(self) -> TestCase:
        n = self.N
        k = randint(max(0, n - 10**6), n)
        return self.solve(n, k)

    def n_k_max(self) -> TestCase:
        n = self.N
        k = n
        return self.solve(n, k)

    def max_small_k(self) -> TestCase:
        n = self.N
        k = 10**6
        return self.solve(n, k)

    def max_large_k(self) -> TestCase:
        n = self.N
        k = n - 10**6
        return self.solve(n, k)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random_small_k,
            self.random_small_k,
            self.random_small_k,
            self.random_small_k,
            self.random_large_k,
            self.random_large_k,
            self.random_large_k,
            self.random_large_k,
            self.n_k_max,
            self.max_small_k,
            self.max_large_k,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, k: int) -> TestCase:
        self.validate(n, k)
        kk = min(k, n - k)
        numer, denom = 1, 1
        for i in range(kk):
            numer *= n - i
            assert numer % MOD != 0
            numer %= MOD
            denom *= i + 1
            denom %= MOD
        ans = numer * pow(denom, MOD - 2, MOD) % MOD
        return (n, k), ans

    def validate(self, n: int, k: int) -> None:
        assert 0 <= k <= n <= self.N
        assert k <= 10**6 or n - k <= 10**6
