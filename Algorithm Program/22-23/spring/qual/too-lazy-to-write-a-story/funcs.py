from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict
from math import gcd
from random import choice, choices, randint, sample
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


TestCase = Tuple[Tuple[int, List[int]], int]
MOD = 10**9 + 7
M = 10**9


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(1, self.N)
        a = sample(range(1, M + 1), k=n)
        return self.solve(n, a)

    def random_max(self) -> TestCase:
        n = self.N
        a = sample(range(1, M + 1), k=n)
        return self.solve(n, a)

    def random_sorted(self) -> TestCase:
        n = randint(1, self.N)
        a = sorted(sample(range(1, M + 1), k=n))
        return self.solve(n, a)

    def n_max_sorted(self) -> TestCase:
        n = self.N
        a = sorted(sample(range(1, M + 1), k=n))
        return self.solve(n, a)

    def random_reverse_sorted(self) -> TestCase:
        n = randint(1, self.N)
        a = sorted(sample(range(1, M + 1), k=n))
        a.reverse()
        return self.solve(n, a)

    def n_max_reverse_sorted(self) -> TestCase:
        n = self.N
        a = sorted(sample(range(1, M + 1), k=n))
        a.reverse()
        return self.solve(n, a)

    def max_ans(self) -> TestCase:
        n = self.N
        cur = M
        a = [0] * n
        for i in range(n):
            if i > n - 1 - i:
                break
            a[i] = cur
            cur -= 1
            a[n - 1 - i] = cur
            cur -= 1
        return self.solve(n, a)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random_max,
            self.random_sorted,
            self.n_max_sorted,
            self.random_reverse_sorted,
            self.n_max_reverse_sorted,
            self.max_ans,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, a: List[int]) -> TestCase:
        self.validate(n, a)
        ans = 0
        sorted_a = sorted([(a[i], i) for i in range(n)])
        for i in range(1, n):
            ans += abs(sorted_a[i][1] - sorted_a[i - 1][1])

        return (n, a), ans

    def validate(self, n: int, a: List[int]) -> None:
        assert 1 <= n <= self.N
        assert len(a) == n
        seen = set({})
        for x in a:
            assert 1 <= x <= M
            assert not (x in seen)
            seen.add(x)
