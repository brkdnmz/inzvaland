from collections import defaultdict
from math import gcd
from random import choices, randint
from typing import List, Tuple

from max_divisors import numbers_with_max_n_divisors
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
    while not is_prime(n):
        n -= 1
    return n


@njit
def next_prime(n: int) -> int:
    n += 1
    while not is_prime(n):
        n += 1
    return n


def solve(n: int) -> int:
    if n == 1:
        return 1
    ans = 0
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        if i != n:
            ans += solve(i)
        if i * i != n and i != 1:
            ans += solve(n // i)
    return ans


TestCase = Tuple[int, int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N
        self.dp = defaultdict(int)

    def random(self) -> TestCase:
        n = randint(1, self.N)
        return n, self.solve(n)

    def max(self) -> TestCase:
        n = self.N
        return n, self.solve(n)

    def max_2_power(self) -> TestCase:
        n = 1
        while n * 2 <= self.N:
            n *= 2
        return n, self.solve(n)

    def max_n_divisors(self) -> TestCase:
        n = numbers_with_max_n_divisors(self.N)[0]
        return n, self.solve(n)

    def max_n_prime_divisors(self) -> TestCase:
        n = 1
        p = 2
        while n * p <= self.N:
            n *= p
            p = next_prime(p)

        while n * 2 <= self.N:
            n *= 2

        return n, self.solve(n)

    def max_prime(self) -> TestCase:
        n = prev_prime(self.N)
        return n, self.solve(n)

    def only_2_3(self) -> TestCase:
        n = 1
        while n * 6 <= self.N:
            n *= 6
        while n * 2 <= self.N:
            n *= 2
        return n, self.solve(n)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.max())
        print("max done")
        all.append(self.max_2_power())
        print("max_2_power done")
        all.append(self.max_n_divisors())
        print("max_n_divisors done")
        all.append(self.max_n_prime_divisors())
        print("max_n_prime_divisors done")
        all.append(self.max_prime())
        print("max_prime done")
        all.append(self.only_2_3())
        print("only_2_3 done")
        return all

    def solve(self, n: int) -> int:
        if self.dp[n]:
            return self.dp[n]
        if n == 1:
            return 1
        for i in range(1, n + 1):
            if i * i > n:
                break
            if n % i:
                continue
            if i != n:
                self.dp[n] += self.solve(i)
            if i * i != n and i != 1:
                self.dp[n] += self.solve(n // i)
        return self.dp[n]

    def validate(self, n: int) -> None:
        assert 1 <= n <= self.N
