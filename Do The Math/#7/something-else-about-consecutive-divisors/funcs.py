from math import gcd
from random import choices, randint
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


TestCase = List[Tuple[int, int, int, int]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int, Q: int, K: int) -> None:
        self.N = N
        self.Q = Q
        self.K = K
        self.lcm = [1]
        self.precalc()

    def precalc(self) -> None:
        for i in range(1, self.K + 5):
            self.lcm.append(1)
            if self.lcm[i - 1] > self.N:
                self.lcm[i] = self.lcm[i - 1]
                continue
            cur_lcm = self.lcm[i - 1] * i // gcd(self.lcm[i - 1], i)
            cur_lcm = min(cur_lcm, self.N + 1)
            self.lcm[i] = cur_lcm

    def random(self) -> TestCase:
        q = randint(1, self.Q)
        queries = []
        for _ in range(q):
            l, r = sorted(choices(range(1, self.N), k=2))
            k = randint(1, self.K)
            ans = self.calc_within_bounds(l, r, k)
            queries.append((l, r, k, ans))
        return queries

    def min_l_max_r(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            l = 1
            r = self.N
            k = randint(1, self.K)
            ans = self.calc_within_bounds(l, r, k)
            queries.append((l, r, k, ans))
        return queries

    def min_l_r(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            l = 1
            r = 1
            k = randint(1, self.K)
            ans = self.calc_within_bounds(l, r, k)
            queries.append((l, r, k, ans))
        return queries

    def max_l_r(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            l = self.N
            r = self.N
            k = randint(1, self.K)
            ans = self.calc_within_bounds(l, r, k)
            queries.append((l, r, k, ans))
        return queries

    def all_min(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            l = 1
            r = 1
            k = 1
            ans = self.calc_within_bounds(l, r, k)
            queries.append((l, r, k, ans))
        return queries

    def all_max(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            l = self.N
            r = self.N
            k = self.K
            ans = self.calc_within_bounds(l, r, k)
            queries.append((l, r, k, ans))
        return queries

    def rand_l_max_r(self) -> TestCase:
        q = self.Q
        queries = []
        for _ in range(q):
            l = randint(1, self.N)
            r = self.N
            k = randint(1, self.K)
            ans = self.calc_within_bounds(l, r, k)
            queries.append((l, r, k, ans))
        return queries

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.min_l_max_r())
        print("min_l_max_r done")
        all.append(self.min_l_r())
        print("min_l_r done")
        all.append(self.max_l_r())
        print("max_l_r done")
        all.append(self.all_min())
        print("all_min done")
        all.append(self.all_max())
        print("all_max done")
        all.append(self.rand_l_max_r())
        print("rand_l_max_r done")
        return all

    def calc_up_to_bound(self, bound: int, k: int) -> int:
        return bound // self.lcm[k] - bound // self.lcm[k + 1]

    def calc_within_bounds(self, l: int, r: int, k: int) -> int:
        return self.calc_up_to_bound(r, k) - self.calc_up_to_bound(l - 1, k)

    def validate(self, queries: TestCase) -> None:
        assert 1 <= len(queries) <= self.Q
        for (l, r, k, ans) in queries:
            assert 1 <= l <= r <= self.N
            assert 1 <= k <= self.K
            assert ans == self.calc_within_bounds(l, r, k)
