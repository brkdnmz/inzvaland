import random
from typing import List, Tuple

from tqdm import tqdm

from util import gen_range, randint, randints

Query = Tuple[int, int]


class Input:
    def __init__(self, n: int, a: List[List[int]]) -> None:
        self.n = n
        self.a = a


N = 10**5


class InputGenerator:
    ### IMPLEMENT GENERATORS BEGIN ###

    def small_random(self) -> Input:
        n = randint(1, 10)
        a = [random.choices(range(10), k=n) for _ in range(10)]

        return Input(n, a)

    def mid_random(self) -> Input:
        n = randint(11, 1000)
        a = [random.choices(range(1000 + 1), k=n) for _ in range(10)]

        return Input(n, a)

    def large_random(self) -> Input:
        n = randint(1001, 10**5)
        a = [random.choices(range(10**9 + 1), k=n) for _ in range(10)]

        return Input(n, a)

    def max_random(self) -> Input:
        n = 10**5
        a = [random.choices(range(10**9 + 1), k=n) for _ in range(10)]

        return Input(n, a)

    def all_same(self) -> Input:
        n = 10**5
        x = randint(1, 10**9)
        a = [[x] * n for _ in range(10)]

        return Input(n, a)

    def all_increasing(self) -> Input:
        n = 10**5
        x = randint(0, 10**9 - n * 10 + 1)
        a = [[x + i * n + j for j in range(n)] for i in range(10)]

        return Input(n, a)

    def all_max(self) -> Input:
        n = 10**5
        x = 10**9
        a = [[x] * n for _ in range(10)]

        return Input(n, a)

    def all_min(self) -> Input:
        n = 10**5
        x = 0
        a = [[x] * n for _ in range(10)]

        return Input(n, a)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.small_random)
        generators.append(self.mid_random)
        generators.append(self.mid_random)
        generators.append(self.mid_random)
        generators.append(self.large_random)
        generators.append(self.large_random)
        generators.append(self.max_random)
        generators.append(self.max_random)
        generators.append(self.max_random)
        generators.append(self.all_same)
        generators.append(self.all_increasing)
        generators.append(self.all_increasing)
        generators.append(self.all_max)
        generators.append(self.all_min)

        inputs: List[Input] = []
        for generate in tqdm(generators, "Generating inputs"):
            inputs.append(generate())
        return inputs
