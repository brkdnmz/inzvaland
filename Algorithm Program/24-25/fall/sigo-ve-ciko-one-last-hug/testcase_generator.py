import random
from typing import List, Tuple

from tqdm import tqdm

from util import gen_range, randint, randints

Query = Tuple[int, int]


class Input:
    def __init__(self, n: int, a: str, s: int, scenarios: List[Query]) -> None:
        self.n = n
        self.a = a
        self.s = s
        self.scenarios = scenarios


MultipleTestInput = List[Input]
N = 5 * 10**5
S = 5 * 10**5


def gen_random_query_type(n: int):
    p = random.random()

    if p <= 0.15:
        q = gen_range(0, n + 1)
    elif p <= 0.35:
        q = gen_range(0, n + 1, max_length=max(1, n // 100))
    elif p <= 0.55:
        q = gen_range(0, n + 1, min_length=max(1, n // 2))
    elif p <= 0.65:
        q = gen_range(0, n + 1, min_length=max(1, 9 * n // 10))
    elif p <= 0.80:
        q = gen_range(0, n + 1, min_length=max(1, 99 * n // 100))
    elif p <= 0.90:
        q = gen_range(0, n + 1, min_length=max(1, n - 100))
    elif p <= 0.9999:
        q = gen_range(0, n + 1, max_length=1)
    else:
        q = (0, n + 1)

    return q


class InputGenerator:
    ### IMPLEMENT GENERATORS BEGIN ###

    def small_random(self) -> MultipleTestInput:
        t = 5000
        testcases = []
        for _ in range(t):
            n = randint(1, 10**2)
            a = "".join(
                random.choices(
                    ["S", "C"], k=n, weights=[randint(1, 10), randint(1, 10)]
                )
            )
            s = randint(1, 10**2)
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def mid_random(self) -> MultipleTestInput:
        t = 500
        testcases = []
        for _ in range(t):
            n = randint(10**2 + 1, 10**3)
            a = "".join(
                random.choices(
                    ["S", "C"], k=n, weights=[randint(1, 10), randint(1, 10)]
                )
            )
            s = randint(10**2 + 1, 10**3)
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def big_random(self) -> MultipleTestInput:
        t = 50
        testcases = []
        for _ in range(t):
            n = randint(10**3 + 1, 10**4)
            a = "".join(
                random.choices(["S", "C"], k=n, weights=[randint(1, 5), randint(1, 5)])
            )
            s = randint(10**3 + 1, 10**4)
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def large_random(self) -> MultipleTestInput:
        t = 5
        testcases = []
        for _ in range(t):
            n = randint(10**4 + 1, 10**5)
            a = "".join(
                random.choices(["S", "C"], k=n, weights=[randint(1, 5), randint(1, 5)])
            )
            s = randint(10**4 + 1, 10**5)
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def max_random(self) -> MultipleTestInput:
        t = 1
        testcases = []
        for _ in range(t):
            n = 5 * 10**5
            a = "".join(random.choices(["S", "C"], k=n))
            s = 5 * 10**5
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def max_c_major(self) -> MultipleTestInput:
        t = 1
        testcases = []
        for _ in range(t):
            n = 5 * 10**5
            a = "".join(random.choices(["S", "C"], k=n, weights=[1, 10**4]))
            s = 5 * 10**5
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def max_s_major(self) -> MultipleTestInput:
        t = 1
        testcases = []
        for _ in range(t):
            n = 5 * 10**5
            a = "".join(random.choices(["S", "C"], k=n, weights=[10**4, 1]))
            s = 5 * 10**5
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def max_all_c(self) -> MultipleTestInput:
        t = 1
        testcases = []
        for _ in range(t):
            n = 5 * 10**5
            a = "C" * n
            s = 5 * 10**5
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def max_all_s(self) -> MultipleTestInput:
        t = 1
        testcases = []
        for _ in range(t):
            n = 5 * 10**5
            a = "S" * n
            s = 5 * 10**5
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def max_alternating(self) -> MultipleTestInput:
        t = 1
        testcases = []
        for _ in range(t):
            n = 5 * 10**5
            a = "SC" * (n // 2)
            s = 5 * 10**5
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    def max_almost_alternating(self) -> MultipleTestInput:
        t = 1
        testcases = []
        for _ in range(t):
            n = 5 * 10**5
            a = list("SC" * (n // 2))
            for i in range(1000):
                pos = randint(0, n - 1)
                a[pos] = "S" if a[pos] == "C" else "C"
            a = "".join(a)
            s = 5 * 10**5
            scenarios = []
            for _ in range(s):
                scenarios.append(random.sample(gen_random_query_type(n), k=2))
            testcases.append(Input(n, a, s, scenarios))
        return testcases

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[MultipleTestInput]:
        generators = []
        generators.append(self.small_random)
        generators.append(self.mid_random)
        generators.append(self.big_random)
        generators.append(self.large_random)
        generators.append(self.max_random)
        generators.append(self.max_c_major)
        generators.append(self.max_s_major)
        generators.append(self.max_all_c)
        generators.append(self.max_all_s)
        generators.append(self.max_alternating)
        generators.append(self.max_almost_alternating)

        # print("Generating inputs...")
        inputs: List[MultipleTestInput] = []
        for generate in tqdm(generators, "Generating inputs"):
            inputs.append(generate())
        return inputs
