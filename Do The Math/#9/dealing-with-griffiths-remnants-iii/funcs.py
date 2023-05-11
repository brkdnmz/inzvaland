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
        pw10 = 10 ** (self.N_digits - len(str(digits_before)))
        digits_after = randint(0, pw10 - 1)

        n = f"{digits_before}.{digits_after}"
        return self.solve(n)

    def padded_random(self) -> TestCase:
        digits_before = randint(0, 99)
        pw10 = 10 ** (self.N_digits - len(str(digits_before)))
        digits_after = randint(0, pw10 - 1)

        n = f"{digits_before}.{'0' * (self.N_digits - len(str(digits_before)) - len(str(digits_after)))}{digits_after}"
        return self.solve(n)

    def random_many_digits(self) -> TestCase:
        n = f"0.{10**self.N_digits - randint(0, 100)}"
        return self.solve(n)

    def max(self) -> TestCase:
        digits_before = 99
        digits_after = 10 ** (self.N_digits - 2) - 1

        n = f"{digits_before}.{digits_after}"
        return self.solve(n)

    def max_100(self) -> TestCase:
        n = f"100.{'0' * (self.N_digits - 3)}"
        return self.solve(n)

    def max_1(self) -> TestCase:
        n = f"1.{'0' * (self.N_digits - 1)}"
        return self.solve(n)

    def max_2_power(self) -> TestCase:
        n_int = 1
        while n_int * 2 < 10**self.N_digits:
            n_int *= 2
        n = f"{n_int // 10**(self.N_digits - 2)}.{n_int % 10**(self.N_digits - 2)}"
        return self.solve(n)

    def max_2_power_first_digit_0(self) -> TestCase:
        n_int = 1
        while n_int * 2 < 10**self.N_digits:
            n_int *= 2
        n = f"0.{n_int}"
        return self.solve(n)

    def max_5_power(self) -> TestCase:
        n_int = 1
        while n_int * 5 < 10**self.N_digits:
            n_int *= 5
        n = f"{n_int // 10**(self.N_digits - 2)}.{n_int % 10**(self.N_digits - 2)}"
        return self.solve(n)

    def max_5_power_first_digit_0(self) -> TestCase:
        n_int = 1
        while n_int * 5 < 10**self.N_digits:
            n_int *= 5
        n = f"0.{n_int}"
        return self.solve(n)

    def mixed_2_5(self) -> TestCase:
        n_int = 1
        cur = choice([2, 5])
        while n_int * cur < 10**self.N_digits:
            n_int *= cur
            cur = choice([2, 5])
        n = f"0.{n_int}"
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
        for _ in range(3):
            all.append(self.random_many_digits())
            print("random_many_digits done")
        all.append(self.max())
        print("max done")
        all.append(self.max_100())
        print("max_100 done")
        all.append(self.max_1())
        print("max_1 done")
        all.append(self.max_2_power())
        print("max_2_power done")
        all.append(self.max_2_power_first_digit_0())
        print("max_2_power_first_digit_0 done")
        all.append(self.max_5_power())
        print("max_5_power done")
        all.append(self.max_5_power_first_digit_0())
        print("max_5_power_first_digit_0 done")
        for _ in range(3):
            all.append(self.mixed_2_5())
            print("mixed_2_5 done")
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
            dot_place != -1 and len(n) - 1 - (n[0] == "0") <= self.N_digits
        ), f"{self.N_digits} {n} {n[(dot_place + 1) :]}"
        assert float(n) > 0
