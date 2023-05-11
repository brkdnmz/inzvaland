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


TestCase = Tuple[Tuple[int, List[Tuple[int, int]]], List[int]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, Q: int, N: int) -> None:
        self.N = N
        self.Q = Q
        self.f = [0] * (N + 1)
        self.invf = [0] * (N + 1)
        self.preprocess()

    def preprocess(self) -> None:
        self.f[0] = 1
        for i in range(1, self.N + 1):
            self.f[i] = self.f[i - 1] * i % MOD
        self.invf[self.N] = pow(self.f[self.N], MOD - 2, MOD)
        for i in range(self.N - 1, -1, -1):
            self.invf[i] = self.invf[i + 1] * (i + 1) % MOD

    def random(self) -> TestCase:
        q = randint(1, self.Q)
        queries = [
            tuple(sorted(choices(range(1, self.N + 1), k=2), reverse=True)) for _ in range(q)
        ]
        return self.solve(q, queries)

    def n_max_k_random(self) -> TestCase:
        n = self.N
        q = self.Q
        queries = [(n, randint(1, n)) for _ in range(q)]
        return self.solve(q, queries)

    def n_k_max(self) -> TestCase:
        n = self.N
        q = self.Q
        queries = [(n, n) for _ in range(q)]
        return self.solve(q, queries)

    def n_max_k_half(self) -> TestCase:
        n = self.N
        q = self.Q
        queries = [(n, n // 2) for _ in range(q)]
        return self.solve(q, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random,
            self.n_max_k_random,
            self.n_k_max,
            self.n_max_k_half,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, q: int, queries: List[Tuple[int, int]]) -> TestCase:
        self.validate(q, queries)
        ans = []
        for (n, k) in queries:
            ans.append(self.f[n] * self.invf[k] % MOD * self.invf[n - k] % MOD)
        return (q, queries), ans

    def validate(self, q: int, queries: List[Tuple[int, int]]) -> None:
        assert 1 <= q <= self.Q
        assert q == len(queries)
        for (n, k) in queries:
            assert 0 <= k <= n <= self.N
