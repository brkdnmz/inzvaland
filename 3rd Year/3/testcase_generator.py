import random
from typing import List

from tqdm import tqdm

from util import randint, randints


class Input:
    def __init__(self, n: int, m: int, grid: List[str]) -> None:
        self.n = n
        self.m = m
        self.grid = grid


MultipleTestInput = List[Input]


class InputGenerator:

    ### IMPLEMENT GENERATORS BEGIN ###

    def small(self) -> MultipleTestInput:
        testcases = []
        n = m = 3
        testcases.append(
            Input(n, m, ["".join(random.choices(r"\/", [1, 2], k=m)) for _ in range(n)])
        )
        testcases.append(
            Input(n, m, ["".join(random.choices(r"\/", [1, 8], k=m)) for _ in range(n)])
        )
        testcases.append(
            Input(n, m, ["".join(random.choices(r"\/", [0, 1], k=m)) for _ in range(n)])
        )

        return testcases

    def mid(self) -> MultipleTestInput:
        testcases = []
        n = m = 33
        testcases.append(
            Input(n, m, ["".join(random.choices(r"\/", [1, 3], k=m)) for _ in range(n)])
        )
        testcases.append(
            Input(
                n, m, ["".join(random.choices(r"\/", [1, 33], k=m)) for _ in range(n)]
            )
        )
        testcases.append(
            Input(n, m, ["".join(random.choices(r"\/", [0, 1], k=m)) for _ in range(n)])
        )

        return testcases

    def large(self) -> MultipleTestInput:
        testcases = []
        n = m = 333
        testcases.append(
            Input(n, m, ["".join(random.choices(r"\/", [1, 3], k=m)) for _ in range(n)])
        )
        testcases.append(
            Input(
                n, m, ["".join(random.choices(r"\/", [1, 33], k=m)) for _ in range(n)]
            )
        )
        testcases.append(
            Input(n, m, ["".join(random.choices(r"\/", [0, 1], k=m)) for _ in range(n)])
        )

        return testcases

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[MultipleTestInput]:
        generators = []
        generators.append(self.small)
        generators.append(self.mid)
        generators.append(self.large)

        print("Generating inputs...")
        inputs: List[MultipleTestInput] = []
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
