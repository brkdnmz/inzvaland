from collections import defaultdict
from math import gcd
from random import choice, choices, randint
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


TestCase = Tuple[int, int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(3, self.N)
        ans = self.solve(n)
        return n, ans

    def n_max(self) -> TestCase:
        n = self.N
        ans = self.solve(n)
        return n, ans

    def n_max_prime(self) -> TestCase:
        n = prev_prime(self.N)
        ans = self.solve(n)
        return n, ans

    def max_number_of_divisors(self) -> TestCase:
        ns = sorted(numbers_with_max_n_divisors(self.N))
        n = choice(ns)
        ans = self.solve(n)
        return n, ans

    def n_square(self) -> TestCase:
        n = choice(sorted(map(lambda x: x**2, numbers_with_max_n_divisors(int(self.N**0.5)))))
        ans = self.solve(n)
        return n, ans

    def max_twos_power(self) -> TestCase:
        n = 1
        while n * 2 <= self.N:
            n *= 2
        ans = self.solve(n)
        return n, ans

    def max_number_of_distinct_primes(self) -> TestCase:
        n = 1
        prime = 2
        while n * prime <= self.N:
            n *= prime
            prime = next_prime(prime)
        ans = self.solve(n)
        return n, ans

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
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
        return (pow(2, n, MOD) - 1 - n - n * (n - 1) // 2) % MOD

    def validate(self, n: int) -> None:
        assert 3 <= n <= self.N
