from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict
from math import gcd
from random import choice, choices, randint
from typing import Dict, List, Tuple, Type

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


TestCase = Tuple[Tuple[int, List[Tuple[int, int, int]]], List[int]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int, Q: int) -> None:
        self.N = N
        self.Q = Q
        self.dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
        self.dp[0][0][0] = 1

    def random(self) -> TestCase:
        q = self.Q
        triplets = [tuple(choices(range(0, self.N + 1), k=3)) for _ in range(q)]
        return self.solve(q, triplets)

    def small(self) -> TestCase:
        q = self.Q
        triplets = [tuple(choices(range(0, min(self.N, 30) + 1), k=3)) for _ in range(q)]
        return self.solve(q, triplets)

    def large(self) -> TestCase:
        q = self.Q
        triplets = [tuple(choices(range(max(0, self.N - 75), self.N + 1), k=3)) for _ in range(q)]
        return self.solve(q, triplets)

    def max(self) -> TestCase:
        q = self.Q
        triplets = [(self.N, self.N, self.N) for _ in range(q)]
        return self.solve(q, triplets)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (self.random, self.small, self.large, self.max)

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, q: int, triplets: List[Tuple[int, int, int]]) -> TestCase:
        self.validate(q, triplets)
        ans = []
        for t in triplets:
            ans.append(self.rec(t[0], t[1], t[2]))
        return (q, triplets), ans

    def rec(self, a: int, b: int, c: int) -> int:
        if ~self.dp[a][b][c]:
            return self.dp[a][b][c]
        factor = lambda a, b, c: 1 + (a + b + c > 0)
        ans = 0
        if a:
            ans += factor(a - 1, b, c) * self.rec(a - 1, b, c)
        if b:
            ans += factor(a, b - 1, c) * self.rec(a, b - 1, c)
        if c:
            ans += factor(a, b, c - 1) * self.rec(a, b, c - 1)
        if a and b:
            ans -= factor(a - 1, b - 1, c) * self.rec(a - 1, b - 1, c)
        if a and c:
            ans -= factor(a - 1, b, c - 1) * self.rec(a - 1, b, c - 1)
        if b and c:
            ans -= factor(a, b - 1, c - 1) * self.rec(a, b - 1, c - 1)
        if a and b and c:
            ans += factor(a - 1, b - 1, c - 1) * self.rec(a - 1, b - 1, c - 1)
        self.dp[a][b][c] = ans % MOD
        return self.dp[a][b][c]

    def validate(self, q: int, triplets: List[Tuple[int, int, int]]) -> None:
        assert 1 <= q <= self.Q
        assert len(triplets) == q
        for t in triplets:
            assert 0 <= t[0] <= self.N
            assert 0 <= t[1] <= self.N
            assert 0 <= t[2] <= self.N
