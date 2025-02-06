from dataclasses import dataclass
from typing import List

from tqdm import tqdm

from util import gen_graph, make_graph_weighted, randint


@dataclass
class Input:
    n: int
    m: int
    q: int
    edges: list[tuple[int, int, int]]
    queries: list[tuple[int, int, int]]


N = 2 * 10**5
Q = 2 * 10**5


def dijkstra(edges: list[tuple[int, int, int]], n: int, start: int) -> list[int]:
    from heapq import heappop, heappush

    g = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))

    dist = [10**18] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heappush(pq, (dist[v], v))
    return dist


def increase_number_of_shortest_paths(
    edges: list[tuple[int, int, int]], n: int
) -> list[tuple[int, int, int]]:

    updated_edges = []

    for _ in range(3):
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        for edge in edges:
            u, v, w = edge
            if d1[u] + w + d2[v] > d1[v] + w + d2[u]:
                u, v = v, u
            diff = d1[u] + w + d2[v] - d1[n]
            if w > diff:
                w -= randint(diff, w - 1)
            else:
                w -= randint(0, w - 1)
            updated_edges.append((edge[0], edge[1], w))

    return updated_edges


class InputGenerator:

    ### IMPLEMENT GENERATORS BEGIN ###

    def small_random(self) -> Input:
        n = randint(10, 30)
        m = randint(n - 1, n**2 // 2)
        q = 100
        edges = make_graph_weighted(
            gen_graph(n, m, should_be_connected=True, shuffle_nodes=False, max_dist=5),
            1,
            10,
        )
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        queries = []
        for _ in range(q):
            u = randint(1, n)
            v = randint(1, n)
            diff = d1[n] - min(d1[u] + d2[v], d1[v] + d2[u])
            if diff > 0:
                w = 1
                if randint(0, 1):
                    w = diff
            else:
                w = randint(1, 10)
            queries.append((u, v, w))
        return Input(n, m, q, edges, queries)

    def mid_random(self) -> Input:
        n = randint(100, 300)
        m = randint(n - 1, n**2 // 2)
        q = 1000
        edges = make_graph_weighted(
            gen_graph(n, m, should_be_connected=True, shuffle_nodes=False, max_dist=5),
            1,
            100,
        )
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        queries = []
        for _ in range(q):
            u = randint(1, n)
            v = randint(1, n)
            diff = d1[n] - min(d1[u] + d2[v], d1[v] + d2[u])
            if diff > 0:
                w = 1
                if randint(0, 1):
                    w = diff
            else:
                w = randint(1, 100)
            queries.append((u, v, w))
        return Input(n, m, q, edges, queries)

    def large_random(self) -> Input:
        n = randint(1000, 3000)
        m = randint(n - 1, min(n**2 // 2, N))
        q = 10000
        edges = make_graph_weighted(
            gen_graph(n, m, should_be_connected=True, shuffle_nodes=False, max_dist=10),
            1,
            1000,
        )
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        queries = []
        for _ in range(q):
            u = randint(1, n)
            v = randint(1, n)
            diff = d1[n] - min(d1[u] + d2[v], d1[v] + d2[u])
            if diff > 0:
                w = 1
                if randint(0, 1):
                    w = diff
            else:
                w = randint(1, 1000)
            queries.append((u, v, w))
        return Input(n, m, q, edges, queries)

    def max_random(self) -> Input:
        n = N
        m = randint(n - 1, N)
        q = Q
        edges = make_graph_weighted(
            gen_graph(
                n, m, should_be_connected=True, shuffle_nodes=False, max_dist=100
            ),
            1,
            10**9,
        )
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        queries = []
        for _ in range(q):
            u = randint(1, n)
            v = randint(1, n)
            diff = d1[n] - min(d1[u] + d2[v], d1[v] + d2[u])
            if diff > 0:
                w = 1
                if randint(0, 1):
                    w = diff
            else:
                w = randint(1, 10**9)
            queries.append((u, v, w))
        return Input(n, m, q, edges, queries)

    def max(self) -> Input:
        n = N
        m = N
        q = Q
        edges = make_graph_weighted(
            gen_graph(
                n, m, should_be_connected=True, shuffle_nodes=False, max_dist=100
            ),
            10**9,
            10**9,
        )
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        queries = []
        for _ in range(q):
            u = randint(1, n)
            v = randint(1, n)
            diff = d1[n] - min(d1[u] + d2[v], d1[v] + d2[u])
            if diff > 0:
                w = 1
                if randint(0, 1):
                    w = diff
            else:
                w = randint(1, 10**9)
            queries.append((u, v, w))
        return Input(n, m, q, edges, queries)

    def max_small_weights(self) -> Input:
        n = N // 4
        m = N
        q = Q
        edges = make_graph_weighted(
            gen_graph(
                n, m, should_be_connected=True, shuffle_nodes=False, max_dist=100
            ),
            1,
            10,
        )
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        queries = []
        for _ in range(q):
            u = randint(1, n)
            v = randint(1, n)
            diff = d1[n] - min(d1[u] + d2[v], d1[v] + d2[u])
            if diff > 0:
                w = 1
                if randint(0, 1):
                    w = diff
            else:
                w = randint(1, 10)
            queries.append((u, v, w))
        return Input(n, m, q, edges, queries)

    def special(self) -> Input:
        n = N // 4 * 3 + 1
        q = Q
        edges = []
        w = 10**9 - 1
        for node in range(1, n, 3):
            edges.append((node, node + 1, w))
            edges.append((node, node + 2, w))
            edges.append((node + 1, node + 3, w))
            edges.append((node + 2, node + 3, w))
        m = len(edges)
        d1 = dijkstra(edges, n, 1)
        d2 = dijkstra(edges, n, n)
        queries = []
        for _ in range(q):
            u = randint(1, n)
            v = randint(1, n)
            if randint(0, 1):
                if u > v:
                    u, v = v, u
                v = u + 1
            w = randint(10**9 - 2, 10**9)
            diff = d1[n] - min(d1[u] + d2[v], d1[v] + d2[u])
            if diff > 0:
                w = 1
                if randint(0, 1):
                    w = diff
            else:
                w = randint(10**9 - 2, 10**9)
            queries.append((u, v, w))

        return Input(n, m, q, edges, queries)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []
        for _ in range(3):
            generators.append(self.small_random)
        for _ in range(3):
            generators.append(self.mid_random)
        for _ in range(3):
            generators.append(self.large_random)
        for _ in range(3):
            generators.append(self.max_random)
        for _ in range(3):
            generators.append(self.max)
        for _ in range(3):
            generators.append(self.max_small_weights)

        generators.append(self.special)

        print("Generating inputs...")
        inputs: List[Input] = []
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
