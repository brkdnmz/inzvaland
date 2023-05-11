from collections import defaultdict
from math import gcd
from random import choice, choices, randint, sample
from typing import List, Tuple

from numba import njit

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


def calc_number_of_multiples(n: int, overall_gcd: int) -> int:
    return (n - 1) // overall_gcd - 1 // overall_gcd


TestCase = Tuple[Tuple[int, int, List[int]], int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M

    def random(self) -> TestCase:
        n = randint(1, self.N)
        m = randint(1, min(n - 2, self.M))
        lines = sorted(sample(range(2, n), m))
        return self.solve(n, m, lines)

    def all_max(self) -> TestCase:
        n = self.N
        m = self.M
        lines = sorted(sample(range(2, n), m))
        return self.solve(n, m, lines)

    def gcd_small(self) -> TestCase:
        g = randint(2, self.N // 10**4)
        n = g * (self.N // g) - 1
        n_multiples = calc_number_of_multiples(n, g)
        m = randint(1, min(n_multiples, self.M))
        lines = sorted(sample(range(g, n, g), m))
        return self.solve(n, m, lines)

    def gcd_large(self) -> TestCase:
        g = randint(2, self.N // 2)
        n = g * (self.N // g) - 1
        n_multiples = calc_number_of_multiples(n, g)
        m = randint(1, min(n_multiples, self.M))
        lines = sorted(sample(range(g, n, g), m))
        return self.solve(n, m, lines)

    def single_rule_middle(self) -> TestCase:
        n = self.N - 1
        m = 1
        lines = [(n + 1) // 2]
        return self.solve(n, m, lines)

    def max_n_divisors(self) -> TestCase:
        n = numbers_with_max_n_divisors(self.N)[0] - 1
        m = 1
        lines = [(n + 1) // 2]
        return self.solve(n, m, lines)

    def prime(self) -> TestCase:
        g = prev_prime(randint(3, self.N // 2))
        n = g * randint(2, self.N // g) - 1
        n_multiples = calc_number_of_multiples(n, g)
        m = min(n_multiples, self.M)
        lines = sorted(sample(range(g, n, g), m))
        return self.solve(n, m, lines)

    def max_prime(self) -> TestCase:
        g = prev_prime(self.N // 2)
        n = g * 2 - 1
        m = 1
        lines = [g]
        return self.solve(n, m, lines)

    def large_difference(self) -> TestCase:
        n = self.N
        m = 2
        lines = [randint(2, 10**3), randint(10**3 + 1, n - 1)]
        return self.solve(n, m, lines)

    def max_difference(self) -> TestCase:
        n = self.N
        m = 2
        lines = [2, n - 1]
        return self.solve(n, m, lines)

    def square(self) -> TestCase:
        g = randint(1, int((self.N // 2) ** 0.5)) ** 2
        n = g * randint(2, self.N // g) - 1
        n_multiples = calc_number_of_multiples(n, g)
        m = randint(1, min(n_multiples, self.M))
        lines = sorted(sample(range(g, n, g), m))
        return self.solve(n, m, lines)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.all_max,
            self.gcd_small,
            self.gcd_large,
            self.single_rule_middle,
            self.max_n_divisors,
            self.prime,
            self.max_prime,
            self.large_difference,
            self.max_difference,
            self.square,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, m: int, lines: List[int]) -> TestCase:
        self.validate(n, m, lines)
        overall_gcd = n + 1
        for line in lines:
            overall_gcd = gcd(overall_gcd, line)
        ans = -1  # exclude divisor = overall_gcd
        for i in range(1, overall_gcd + 1):
            if i * i > overall_gcd:
                break
            if overall_gcd % i:
                continue
            ans += 1 + (i * i != overall_gcd)
        return (n, m, lines), ans

    def validate(self, n: int, m: int, lines: List[int]) -> None:
        assert 1 <= n <= self.N
        assert 1 <= m <= min(n - 2, self.M)
        assert len(lines) == m
        for i in range(m):
            assert lines[i] > (lines[i - 1] if i else 1)
        assert n > lines[-1]
