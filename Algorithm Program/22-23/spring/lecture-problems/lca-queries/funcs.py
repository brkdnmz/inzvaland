import random
import sys
from random import choice, choices, randint, sample, shuffle
from typing import List, Tuple

import numpy
from numba import njit
from numpy import insert

Query = Tuple[int, int]
Edge = Query
Answer = Query
TestCase = Tuple[Tuple[int, int, List[Edge], List[Query]], List[Answer]]
Tree = List[List[int]]
Parents = Tree

sys.setrecursionlimit(10**9)


# @njit
def dfs(g: Tree, cur=1, p=0) -> int:
    cnt = 1
    for nxt in g[cur]:
        if nxt == p:
            continue
        cnt += dfs(g, nxt, cur)
    return cnt


@njit
def gen_tree(edges: List[Edge]) -> Tree:
    n = 0
    for u, v in edges:
        n = max(n, u, v)
    g: Tree = [[0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        g[i].pop()
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    return g


# @njit
def precalc(g: Tree, par: Parents, height: List[int], cur=1, p=0):
    height[cur] = height[p] + 1
    par[cur][0] = p
    for j in range(1, len(par[cur])):
        par[cur][j] = par[par[cur][j - 1]][j - 1]
    for nxt in g[cur]:
        if nxt == p:
            continue
        precalc(g, par, height, nxt, cur)


# @njit
def lca(par: Parents, height: List[int], u: int, v: int):
    if height[u] < height[v]:
        u, v = v, u
    for i in range(17, -1, -1):
        if height[par[u][i]] >= height[v]:
            u = par[u][i]
    if u == v:
        return u
    for i in range(17, -1, -1):
        if par[u][i] != par[v][i]:
            u, v = par[u][i], par[v][i]
    return par[u][0]


def gen_nodes(n: int) -> List[int]:
    nodes = list(range(1, n + 1))
    copy = nodes[1:]
    shuffle(copy)
    nodes[1:] = copy
    return nodes


class Generator:
    def __init__(self, N: int, Q: int) -> None:
        self.N = N
        self.Q = Q

    def random(self) -> TestCase:
        n = randint(1, self.N)
        q = randint(1, self.Q)
        edges: List[Edge] = []
        nodes = gen_nodes(n)
        for i, node in enumerate(nodes):
            if not i:
                continue
            u, v = nodes[randint(0, i - 1)], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        queries = [tuple(choices(range(1, n + 1), k=2)) for _ in range(q)]
        return self.solve(n, q, edges, queries)

    def max_limits_random(self) -> TestCase:
        n = self.N
        q = self.Q
        edges = []
        nodes = gen_nodes(n)
        for i, node in enumerate(nodes):
            if not i:
                continue
            u, v = nodes[randint(0, i - 1)], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        queries = [tuple(choices(range(1, n + 1), k=2)) for _ in range(q)]
        return self.solve(n, q, edges, queries)

    def max_limits_random_same_nodes(self) -> TestCase:
        n = self.N
        q = self.Q
        edges = []
        nodes = gen_nodes(n)
        for i, node in enumerate(nodes):
            if not i:
                continue
            u, v = nodes[randint(0, i - 1)], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        queries = [tuple([randint(1, n)] * 2) for _ in range(q)]
        for u, v in queries:
            assert u == v
        return self.solve(n, q, edges, queries)

    def chain(self) -> TestCase:
        n = self.N
        q = self.Q
        edges = []
        nodes = gen_nodes(n)
        for i, node in enumerate(nodes):
            if not i:
                continue
            u, v = nodes[i - 1], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        queries = [tuple(choices(range(1, n + 1), k=2)) for _ in range(q)]
        return self.solve(n, q, edges, queries)

    def chain_distant_queries(self) -> TestCase:
        n = self.N
        q = self.Q
        edges = []
        nodes = gen_nodes(n)
        for i, node in enumerate(nodes):
            if not i:
                continue
            u, v = nodes[i - 1], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        queries = []
        for i in range(q):
            queries.append((1, i + 1))
        return self.solve(n, q, edges, queries)

    def chain_plus_two_branches(self) -> TestCase:
        n = self.N
        q = self.Q
        edges = []
        nodes = gen_nodes(n)
        for i, node in enumerate(nodes[: n // 3]):
            if not i:
                continue
            u, v = nodes[i - 1], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        for i, node in enumerate(nodes[n // 3 : 2 * n // 3]):
            u, v = nodes[i - 1], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        for i, node in enumerate(nodes[2 * n // 3 :]):
            u, v = nodes[n // 3 - 1] if i == 2 * n // 3 else nodes[i - 1], node
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))
        queries = [tuple(choices(range(1, n + 1), k=2)) for _ in range(q)]
        return self.solve(n, q, edges, queries)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.max_limits_random,
            self.max_limits_random_same_nodes,
            self.chain,
            self.chain_distant_queries,
            self.chain_plus_two_branches,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, q: int, edges: List[Edge], queries: List[Query]) -> TestCase:
        self.validate(n, q, edges, queries)
        tree = gen_tree(edges)
        par = [[0] * 18 for _ in range(n + 1)]
        height = [0] * (n + 1)
        precalc(tree, par, height)
        answers: List[Answer] = []
        for u, v in queries:
            cur_lca = lca(par, height, u, v)
            answers.append((cur_lca, height[u] + height[v] - 2 * height[cur_lca]))
        return (n, q, edges, queries), answers

    def validate(self, n: int, q: int, edges: List[Edge], queries: List[Query]) -> None:
        assert 1 <= n <= self.N
        assert 1 <= q <= self.Q
        assert len(edges) == n - 1
        for u, v in edges:
            assert 1 <= u <= n and 1 <= v <= n and u != v
        tree = gen_tree(edges)
        assert dfs(tree) == n
        for u, v in queries:
            assert 1 <= u <= n and 1 <= v <= n
