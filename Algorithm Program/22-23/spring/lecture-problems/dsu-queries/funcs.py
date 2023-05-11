from random import choice, choices, randint, sample, shuffle
from typing import List, Tuple

TestCase = Tuple[Tuple[int, int, List[List[int]]], List[int]]


class Generator:
    def __init__(self, N: int, Q: int) -> None:
        self.N = N
        self.Q = Q

    def random(self) -> TestCase:
        n = randint(1, self.N)
        q = randint(1, self.Q)
        queries = []
        for _ in range(q):
            type = randint(1, 2)
            if type == 1:
                queries.append([1, *sample(range(1, n+1), k=2)])
            else:
                queries.append([2, randint(1, n)])
        return self.solve(n, q, queries)

    def max_limits_random(self) -> TestCase:
        n = self.N
        q = self.Q
        queries = []
        for _ in range(q):
            type = randint(1, 2)
            if type == 1:
                queries.append([1, *sample(range(1, n+1), k=2)])
            else:
                queries.append([2, randint(1, n)])
        return self.solve(n, q, queries)

    def max_queries_small_n(self) -> TestCase:
        n = self.N // 10
        q = self.Q
        queries = []
        for _ in range(q):
            type = randint(1, 2)
            if type == 1:
                queries.append([1, *sample(range(1, n+1), k=2)])
            else:
                queries.append([2, randint(1, n)])
        return self.solve(n, q, queries)
    
    def worst_case(self) -> TestCase:
        n = self.N
        q = self.Q
        fixed = randint(1, n)
        queries = []
        for i in range(1, n+1):
            if i == fixed:
                continue
            queries.append([1, i, fixed])
        while len(queries) < q:
            queries.append([2, randint(1, n)])
        shuffle(queries)
        return self.solve(n, q, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.max_limits_random,
            self.max_queries_small_n,
            self.worst_case
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, q: int, queries: List[List[int]]) -> TestCase:
        self.validate(n, q, queries)
        par = [i for i in range(n+1)]
        sz = [1] * (n+1)
        def find(x: int):
            if x == par[x]:
                return x
            par[x] = find(par[x])
            return par[x]
        def union(x: int, y: int):
            x = find(x)
            y = find(y)
            if sz[x] < sz[y]:
                x, y = y, x
            if x != y:
                sz[x] += sz[y]
                par[y] = x
        answers = []
        for query in queries:
            if query[0] == 1:
                union(query[1], query[2])
                answers.append(sz[find(query[1])])
            else:
                answers.append(sz[find(query[1])])

        return (n, q, queries), answers

    def validate(self, n: int, q: int, queries: List[List[int]]) -> None:
        assert 1 <= n <= self.N
        assert 1 <= q <= self.Q
        for query in queries:
            assert query[0] in [1, 2]
            if query[0] == 2:
                assert len(query) == 2
                assert 1 <= query[1] <= self.N
            else:
                assert len(query) == 3
                assert 1 <= query[1] <= self.N
                assert 1 <= query[2] <= self.N
                assert query[1] != query[2]

