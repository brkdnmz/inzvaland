from typing import List

from tqdm import tqdm

from util import randint, randints


class Input:
    n: int
    sucuks: List[int]
    q: int
    queries: List[List[int]]

    def __init__(
        self,
        n: int,
        sucuks: List[int],
        q: int,
        queries: List[List[int]],
    ) -> None:
        self.n = n
        self.sucuks = sucuks
        self.q = q
        self.queries = queries


N = 50
S = 50
Q = 5 * 10**5


class InputGenerator:
    def small_random(self) -> Input:
        n = randint(1, 2)
        sucuks = randints(n, 1, 20)
        q = 10**2
        queries = [sorted(randints(2, n, sum(sucuks))) for _ in range(q)]
        input = Input(n, sucuks, q, queries)
        return input

    def mid_random(self) -> Input:
        n = randint(1, 10)
        sucuks = randints(n, 1, 20)
        q = 10**3
        queries = [sorted(randints(2, n, sum(sucuks))) for _ in range(q)]
        input = Input(n, sucuks, q, queries)
        return input

    def large_random(self) -> Input:
        n = randint(1, 50)
        sucuks = randints(n, 1, 50)
        q = Q
        queries = [sorted(randints(2, n, sum(sucuks))) for _ in range(q)]
        input = Input(n, sucuks, q, queries)
        return input

    def max_random(self) -> Input:
        n = N
        sucuks = [S] * n
        q = Q
        queries = [sorted(randints(2, n, sum(sucuks))) for _ in range(q)]
        input = Input(n, sucuks, q, queries)
        return input

    def max(self) -> Input:
        n = N
        sucuks = [S] * n
        q = Q
        queries = [[n, sum(sucuks)] for _ in range(q)]
        input = Input(n, sucuks, q, queries)
        return input

    def generate(self) -> List[Input]:
        generators = []

        for _ in range(5):
            generators.append(self.small_random)
        for _ in range(5):
            generators.append(self.mid_random)
        for _ in range(5):
            generators.append(self.large_random)
        for _ in range(5):
            generators.append(self.max_random)
        generators.append(self.max)

        inputs: List[Input] = []
        print("Generating inputs...")
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
