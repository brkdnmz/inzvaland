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
    while not is_prime(n):
        n -= 1
    return n


@njit
def next_prime(n: int) -> int:
    n += 1
    while not is_prime(n):
        n += 1
    return n


TestCase = Tuple[str, int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N_digits: int) -> None:
        self.N_digits = N_digits

    def random(self) -> TestCase:
        digits_before = randint(0, 99)
        digits_after = randint(0, 10**self.N_digits - 1)

        n = f"{digits_before}.{digits_after}"
        return self.solve(n)

    def padded_random(self) -> TestCase:
        digits_before = randint(0, 99)
        digits_after = randint(0, 10**self.N_digits - 1)

        n = f"{digits_before}.{'0' * (self.N_digits - len(str(digits_after)))}{digits_after}"
        return self.solve(n)

    def max(self) -> TestCase:
        digits_before = 99
        digits_after = 10**self.N_digits - 1

        n = f"{digits_before}.{digits_after}"
        return self.solve(n)

    def max_2_power(self) -> TestCase:
        n_int = 1
        while n_int * 2 < 10 ** (2 + self.N_digits):
            n_int *= 2
        n = f"{n_int // 10**self.N_digits}.{n_int % 10**self.N_digits}"
        return self.solve(n)

    def max_5_power(self) -> TestCase:
        n_int = 1
        while n_int * 5 < 10 ** (2 + self.N_digits):
            n_int *= 5
        n = f"{n_int // 10**self.N_digits}.{n_int % 10**self.N_digits}"
        return self.solve(n)

    def min(self) -> TestCase:
        n = f"0.{'0' * (self.N_digits - 1)}1"
        return self.solve(n)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.padded_random())
        print("padded_random done")
        all.append(self.max())
        print("max done")
        all.append(self.max_2_power())
        print("max_2_power done")
        all.append(self.max_5_power())
        print("max_5_power done")
        all.append(self.min())
        print("min done")
        return all

    def solve(self, n: str) -> TestCase:
        self.validate(n)
        exp = 2
        seen_dot = False
        n_int = 0
        for c in n:
            if c == ".":
                seen_dot = True
                continue
            exp += seen_dot
            digit = ord(c) - ord("0")
            n_int = 10 * n_int + digit
        return n, n_int // gcd(n_int, 10**exp)

    def validate(self, n: str) -> None:
        dot_place = n.find(".")
        assert (
            dot_place != -1 and len(n[(dot_place + 1) :]) <= self.N_digits
        ), f"{n} {n[(dot_place + 1) :]}"
        assert float(n) > 0
