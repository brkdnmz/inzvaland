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


TestCase = Tuple[Tuple[int, int], int]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int, N_zero: int) -> None:
        self.N = N
        self.N_zero = N_zero

    def random(self) -> TestCase:
        a = randint(1, self.N)
        b = randint(1, self.N // a)
        return (a, b), self.solve(a, b)

    def equal(self) -> TestCase:
        a = int(self.N**0.5)
        b = self.N // a
        return (a, b), self.solve(a, b)

    def a_min_b_max(self) -> TestCase:
        a = 1
        b = self.N
        return (a, b), self.solve(a, b)

    def b_min_a_max(self) -> TestCase:
        a = self.N
        b = 1
        return (a, b), self.solve(a, b)

    def random_a_zero(self) -> TestCase:
        a = 0
        b = randint(1, self.N_zero)
        return (a, b), self.solve(a, b)

    def random_b_zero(self) -> TestCase:
        b = 0
        a = randint(1, self.N_zero)
        return (a, b), self.solve(a, b)

    def a_zero_b_max(self) -> TestCase:
        a = 0
        b = self.N_zero
        return (a, b), self.solve(a, b)

    def b_zero_a_max(self) -> TestCase:
        b = 0
        a = self.N_zero
        return (a, b), self.solve(a, b)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        all.append(self.equal())
        all.append(self.a_min_b_max())
        all.append(self.b_min_a_max())
        all.append(self.random_a_zero())
        all.append(self.random_b_zero())
        all.append(self.a_zero_b_max())
        all.append(self.b_zero_a_max())
        return all

    def solve(self, a: int, b: int) -> int:
        if a < b:
            a, b = b, a
        if not b:
            return pow(2, max(0, a - 1), MOD)
        dp = [[0] * (b + 1) for _ in range(a + 1)]
        dp[0][0] = 1
        for i in range(a + 1):
            for j in range(b + 1):
                if i:
                    dp[i][j] = (1 + (i + j > 1)) * dp[i - 1][j]
                    dp[i][j] %= MOD
                if j:
                    dp[i][j] += (1 + (i + j> 1)) * dp[i][j - 1]
                    dp[i][j] %= MOD
                if i and j:
                    dp[i][j] -= (1 + (i > 1 or j > 1)) * dp[i - 1][j - 1]
                    dp[i][j] %= MOD
        return dp[a][b]

    def validate(self, a: int, b: int) -> None:
        if a < b:
            a, b = b, a
        assert (a and b and a * b <= self.N) or (not b and a <= self.N_zero)
