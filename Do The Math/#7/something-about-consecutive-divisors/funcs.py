from random import randint, shuffle
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


TestCase = List[Tuple[int, int]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int, Q: int) -> None:
        self.N = N
        self.Q = Q
        self.n_primes = [0 for _ in range(self.N + 1)]
        self.ans = [1 for _ in range(self.N + 1)]
        self.precalc()

    def precalc(self) -> None:
        for i in range(2, self.N + 1):
            self.ans[i] = self.ans[i - 1]
            is_p = self.n_primes[i] == 0
            if is_p:
                self.ans[i] *= i
                self.ans[i] %= MOD
            self.n_primes[i] = self.n_primes[i - 1]
            if not is_p:
                continue
            for k in range(i, self.N + 1, i):
                self.n_primes[k] += 1

    def random(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for _ in range(n_qs):
            n_i = randint(1, self.N)
            ans = self.ans[n_i]
            queries.append((n_i, ans))
        self.validate(queries)
        return queries

    def max_n(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for _ in range(n_qs):
            n_i = self.N
            ans = self.ans[n_i]
            queries.append((n_i, ans))
        self.validate(queries)
        return queries

    def min_n(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for _ in range(n_qs):
            n_i = 1
            ans = self.ans[n_i]
            queries.append((n_i, ans))
        self.validate(queries)
        return queries

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.max_n())
        print("max_n done")
        all.append(self.min_n())
        print("min_n done")
        return all

    def validate(self, queries: TestCase) -> None:
        assert 1 <= len(queries) <= self.Q
        for (n_i, ans) in queries:
            assert 1 <= n_i <= self.N
