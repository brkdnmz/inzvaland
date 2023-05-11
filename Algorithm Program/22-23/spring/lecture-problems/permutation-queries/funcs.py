import random
from random import choice, choices, randint, sample, shuffle
from typing import List, Tuple

from numba import njit
from numpy import insert

Query = Tuple[int, int]
TestCase = Tuple[Tuple[int, int, List[int], List[Query]], List[int]]


@njit
def calc(n, p, queries):
    next = [[0] * 64 for i in range(n)]
    for i, x in enumerate(p):
        next[i][0] = x - 1
    for j in range(1, 64):
        for i in range(n):
            next[i][j] = next[next[i][j - 1]][j - 1]
    answers = []
    for x, k in queries:
        cur = x - 1
        j = 0
        while k:
            if k & 1:
                cur = next[cur][j]
            k >>= 1
            j += 1
        answers.append(p[cur])
    return answers


@njit
def gen_one_cycle(p):
    values = list(range(1, len(p) + 1))
    values.remove(1)
    cur = 0
    while len(values):
        if len(values) % 1000 == 0:
            print(len(values))
        next_value = values[randint(0, len(values) - 1)]
        values.remove(next_value)
        p[cur] = next_value
        cur = next_value - 1
    p[cur] = 1
    vis = [0] * len(p)
    cur = 0
    while not vis[cur]:
        vis[cur] = 1
        cur = p[cur] - 1
    assert sum(vis) == len(p)


class Generator:
    def __init__(self, N: int, Q: int, K: int) -> None:
        self.N = N
        self.Q = Q
        self.K = K

    def random(self) -> TestCase:
        n = randint(1, self.N)
        q = randint(1, self.Q)
        p = list(range(1, n + 1))
        shuffle(p)
        queries = []
        for _ in range(q):
            queries.append((randint(1, n), randint(0, self.K)))
        return self.solve(n, q, p, queries)

    def max_limits_random(self) -> TestCase:
        n = self.N
        q = self.Q
        p = list(range(1, n + 1))
        shuffle(p)
        queries = []
        for _ in range(q):
            queries.append((randint(1, n), randint(0, self.K)))
        return self.solve(n, q, p, queries)

    def all_max(self) -> TestCase:
        n = self.N
        q = self.Q
        p = list(range(1, n + 1))
        shuffle(p)
        queries = []
        for _ in range(q):
            queries.append((randint(1, n), self.K))
        return self.solve(n, q, p, queries)

    def identity(self) -> TestCase:
        n = self.N
        q = self.Q
        p = list(range(1, n + 1))
        queries = []
        for _ in range(q):
            queries.append((randint(1, n), randint(0, self.K)))
        return self.solve(n, q, p, queries)

    def one_cycle(self) -> TestCase:
        n = self.N
        q = self.Q
        p = [0] * n
        gen_one_cycle(p)
        queries = []
        for _ in range(q):
            queries.append((randint(1, n), randint(0, self.K)))
        return self.solve(n, q, p, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (self.random, self.max_limits_random, self.all_max, self.identity, self.one_cycle)

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, q: int, p: List[int], queries: List[Query]) -> TestCase:
        self.validate(n, q, p, queries)

        answers = calc(n, p, queries)
        return (n, q, p, queries), answers

    def validate(self, n: int, q: int, p: List[int], queries: List[Query]) -> None:
        assert 1 <= n <= self.N
        assert 1 <= q <= self.Q
        assert len(p) == n
        sorted_p = sorted(p)
        for i, x in enumerate(sorted_p):
            assert x == i + 1
        for query in queries:
            assert len(query) == 2
            x, k = query
            assert 1 <= x <= n
            assert 0 <= k <= self.K
