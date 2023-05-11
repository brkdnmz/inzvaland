from random import choice, randint
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


TestCase = Tuple[Tuple[int, int], str]
MOD = 10**9 + 7


class Generator:
    def __init__(self, H: int) -> None:
        self.H = H

    def random(self) -> TestCase:
        h = randint(1, self.H)
        m = randint(0, 59)
        return (h, m), self.solve(h, m)

    def max(self) -> TestCase:
        h = self.H
        m = 59
        return (h, m), self.solve(h, m)

    def random_yes(self) -> TestCase:
        # n = (60k + 59) * x <= 60H + 59
        k = randint(0, self.H)
        x = randint(1, (60 * self.H + 59) // (60 * k + 59))
        n = (60 * k + 59) * x
        h = n // 60
        m = n % 60
        res = self.solve(h, m)
        assert res == "YES"
        return (h, m), res

    def max_yes(self) -> TestCase:
        # n = (60k + 59) * x <= 60H + 59
        h = self.H
        m = 59
        res = self.solve(h, m)
        assert res == "YES"
        return (h, m), res

    def large_yes(self) -> TestCase:
        # n = (60k + 59) * x <= 60H + 59
        h = self.H // 2
        m = 59
        res = self.solve(h, m)
        assert res == "YES"
        return (h, m), res

    def large_prime_yes(self) -> TestCase:
        # n = (60k + 59) * x <= 60H + 59
        k = randint(0, 100)
        x = (60 * self.H + 59) // (60 * k + 59)
        x = prev_prime(x)
        n = (60 * k + 59) * x
        h = n // 60
        m = n % 60
        res = self.solve(h, m)
        assert res == "YES"
        return (h, m), res

    def m_zero_yes(self) -> TestCase:
        # h = k * (60t + 59) <= self.H
        # k * (60t + 59) <= self.H
        # 60t <= self.H - 59
        t = randint(0, (self.H - 59) // 60)
        k = randint(1, self.H // (60 * t + 59))
        h = k * (60 * t + 59)
        m = 0
        res = self.solve(h, m)
        assert res == "YES"
        return (h, m), res

    def h_max_m_zero(self) -> TestCase:
        h = self.H
        m = 0
        return (h, m), self.solve(h, m)

    def square(self) -> TestCase:
        # n = (60k + 59)**2 <= 60H + 59
        bound = int((60 * self.H + 59) ** 0.5)
        k = (bound - 59) // 60
        n = (60 * k + 59) ** 2
        h = n // 60
        m = n % 60
        return (h, m), self.solve(h, m)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        all.append(self.random())
        all.append(self.random())
        all.append(self.max())
        all.append(self.random_yes())
        all.append(self.random_yes())
        all.append(self.max_yes())
        all.append(self.large_yes())
        all.append(self.large_prime_yes())
        all.append(self.max_yes())
        all.append(self.m_zero_yes())
        all.append(self.m_zero_yes())
        all.append(self.h_max_m_zero())
        return all

    def solve(self, h: int, m: int) -> str:
        self.validate(h, m)
        n = 60 * h + m
        for d in range(1, n + 1):
            if d * d > n:
                break
            if n % d:
                continue
            if (d + 1) % 60 == 0 or (n // d + 1) % 60 == 0:
                return "YES"
        return "NO"

    def validate(self, h: int, m: int) -> None:
        assert 1 <= h <= self.H and 0 <= m <= 59
