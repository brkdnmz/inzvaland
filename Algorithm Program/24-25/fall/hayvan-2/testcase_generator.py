import random
from typing import List, Literal

from tqdm import tqdm

from util import randint, randints


class Input:
    def __init__(self, n: int, a: List[int], q: int, guesses: List[int]) -> None:
        self.n = n
        self.a = a
        self.q = q
        self.guesses = guesses


MultipleTestInput = List[Input]


class InputGenerator:

    ### IMPLEMENT GENERATORS BEGIN ###

    def small_random(self) -> Input:
        n = randint(2, 10**2)
        a = randints(n, 1, 10**9)
        q = 10**2
        guesses = randints(q, 1, n)
        return Input(n, a, q, guesses)

    def mid_random(self) -> Input:
        n = randint(10**2 + 1, 10**4)
        a = randints(n, 1, 10**9)
        q = 10**2
        guesses = randints(q, 1, n)
        return Input(n, a, q, guesses)

    def max_random(self) -> Input:
        n = 2 * 10**5
        a = randints(n, 1, 10**9)
        q = 2 * 10**5
        guesses = randints(q, 1, n)
        return Input(n, a, q, guesses)

    def all_guesses(self) -> Input:
        n = 2 * 10**5
        a = randints(n, 1, 10**9)
        q = 2 * 10**5
        guesses = list(range(1, n + 1))
        return Input(n, a, q, guesses)

    def all_same(self) -> Input:
        n = 2 * 10**5
        a = [randint(1, 10**9)] * n
        q = 2 * 10**5
        guesses = list(range(1, n + 1))
        return Input(n, a, q, guesses)

    def endpoints_different_small(self) -> Input:
        n = 2 * 10**5
        a = [1] + [randint(2, n)] * (n - 2) + [1]
        q = 2 * 10**5
        guesses = [
            random.choice([n // 2, n // 2 - 1, n // 2 + 1]) for _ in range(q - 2)
        ]
        guesses.append(1)
        guesses.append(n)
        return Input(n, a, q, guesses)

    def endpoints_different_big(self) -> Input:
        n = 2 * 10**5
        a = [10**9] + [1] * (n - 2) + [10**9]
        q = 2 * 10**5
        guesses = [
            random.choice([n // 2, n // 2 - 1, n // 2 + 1]) for _ in range(q - 2)
        ]
        guesses.append(1)
        guesses.append(n)
        return Input(n, a, q, guesses)

    def min_max_mid(self) -> Input:
        n = 2 * 10**5
        mn = 2
        mx = 10**9
        mid = (mn + mx) // 2
        a = random.choices([mn, mx, mid], weights=[1, 1, 10**4], k=n)
        q = 2 * 10**5
        guesses = list(range(1, n + 1))
        return Input(n, a, q, guesses)

    def min_max(self) -> Input:
        n = 2 * 10**5
        mn = 2
        mx = 10**9
        a = [mn] * (n // 2) + [mx] * (n // 2)
        q = 2 * 10**5
        guesses = list(range(1, n + 1))
        return Input(n, a, q, guesses)

    def min_max_randomly_dist(self) -> Input:
        n = 2 * 10**5
        mn = 2
        mx = 10**9
        a = random.choices([mn, mx], k=n)
        q = 2 * 10**5
        guesses = list(range(1, n + 1))
        return Input(n, a, q, guesses)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []

        for _ in range(5):
            generators.append(self.small_random)
        for _ in range(5):
            generators.append(self.mid_random)
        for _ in range(5):
            generators.append(self.max_random)
        generators.append(self.all_guesses)
        generators.append(self.all_same)
        generators.append(self.endpoints_different_small)
        generators.append(self.endpoints_different_big)
        for _ in range(3):
            generators.append(self.min_max_mid)
            generators.append(self.min_max_mid)
            generators.append(self.min_max_mid)

        generators.append(self.min_max)
        generators.append(self.min_max_randomly_dist)

        print("Generating inputs...")
        inputs: List[Input] = []
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
