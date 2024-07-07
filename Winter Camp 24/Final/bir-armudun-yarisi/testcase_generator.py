import random
from typing import List

from tqdm import tqdm

from generator_util import randint, randints


class Input:
    n: int
    a: List[int]

    def __init__(self, n: int, a: List[int]) -> None:
        self.n = n
        self.a = a


class Bounds:
    lower: int
    upper: int

    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper


class Constraints:
    n_bounds: Bounds
    a_bounds: Bounds

    def __init__(self, n_bounds: Bounds, a_bounds: Bounds) -> None:
        self.n_bounds = n_bounds
        self.a_bounds = a_bounds

    # This method will be used to validate inputs.
    def validate(self, input: Input) -> None:
        assert self.n_bounds.lower <= input.n <= self.n_bounds.upper
        assert input.n == len(input.a)
        assert (self.a_bounds.lower <= x <= self.a_bounds.upper for x in input.a)


class InputGenerator:
    MOD = 10**9 + 7
    generalConstraints = Constraints(n_bounds=Bounds(1, 50), a_bounds=Bounds(0, MOD - 1))

    ### IMPLEMENT GENERATORS BEGIN ###

    def all_random(self) -> Input:
        constraints = self.generalConstraints
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        a = randints(n, constraints.a_bounds.lower, constraints.a_bounds.upper)
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    def small_random(self) -> Input:
        constraints = Constraints(n_bounds=Bounds(1, 10), a_bounds=self.generalConstraints.a_bounds)
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        a = randints(n, constraints.a_bounds.lower, constraints.a_bounds.upper)
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    def mid_random(self) -> Input:
        constraints = Constraints(n_bounds=Bounds(11, 30), a_bounds=self.generalConstraints.a_bounds)
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        a = randints(n, constraints.a_bounds.lower, constraints.a_bounds.upper)
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    def big_random(self) -> Input:
        constraints = Constraints(n_bounds=Bounds(31, 45), a_bounds=self.generalConstraints.a_bounds)
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        a = randints(n, constraints.a_bounds.lower, constraints.a_bounds.upper)
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    def large_random(self) -> Input:
        constraints = Constraints(
            n_bounds=Bounds(45, self.generalConstraints.n_bounds.upper), a_bounds=self.generalConstraints.a_bounds
        )
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        a = randints(n, constraints.a_bounds.lower, constraints.a_bounds.upper)
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    def n_max(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n_bounds.upper
        a = randints(n, constraints.a_bounds.lower, constraints.a_bounds.upper)
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    def n_max_all_min(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n_bounds.upper
        a = [constraints.a_bounds.lower] * n
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    def all_max(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n_bounds.upper
        a = [constraints.a_bounds.upper] * n
        input = Input(n, a)
        return self.validateAndReturn(input, constraints)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []
        for _ in range(10):
            generators.append(self.all_random)
        for _ in range(10):
            generators.append(self.small_random)
        for _ in range(10):
            generators.append(self.mid_random)
        for _ in range(10):
            generators.append(self.big_random)
        for _ in range(10):
            generators.append(self.large_random)
        for _ in range(10):
            generators.append(self.n_max)

        generators.append(self.n_max_all_min)
        generators.append(self.all_max)

        inputs: List[Input] = []
        print("Generating inputs...")
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs

    # Each generator should return by calling this method.
    def validateAndReturn(self, input: Input, constraints: Constraints):
        constraints.validate(input)
        self.generalConstraints.validate(input)  # Any input must satisfy the general constraints.
        return input
