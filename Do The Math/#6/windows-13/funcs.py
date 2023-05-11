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


TestCase = List[Tuple[int, int, int]]


class Generator:
    def __init__(self, N: int, Q: int, S: int) -> None:
        self.N = N
        self.Q = Q
        self.S = S
        self.n_divisors = [0 for _ in range(self.N + self.S + 1)]
        self.precalc()

    def precalc(self) -> None:
        for i in range(1, self.N + self.S + 1):
            self.n_divisors[i] += self.n_divisors[i - 1]
            for k in range(i, self.N + self.S + 1, i):
                self.n_divisors[k] += 1

    def random(self) -> TestCase:
        queries = []
        n_qs = randint(1, self.Q)
        for query in range(n_qs):
            n_i = randint(1, self.N)
            s_i = randint(0, self.S)
            ans = self.solve(n_i, s_i)
            queries.append((n_i, s_i, ans))
        self.validate(queries)
        return queries

    def max_n_max_s(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for query in range(n_qs):
            n_i = self.N
            s_i = self.S
            ans = self.solve(n_i, s_i)
            queries.append((n_i, s_i, ans))
        self.validate(queries)
        return queries

    def max_prime_max_s(self) -> TestCase:
        queries = []
        n_qs = self.Q
        prime = self.N
        while not is_prime(prime):
            prime -= 1
        for query in range(n_qs):
            n_i = prime
            s_i = self.S
            ans = self.solve(n_i, s_i)
            queries.append((n_i, s_i, ans))
        self.validate(queries)
        return queries

    def max_n_varying_s(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for query in range(n_qs):
            n_i = self.N
            s_i = randint(0, self.S)
            ans = self.solve(n_i, s_i)
            queries.append((n_i, s_i, ans))
        self.validate(queries)
        return queries

    def largest_ns_max_s(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for query in range(n_qs):
            n_i = max(1, self.N - query)
            s_i = self.S
            ans = self.solve(n_i, s_i)
            queries.append((n_i, s_i, ans))
        self.validate(queries)
        return queries

    def zero_s(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for query in range(n_qs):
            n_i = randint(1, self.N)
            s_i = 0
            ans = self.solve(n_i, s_i)
            queries.append((n_i, s_i, ans))
        self.validate(queries)
        return queries

    def n_1(self) -> TestCase:
        queries = []
        n_qs = self.Q
        for query in range(n_qs):
            n_i = 1
            s_i = randint(0, self.S)
            ans = self.solve(n_i, s_i)
            queries.append((n_i, s_i, ans))
        self.validate(queries)
        return queries

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.max_n_max_s())
        print("max_n_max_s done")
        all.append(self.max_prime_max_s())
        print("max_prime_max_s done")
        all.append(self.max_n_varying_s())
        print("max_n_varying_s done")
        all.append(self.largest_ns_max_s())
        print("largest_ns_max_s done")
        all.append(self.zero_s())
        print("zero_s done")
        all.append(self.n_1())
        print("n_1 done")
        return all

    def solve(self, n: int, s: int) -> int:
        ans = self.n_divisors[n + s] - self.n_divisors[n - 1]
        for i in range(1, s + 1):
            ans -= (n + s) // i - (n - 1) // i - 1  # excluding extra counts
        return ans

    def validate(self, queries: TestCase) -> None:
        assert 1 <= len(queries) <= self.Q
        for (n_i, s_i, ans) in queries:
            assert 1 <= n_i <= self.N
            assert 0 <= s_i <= self.S
            assert 1 <= ans and self.solve(n_i, s_i) == ans
