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


TestCase = Tuple[Tuple[int, List[int]], List[Tuple[int, int]]]
MOD = 10**9 + 7
M = 10**9


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(1, self.N)
        a = choices(range(1, M + 1), k=n)
        return self.solve(n, a)

    def random_sorted(self) -> TestCase:
        n = randint(1, self.N)
        a = sorted(choices(range(1, M + 1), k=n))
        return self.solve(n, a)

    def n_max_sorted(self) -> TestCase:
        n = self.N
        a = sorted(choices(range(1, M + 1), k=n))
        return self.solve(n, a)

    def random_reverse_sorted(self) -> TestCase:
        n = randint(1, self.N)
        a = sorted(choices(range(1, M + 1), k=n))
        a.reverse()
        return self.solve(n, a)

    def n_max_reverse_sorted(self) -> TestCase:
        n = self.N
        a = sorted(choices(range(1, M + 1), k=n))
        a.reverse()
        return self.solve(n, a)

    def n_max_same(self) -> TestCase:
        n = self.N
        x = randint(1, M)
        a = [x] * self.N
        return self.solve(n, a)

    def max(self) -> TestCase:
        n = self.N
        a = [M] * n
        return self.solve(n, a)

    def min(self) -> TestCase:
        n = self.N
        a = [1] * n
        return self.solve(n, a)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random_sorted,
            self.n_max_sorted,
            self.random_reverse_sorted,
            self.n_max_reverse_sorted,
            self.n_max_same,
            self.max,
            self.min,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, a: List[int]) -> TestCase:
        self.validate(n, a)
        prefix_max = [0] * n
        suffix_max = [0] * n
        for i in range(n):
            prefix_max[i] = max(prefix_max[i - 1] if i else 0, a[i])
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1] if i + 1 < n else 0, a[i])
        suffix_max.reverse()
        ans: List[Tuple[int, int]] = []
        for i in range(n):
            l_i = bisect_left(prefix_max, a[i], 0, i + 1)
            r_i = bisect_left(suffix_max, a[i], 0, n - i)
            r_i = n - 1 - r_i
            ans.append((l_i, r_i))
        return (n, a), ans

    def validate(self, n: int, a: List[int]) -> None:
        assert 1 <= n <= self.N
        assert len(a) == n
        for x in a:
            assert 1 <= x <= M
