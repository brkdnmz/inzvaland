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


TestCase = Tuple[int, int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int) -> None:
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
        return self.solve(n)

    def max(self) -> TestCase:
        n = self.N
        return self.solve(n)

    def max_prime(self) -> TestCase:
        n = prev_prime(self.N)
        return self.solve(n)

    def one_less_than_max_prime(self) -> TestCase:
        n = prev_prime(self.N) - 1
        return self.solve(n)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random,
            self.random,
            self.random,
            self.max,
            self.max_prime,
            self.one_less_than_max_prime,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int) -> TestCase:
        self.validate(n)
        return n, self.n_primes[n]

    def validate(self, n: int) -> None:
        assert 1 <= n <= self.N
