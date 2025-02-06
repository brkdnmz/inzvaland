from random import random, shuffle
from typing import List

from tqdm import tqdm

from util import gen_blossom_tree, gen_chain_tree, gen_random_tree, gen_tree, randint


class Input:
    def __init__(
        self,
        n: int,
        edges: list[tuple[int, int, int]],
        q: int,
        queries: list[tuple[int, int]],
    ) -> None:
        self.n = n
        self.edges = edges
        self.q = q
        self.queries = queries


N = 2 * 10**5
Q = 2 * 10**5
W = 10**8


def gen_query(n: int) -> tuple[int, int]:
    p = random()
    if p < 0.1:
        u = randint(1, n)
        return u, u
    return randint(1, n), randint(1, n)


class InputGenerator:

    ### IMPLEMENT GENERATORS BEGIN ###

    def small(self) -> Input:
        n = randint(5, 10**2)
        edges = gen_random_tree(n)
        edges = [(u, v, randint(1, 10**2)) for u, v in edges]
        q = 10**2
        queries = []
        for _ in range(q):
            queries.append(gen_query(n))
        return Input(n, edges, q, queries)

    def mid(self) -> Input:
        n = randint(10**2 + 1, 10**4)
        edges = gen_random_tree(n)
        edges = [(u, v, randint(1, 10**4)) for u, v in edges]
        q = 10**4
        queries = []
        for _ in range(q):
            queries.append(gen_query(n))
        return Input(n, edges, q, queries)

    def large(self) -> Input:
        n = randint(10**4 + 1, N)
        edges = gen_tree(n)
        edges = [(u, v, randint(1, W)) for u, v in edges]
        q = Q
        queries = []
        for _ in range(q):
            queries.append(gen_query(n))
        return Input(n, edges, q, queries)

    def max(self) -> Input:
        n = N
        edges = gen_tree(n)
        edges = [(u, v, randint(1, W)) for u, v in edges]
        q = Q
        queries = []
        for _ in range(q):
            queries.append(gen_query(n))
        return Input(n, edges, q, queries)

    def max_chain(self) -> Input:
        n = N
        edges = gen_chain_tree(n)
        edges = [(u, v, randint(1, W)) for u, v in edges]
        q = Q
        queries = []
        for _ in range(q):
            queries.append(gen_query(n))
        return Input(n, edges, q, queries)

    def max_blossom(self) -> Input:
        n = N
        edges = gen_blossom_tree(n)
        edges = [(u, v, randint(1, W)) for u, v in edges]
        q = Q
        queries = []
        for i in range(q):
            queries.append(gen_query(n))
        shuffle(queries)
        return Input(n, edges, q, queries)

    def max_tall(self) -> Input:
        n = N
        edges = gen_tree(n, 5, 1)
        edges = [(u, v, randint(1, W)) for u, v in edges]
        q = Q
        queries = []
        for i in range(q):
            queries.append(gen_query(n))
        shuffle(queries)
        return Input(n, edges, q, queries)

    def chain_max_weight_single_node_queries(self) -> Input:
        n = N
        edges = gen_chain_tree(n)
        edges = [(u, v, W) for u, v in edges]
        q = Q
        queries = []
        for i in range(q):
            queries.append((i + 1, i + 1))
        shuffle(queries)
        return Input(n, edges, q, queries)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []
        for _ in range(25):
            generators.append(self.small)
        for _ in range(10):
            generators.append(self.mid)
        for _ in range(5):
            generators.append(self.large)

        generators.append(self.max)
        generators.append(self.max_chain)
        generators.append(self.max_blossom)
        generators.append(self.max_tall)
        generators.append(self.chain_max_weight_single_node_queries)

        print("Generating inputs...")
        inputs: List[Input] = []
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
