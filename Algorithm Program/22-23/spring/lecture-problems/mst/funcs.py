from random import choice, choices, randint, sample, shuffle
from typing import List, Tuple

Edge = Tuple[int, int, int]
TestCase = Tuple[Tuple[int, int, List[Edge]], int]


class Generator:
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M

    def random(self) -> TestCase:
        n = randint(1, self.N)
        m = randint(1, self.M)
        edges = []
        for _ in range(m):
            u, v = sample(range(1, n + 1), k=2)
            w = randint(0, 10**9)
            edges.append([u, v, w])
        return self.solve(n, m, edges)

    def max_limits_random(self) -> TestCase:
        n = self.N
        m = self.M
        edges = self.gen_tree(n, 0, 10**9)
        for _ in range(m - len(edges)):
            u, v = sample(range(1, n + 1), k=2)
            w = randint(0, 10**9)
            edges.append((u, v, w))
        return self.solve(n, m, edges)

    def max_limits(self) -> TestCase:
        n = self.N
        m = self.M
        edges = self.gen_tree(n, 10**9, 10**9)
        for _ in range(m - len(edges)):
            u, v = sample(range(1, n + 1), k=2)
            w = 10**9
            edges.append((u, v, w))
        return self.solve(n, m, edges)

    def small_weights(self) -> TestCase:
        n = self.N
        m = self.M
        edges = self.gen_tree(n, 0, 10)
        for _ in range(m - len(edges)):
            u, v = sample(range(1, n + 1), k=2)
            w = randint(0, 10)
            edges.append((u, v, w))
        return self.solve(n, m, edges)

    def small_n(self) -> TestCase:
        n = self.N // 100
        m = self.M
        edges = self.gen_tree(n, 0, 10**9)
        for _ in range(m - len(edges)):
            u, v = sample(range(1, n + 1), k=2)
            w = randint(0, 10**9)
            edges.append((u, v, w))
        return self.solve(n, m, edges)

    def disconnected(self) -> TestCase:
        n = self.N
        m = self.M
        edges = []
        for _ in range(m):
            if randint(0, 1):
                u, v = sample(range(1, n // 2), k=2)
            else:
                u, v = sample(range(n // 2, n + 1), k=2)
            w = randint(0, 10**9)
            edges.append([u, v, w])
        return self.solve(n, m, edges)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.max_limits_random,
            self.max_limits_random,
            self.max_limits,
            self.small_weights,
            self.small_weights,
            self.small_n,
            self.disconnected,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def gen_tree(self, n: int, w_lower: int, w_upper) -> List[Edge]:
        edges = []
        nodes = list(range(1, n + 1))
        shuffle(nodes)
        for i, node in enumerate(nodes):
            if not i:
                continue
            parent = nodes[randint(0, i - 1)]
            u, v = node, parent
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v, randint(w_lower, w_upper)))
        return edges

    def solve(self, n: int, m: int, edges: List[Edge]) -> TestCase:
        self.validate(n, m, edges)
        par = [i for i in range(n + 1)]
        sz = [1] * (n + 1)

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
            if x == y:
                return False
            sz[x] += sz[y]
            par[y] = x
            return True

        sorted_edges = sorted(edges, key=lambda edge: edge[2])
        n_components = n
        mst_weight = 0
        for u, v, w in sorted_edges:
            different = union(u, v)
            if different:
                n_components -= 1
                mst_weight += w
        if n_components > 1:
            mst_weight = -1
        return (n, m, edges), mst_weight

    def validate(self, n: int, m: int, edges: List[Edge]) -> None:
        assert 1 <= n <= self.N
        assert 1 <= m <= self.M
        for edge in edges:
            assert len(edge) == 3
            u, v, w = edge
            assert 1 <= u <= self.N and 1 <= v <= self.N and u != v
            assert 0 <= w <= 10**9
