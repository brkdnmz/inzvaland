from collections import defaultdict
from math import gcd
from random import choice, choices, randint
from typing import List, Tuple

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


TestCase = Tuple[Tuple[int, List[Tuple[int, int]]], List[int]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, Q: int, N: int) -> None:
        self.Q = Q
        self.N = N
        self.n_primes = self.sieve()

    def sieve(self) -> List[int]:
        n_primes = [1] * (self.N + 1)
        n_primes[0] = n_primes[1] = 0
        for i in range(2, self.N + 1):
            n_primes[i] += n_primes[i - 1]
            if n_primes[i] == n_primes[i - 1]:
                continue
            for k in range(i * i, self.N + 1, i):
                n_primes[k] = 0
        return n_primes

    def random(self) -> TestCase:
        n = randint(1, self.N)
        q = randint(1, self.Q)
        queries = [tuple(sorted(choices(range(1, n + 1), k=2))) for _ in range(q)]
        return self.solve(n, q, queries)

    def max_limits_random(self) -> TestCase:
        n = self.N
        q = self.Q
        queries = [tuple(sorted(choices(range(1, n + 1), k=2))) for _ in range(q)]
        return self.solve(n, q, queries)

    def all_max(self) -> TestCase:
        n = self.N
        q = self.Q
        queries = [(1, n) for _ in range(q)]
        return self.solve(n, q, queries)

    def max_limits_l_small_r_big(self) -> TestCase:
        n = self.N
        q = self.Q
        add = min(1000, n // 2)
        assert add <= n - (add - 1)
        queries = [(randint(1, add), randint(n - (add - 1), n)) for _ in range(q)]
        return self.solve(n, q, queries)

    def l_r_equal(self) -> TestCase:
        n = self.N
        q = self.Q
        queries = []
        for _ in range(q):
            x = randint(1, n)
            queries.append((x, x))
        return self.solve(n, q, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.max_limits_random,
            self.max_limits_random,
            self.max_limits_random,
            self.all_max,
            self.max_limits_l_small_r_big,
            self.l_r_equal,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, q: int, queries: List[Tuple[int, int]]) -> TestCase:
        self.validate(n, q, queries)
        ans = [self.n_primes[query[1]] - self.n_primes[query[0] - 1] for query in queries]
        return (q, queries), ans

    def validate(self, n: int, q: int, queries: List[Tuple[int, int]]) -> None:
        assert 1 <= n <= self.N
        assert 1 <= q <= self.Q
        assert q == len(queries)
        for query in queries:
            assert 1 <= query[0] <= query[1] <= n
