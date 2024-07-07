import random
from typing import List, Tuple

from tqdm import tqdm

from util import randint, randints


class Input:
    def __init__(
        self, n: int, m: int, sigo: int, ciko: int, edges: List[Tuple[int, int]], q: int, queries: List[Tuple[int, int]]
    ) -> None:
        self.n = n
        self.m = m
        self.sigo = sigo
        self.ciko = ciko
        self.edges = edges
        self.q = q
        self.queries = queries


MultipleTestInput = List[Input]


class InputGenerator:

    ### IMPLEMENT GENERATORS BEGIN ###

    def all_random(self) -> Input:
        n = randint(1, 2 * 10**5)
        m = randint(0, 2 * 10**5)
        sigo = randint(1, n)
        ciko = randint(1, n)
        edges = [(randint(1, n), randint(1, n)) for _ in range(m)]
        q = randint(1, 2 * 10**5)
        queries = [(randint(1, n), randint(1, n)) for _ in range(q)]
        return Input(n, m, sigo, ciko, edges, q, queries)

    def small(self) -> Input:
        n = randint(1, 20)
        m = randint(0, 20)
        sigo = randint(1, n)
        ciko = randint(1, n)
        edges = [(randint(1, n), randint(1, n)) for _ in range(m)]
        q = randint(1, 20)
        queries = [(randint(1, n), randint(1, n)) for _ in range(q)]
        return Input(n, m, sigo, ciko, edges, q, queries)

    def mid(self) -> Input:
        n = randint(1, 1000)
        m = randint(0, 1000)
        sigo = randint(1, n)
        ciko = randint(1, n)
        edges = [(randint(1, n), randint(1, n)) for _ in range(m)]
        q = randint(1, 1000)
        queries = [(randint(1, n), randint(1, n)) for _ in range(q)]
        return Input(n, m, sigo, ciko, edges, q, queries)

    def no_edge(self) -> Input:
        n = 2 * 10**5
        m = 0
        sigo = randint(1, n)
        ciko = randint(1, n)
        edges = [(randint(1, n), randint(1, n)) for _ in range(m)]
        q = 2 * 10**5
        queries = [(randint(1, n), randint(1, n)) for _ in range(q)]
        return Input(n, m, sigo, ciko, edges, q, queries)

    def few_edges(self) -> Input:
        n = 2 * 10**5
        m = 12345
        sigo = randint(1, n)
        ciko = randint(1, n)
        edges = [(randint(1, n), randint(1, n)) for _ in range(m)]
        q = 2 * 10**5
        queries = [(randint(1, n), randint(1, n)) for _ in range(q)]
        return Input(n, m, sigo, ciko, edges, q, queries)

    def max(self) -> Input:
        n = 2 * 10**5
        m = 2 * 10**5
        sigo = randint(1, n)
        ciko = randint(1, n)
        edges = [(randint(1, n), randint(1, n)) for _ in range(m)]
        q = 2 * 10**5
        queries = [(randint(1, n), randint(1, n)) for _ in range(q)]
        return Input(n, m, sigo, ciko, edges, q, queries)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []
        for _ in range(5):
            generators.append(self.all_random)
        for _ in range(5):
            generators.append(self.small)
        for _ in range(5):
            generators.append(self.mid)
        generators.append(self.no_edge)
        for _ in range(5):
            generators.append(self.few_edges)
        for _ in range(5):
            generators.append(self.max)

        print("Generating inputs...")
        inputs: List[Input] = []
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
