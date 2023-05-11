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


TestCase = Tuple[Tuple[int, List[int]], List[Tuple[int, List[int]]]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, Q: int, N: int) -> None:
        self.N = N
        self.Q = Q
        self.spf = [0] * (N + 1)
        self.preprocess()

    def preprocess(self) -> None:
        for i in range(2, self.N + 1):
            if self.spf[i]:
                continue
            self.spf[i] = i
            for k in range(i * i, self.N + 1, i):
                if not self.spf[k]:
                    self.spf[k] = i

    def random(self) -> TestCase:
        q = randint(1, self.Q)
        queries = choices(range(2, self.N + 1), k=q)
        return self.solve(q, queries)

    def min(self) -> TestCase:
        q = self.Q
        queries = [2] * q
        return self.solve(q, queries)

    def max(self) -> TestCase:
        q = self.Q
        queries = [self.N] * q
        return self.solve(q, queries)

    def consecutive_primes(self) -> TestCase:
        q = self.Q
        x = 1
        p = 2
        while x * p <= self.N:
            x *= p
            p = next_prime(p)
        while x * 2 <= self.N:
            x *= 2
        queries = [x] * q
        return self.solve(q, queries)

    def max_twos_power(self) -> TestCase:
        q = self.Q
        x = 1
        while x * 2 <= self.N:
            x *= 2
        queries = [x] * q
        return self.solve(q, queries)

    def max_prime(self) -> TestCase:
        q = self.Q
        x = prev_prime(self.N)
        queries = [x] * q
        return self.solve(q, queries)

    def large_primes(self) -> TestCase:
        q = self.Q
        x = prev_prime(self.N)
        queries = []
        for _ in range(q):
            queries.append(x)
            x = prev_prime(x)
        return self.solve(q, queries)

    def small_primes(self) -> TestCase:
        q = self.Q
        x = 2
        queries = []
        for _ in range(q):
            queries.append(x)
            x = next_prime(x)
        return self.solve(q, queries)

    def small_consecutive_numbers(self) -> TestCase:
        q = self.Q
        x = 2
        queries = []
        for _ in range(q):
            queries.append(x)
            x += 1
        return self.solve(q, queries)

    def large_consecutive_numbers(self) -> TestCase:
        q = self.Q
        x = self.N
        queries = []
        for _ in range(q):
            queries.append(x)
            x -= 1
        return self.solve(q, queries)

    def max_divisors(self) -> TestCase:
        q = self.Q
        x = numbers_with_max_n_divisors(self.N)[0]
        queries = [x] * q
        return self.solve(q, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.min,
            self.max,
            self.consecutive_primes,
            self.max_twos_power,
            self.max_prime,
            self.large_primes,
            self.small_primes,
            self.small_consecutive_numbers,
            self.large_consecutive_numbers,
            self.max_divisors,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, q: int, queries: List[int]) -> TestCase:
        self.validate(q, queries)
        ans = []
        for x in queries:
            primes = []
            n_divisors = 1
            while x > 1:
                p = self.spf[x]
                exp = 0
                while x % p == 0:
                    x //= p
                    primes.append(p)
                    exp += 1
                n_divisors *= exp + 1
            ans.append((n_divisors, primes))

        return (q, queries), ans

    def validate(self, q: int, queries: List[int]) -> None:
        assert 1 <= q <= self.Q
        assert q == len(queries)
        for x in queries:
            assert 2 <= x <= self.N
