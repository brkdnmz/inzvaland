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

    def random(self) -> TestCase:
        q = randint(1, self.Q)
        queries = [tuple(choices(range(1, self.N + 1), k=2)) for _ in range(q)]
        return self.solve(q, queries)

    def small_gcd(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = randint(1, 100)
            limit = self.N // x
            queries.append([x * randint(1, limit), x * randint(1, limit)])
        return self.solve(q, queries)

    def large_gcd(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = randint(self.N // 10, self.N)
            limit = self.N // x
            queries.append([x * randint(1, limit), x * randint(1, limit)])
        return self.solve(q, queries)

    def coprime(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            a, b = randint(1, self.N), randint(1, self.N)
            while gcd(a, b) > 1:
                a, b = randint(1, self.N), randint(1, self.N)
            queries.append([a, b])
        return self.solve(q, queries)

    def consecutive(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            x = randint(1, self.N - 1)
            queries.append([x, x + 1])
        return self.solve(q, queries)

    def max_ans(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            queries.append([self.N - 1, self.N])
        return self.solve(q, queries)

    def max_limits(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            queries.append([self.N, self.N])
        return self.solve(q, queries)

    def min_limits(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            queries.append([1, 1])
        return self.solve(q, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.small_gcd,
            self.large_gcd,
            self.coprime,
            self.consecutive,
            self.max_ans,
            self.max_limits,
            self.min_limits,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, q: int, queries: List[Tuple[int, int]]) -> TestCase:
        self.validate(q, queries)
        ans = []
        for (a, b) in queries:
            ans.append(a * b // gcd(a, b))
        return (q, queries), ans

    def validate(self, q: int, queries: List[Tuple[int, int]]) -> None:
        assert 1 <= q <= self.Q
        assert q == len(queries)
        for (a, b) in queries:
            assert 1 <= a <= self.N and 1 <= b <= self.N
