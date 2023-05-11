from math import gcd
from random import choices, randint
from typing import List, Tuple

from numba import njit
from sklearn.preprocessing import quantile_transform

from max_divisors import numbers_with_max_n_divisors


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
    while not is_prime(n):
        n -= 1
    return n


@njit
def next_prime(n: int) -> int:
    n += 1
    while not is_prime(n):
        n += 1
    return n


TestCase = List[Tuple[int, int]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, Q: int, N: int) -> None:
        self.Q = Q
        self.N = N
        self.n_divisors = [0] * (N + 1)
        self.precalc()

    def precalc(self) -> None:
        for i in range(1, self.N + 1):
            for multiple in range(i, self.N + 1, i):
                self.n_divisors[multiple] += 1

    def random(self) -> TestCase:
        q = randint(1, self.Q)
        queries = []
        for _ in range(q):
            n = randint(1, self.N)
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def n_min(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            n = 1
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def n_max(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            n = self.N
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def n_max_prime(self) -> TestCase:
        q = self.Q
        queries = []
        n = prev_prime(self.N)
        for _ in range(q):
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def max_number_of_divisors(self) -> TestCase:
        q = self.Q
        queries = []
        ns = sorted(numbers_with_max_n_divisors(self.N))
        for _ in range(q):
            n = ns[randint(0, len(ns) - 1)]
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def n_square(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            n = randint(1, int(self.N**0.5)) ** 2
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def max_twos_power(self) -> TestCase:
        q = self.Q
        queries = []
        n = 1
        while n * 2 <= self.N:
            n *= 2
        for _ in range(q):
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def max_number_of_distinct_primes(self) -> TestCase:
        q = self.Q
        queries = []
        n = 1
        prime = 2
        while n * prime <= self.N:
            n *= prime
            prime = next_prime(prime)
        for _ in range(q):
            ans = self.solve(n)
            queries.append((n, ans))
        self.validate(queries)
        return queries

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.n_min())
        print("n_min done")
        all.append(self.n_max())
        print("n_max done")
        all.append(self.n_max_prime())
        print("n_max_prime done")
        all.append(self.max_number_of_divisors())
        print("max_number_of_divisors done")
        all.append(self.n_square())
        print("n_square done")
        all.append(self.max_twos_power())
        print("max_twos_power done")
        all.append(self.max_number_of_distinct_primes())
        print("max_number_of_distinct_primes done")
        return all

    def solve(self, n: int) -> int:
        return pow(3, self.n_divisors[n] // 2, MOD) * pow(2, self.n_divisors[n] % 2, MOD) % MOD

    def validate(self, queries: TestCase) -> None:
        assert 1 <= len(queries) <= self.Q
        for (n, ans) in queries:
            assert 1 <= n <= self.N
            assert ans % MOD == self.solve(n)
