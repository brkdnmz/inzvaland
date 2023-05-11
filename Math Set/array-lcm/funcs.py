from collections import defaultdict
from math import gcd
from random import choice, choices, randint
from typing import Dict, List, Tuple

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
    def __init__(self, N: int, A: int) -> None:
        self.N = N
        self.A = A
        self.spf = [0] * (A + 1)
        self.preprocess()

    def preprocess(self) -> None:
        for i in range(2, self.A + 1):
            if self.spf[i]:
                continue
            self.spf[i] = i
            for k in range(i * i, self.A + 1, i):
                if not self.spf[k]:
                    self.spf[k] = i

    def random(self) -> TestCase:
        n = randint(1, self.N)
        a = choices(range(1, self.A + 1), k=n)
        return self.solve(n, a)

    def largest_prime(self) -> TestCase:
        n = self.N
        p = prev_prime(self.A)
        a = [p] * n
        return self.solve(n, a)

    def largest_primes(self) -> TestCase:
        n = self.N
        p = prev_prime(self.A)
        a = []
        for _ in range(n):
            a.append(p)
            p = prev_prime(p)
        return self.solve(n, a)

    def power_of_two(self) -> TestCase:
        n = self.N
        x = 1
        while x * 2 <= self.A:
            x *= 2
        a = [x] * n
        return self.solve(n, a)

    def many_primes(self) -> TestCase:
        n = self.N
        p = 2
        a = []
        cur = 1
        for _ in range(n):
            while cur * p <= self.A:
                cur *= p
                p = next_prime(p)
            a.append(cur)
            cur = 1
        return self.solve(n, a)

    def min(self) -> TestCase:
        n = self.N
        a = [1] * n
        return self.solve(n, a)

    def max(self) -> TestCase:
        n = self.N
        a = [self.A] * n
        return self.solve(n, a)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.largest_prime,
            self.largest_primes,
            self.power_of_two,
            self.many_primes,
            self.min,
            self.max,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, a: List[int]) -> TestCase:
        self.validate(n, a)
        exponents: Dict[int, int] = defaultdict(int)
        for x in a:
            while x > 1:
                p = self.spf[x]
                exp = 0
                while x % p == 0:
                    x //= p
                    exp += 1
                exponents[p] = max(exponents[p], exp)
        ans = 1
        for (prime, exp) in exponents.items():
            ans *= pow(prime, exp, MOD)
            ans %= MOD
        return (n, a), ans

    def validate(self, n: int, a: List[int]) -> None:
        assert 1 <= n <= self.N
        assert n == len(a)
        for x in a:
            assert 1 <= x <= self.A
