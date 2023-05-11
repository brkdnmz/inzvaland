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


TestCase = Tuple[Tuple[int, List[int]], int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M

    def random(self) -> TestCase:
        n = randint(1, self.N)
        a = choices(range(1, self.M + 1), k=n)
        return self.solve(n, a)

    def n_max_random(self) -> TestCase:
        n = self.N
        a = choices(range(1, self.M + 1), k=n)
        return self.solve(n, a)

    def m_1(self) -> TestCase:
        n = self.N
        a = [1] * n
        return self.solve(n, a)

    def m_max(self) -> TestCase:
        n = self.N
        a = [self.M] * n
        return self.solve(n, a)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (self.random, self.random, self.random, self.n_max_random, self.m_1, self.m_max)

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, a: List[int]) -> TestCase:
        self.validate(n, a)
        dp: Dict[Tuple[int, int], int] = defaultdict(int)
        dp[(0, 1)] = 1
        for x in a:
            ndp = dp.copy()
            for (p, q) in dp:
                # p/q + 1/x
                pp = p * x + q
                qq = q * x
                if pp > qq:
                    continue
                g = gcd(pp, qq)
                pp //= g
                qq //= g
                ndp[(pp, qq)] += dp[(p, q)]
                ndp[(pp, qq)] %= MOD
            dp = ndp
        return (n, a), dp[(1, 1)]

    def validate(self, n: int, a: List[int]) -> None:
        assert 1 <= n <= self.N
        assert len(a) == n
        for x in a:
            assert 1 <= x <= self.M
