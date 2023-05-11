import sys
from random import choices, randint, shuffle
from typing import List, Literal, Tuple, Union

from numba import njit

Query = Union[Tuple[Literal[1], int, int], Tuple[Literal[2], int]]
Parents = List[int]
Answer = int
TestCase = Tuple[Tuple[int, int, Parents, List[Query]], List[Answer]]
Tree = List[List[int]]

sys.setrecursionlimit(10**9)


# @njit
def gen_parents(n: int, max_parent_dist=10**9) -> Parents:
    nodes = list(range(2, n + 1))
    shuffle(nodes)
    nodes = [1] + nodes
    p = [0] * (n - 1)
    for i, node in enumerate(nodes):
        if not i:
            continue
        p[node - 2] = nodes[randint(max(0, i - max_parent_dist), i - 1)]
    return p


@njit
def gen_tree(parents: Parents) -> Tree:
    n = len(parents) + 1
    g: Tree = [[0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        g[i].pop()
    for i, p in enumerate(parents):
        g[p].append(i + 2)
    return g


# @njit
def dfs(tree: Tree, cur=1) -> int:
    cnt = 1
    for nxt in tree[cur]:
        cnt += dfs(tree, nxt)
    return cnt


def euler_tour(tree: Tree, tin: List[int], tout: List[int], cur=1, t=[0]):
    tin[cur] = t[0]
    t[0] += 1
    for nxt in tree[cur]:
        euler_tour(tree, tin, tout, nxt)
    tout[cur] = t[0]
    t[0] += 1


class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.seg = [0] * (n << 2)

    def get(self, tl: int, tr: int) -> int:
        return self.__get(1, 0, self.n - 1, tl, tr)

    def __get(self, c: int, l: int, r: int, tl: int, tr: int) -> int:
        if tl > r or tr < l:
            return 0
        if tl <= l and r <= tr:
            return self.seg[c]
        mid = (l + r) >> 1
        return self.__get(2 * c, l, mid, tl, tr) + self.__get(2 * c + 1, mid + 1, r, tl, tr)

    def add(self, target: int, val: int):
        self.__add(1, 0, self.n - 1, target, val)

    def __add(self, c: int, l: int, r: int, target: int, val: int):
        if not (l <= target <= r):
            return
        if l == r:
            self.seg[c] += val
            return
        mid = (l + r) >> 1
        self.__add(2 * c, l, mid, target, val)
        self.__add(2 * c + 1, mid + 1, r, target, val)
        self.seg[c] = self.seg[2 * c] + self.seg[2 * c + 1]


class Generator:
    def __init__(self, N: int, Q: int) -> None:
        self.N = N
        self.Q = Q

    def random_1(self) -> TestCase:
        n = randint(self.N // 2, self.N)
        q = randint(self.Q // 2, self.Q)
        parents = gen_parents(n, 10**9)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = randint(-(10**9), 10**9)
                queries.append((1, u, x))
            else:
                u = randint(1, n)
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def random_2(self) -> TestCase:
        n = randint(self.N // 2, self.N)
        q = randint(self.Q // 2, self.Q)
        parents = gen_parents(n, 10**3)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = randint(-(10**9), 10**9)
                queries.append((1, u, x))
            else:
                u = randint(1, n)
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def random_3(self) -> TestCase:
        n = randint(self.N // 2, self.N)
        q = randint(self.Q // 2, self.Q)
        parents = gen_parents(n, 10)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = randint(-(10**9), 10**9)
                queries.append((1, u, x))
            else:
                u = randint(1, n)
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def random_4(self) -> TestCase:
        n = randint(self.N // 2, self.N)
        q = randint(self.Q // 2, self.Q)
        parents = gen_parents(n, 2)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = randint(-(10**9), 10**9)
                queries.append((1, u, x))
            else:
                u = randint(1, n)
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def max(self) -> TestCase:
        n = self.N
        q = self.Q
        parents = gen_parents(n, 50)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = randint(-(10**9), 10**9)
                queries.append((1, u, x))
            else:
                u = randint(1, n)
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def max_u_always_1(self) -> TestCase:
        n = self.N
        q = self.Q
        parents = gen_parents(n, 5)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = randint(-(10**9), 10**9)
                queries.append((1, u, x))
            else:
                u = 1
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def max_u_always_1_x_max(self) -> TestCase:
        n = self.N
        q = self.Q
        parents = gen_parents(n, 5)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = 10**9
                queries.append((1, u, x))
            else:
                u = 1
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def chain(self) -> TestCase:
        n = self.N
        q = self.Q
        parents = gen_parents(n, 1)
        queries: List[Query] = []
        for _ in range(q):
            query_type = randint(1, 2)
            if query_type == 1:
                u = randint(1, n)
                x = randint(-(10**9), 10**9)
                queries.append((1, u, x))
            else:
                u = randint(1, n)
                queries.append((2, u))
        return self.solve(n, q, parents, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random_1,
            self.random_2,
            self.random_3,
            self.random_4,
            self.max,
            self.max_u_always_1,
            self.max_u_always_1_x_max,
            self.chain,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, q: int, parents: Parents, queries: List[Query]) -> TestCase:
        self.validate(n, q, parents, queries)
        tree = gen_tree(parents)
        tin = [0] * (n + 1)
        tout = [0] * (n + 1)
        euler_tour(tree, tin, tout)
        seg_tree = SegTree(tout[1] + 1)
        answers: List[Answer] = []
        for query in queries:
            if query[0] == 1:
                seg_tree.add(tin[query[1]], query[2])
            answers.append(seg_tree.get(tin[query[1]], tout[query[1]]))
        return (n, q, parents, queries), answers

    def validate(self, n: int, q: int, parents: Parents, queries: List[Query]) -> None:
        assert 1 <= n <= self.N
        assert 1 <= q <= self.Q
        assert len(parents) == n - 1
        tree = gen_tree(parents)
        assert dfs(tree) == n
        for query in queries:
            if query[0] == 1:
                assert 1 <= query[1] <= n and abs(query[2]) <= 10**9
            else:
                assert query[0] == 2
                assert 1 <= query[1] <= n
