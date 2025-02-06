from random import random
from typing import List

from tqdm import tqdm

from util import randint, randints


class Input:
    n: int
    heights: List[int]
    o: int
    rains: List[List[int]]

    def __init__(
        self, n: int, heights: List[int], o: int, rains: List[List[int]]
    ) -> None:
        self.n = n
        self.heights = heights
        self.o = o
        self.rains = rains


N = 10**6
H = 10**9
O = 5 * 10**5


def gen_query(n: int) -> List[int]:
    type_prob = random()
    if type_prob <= 0.2:
        return [randint(1, max(1, n // 2)), randint(n - n // 2, n)]
    elif type_prob <= 0.3:
        return [randint(1, max(1, n // 10)), randint(n - n // 10, n)]
    elif type_prob <= 0.4:
        return [randint(1, max(1, n // 100)), randint(n - n // 100, n)]
    elif type_prob <= 0.5:
        return [randint(1, max(1, n // 1000)), randint(n - n // 1000, n)]
    elif type_prob <= 0.6:
        return [randint(1, max(1, n // 10000)), randint(n - n // 10000, n)]
    elif type_prob <= 0.7:
        l = randint(1, n)
        r = min(n, l + randint(0, 10))
        return [l, r]
    elif type_prob <= 0.8:
        l = randint(1, n)
        r = min(n, l + randint(0, 100))
        return [l, r]
    return sorted(randints(2, 1, n))


class InputGenerator:
    def small_random(self) -> Input:
        n = randint(1, 10**2)
        heights = randints(n, 1, 10**2)
        o = 10**2
        rains = [[*gen_query(n), randint(1, 10**2)] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def mid_random(self) -> Input:
        n = randint(10**2 + 1, 10**3)
        heights = randints(n, 1, 10**5)
        o = 10**3
        rains = [[*gen_query(n), randint(1, 10**5)] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def large_random(self) -> Input:
        n = randint(10**3 + 1, 10**5)
        heights = randints(n, 1, 10**9)
        o = 10**5
        rains = [[*gen_query(n), randint(1, H)] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def max_random(self) -> Input:
        n = N
        heights = randints(n, 1, H)
        o = O
        rains = [[*gen_query(n), randint(1, H)] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def all_heights_1(self) -> Input:
        n = N
        heights = [1] * n
        o = O
        rains = [[*gen_query(n), randint(1, H)] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def all_rains_median(self) -> Input:
        n = N
        heights = randints(n, 1, H)
        median = sorted(heights)[len(heights) // 2]
        o = O
        rains = [[*gen_query(n), median] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def all_rains_1(self) -> Input:
        n = N
        heights = randints(n, 1, H)
        o = O
        rains = [[*gen_query(n), 1] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def all_rains_max(self) -> Input:
        n = N
        heights = randints(n, 1, H)
        o = O
        rains = [[*gen_query(n), H] for _ in range(o)]
        input = Input(n, heights, o, rains)
        return input

    def generate(self) -> List[Input]:
        generators = []

        for _ in range(5):
            generators.append(self.small_random)
        for _ in range(5):
            generators.append(self.mid_random)
        for _ in range(5):
            generators.append(self.large_random)
        for _ in range(2):
            generators.append(self.max_random)
        generators.append(self.all_heights_1)
        generators.append(self.all_rains_median)
        generators.append(self.all_rains_1)
        generators.append(self.all_rains_max)

        inputs: List[Input] = []
        print("Generating inputs...")
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
