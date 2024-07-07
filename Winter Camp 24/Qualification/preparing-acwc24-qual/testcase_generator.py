import random
from typing import List

from tqdm import tqdm

from generator_util import randint, randints


class Input:
    n: int
    p: List[int]
    t: List[int]

    def __init__(self, n: int, p: List[int], t: List[int]) -> None:
        self.n = n
        self.p = p
        self.t = t


class Bounds:
    lower: int
    upper: int

    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper


class Constraints:
    n_bounds: Bounds
    p_bounds: Bounds
    t_bounds: Bounds

    def __init__(self, n_bounds: Bounds, p_bounds: Bounds, t_bounds: Bounds) -> None:
        self.n_bounds = n_bounds
        self.p_bounds = p_bounds
        self.t_bounds = t_bounds

    # This method will be used to validate inputs.
    def validate(self, input: Input) -> None:
        assert self.n_bounds.lower <= input.n <= self.n_bounds.upper
        assert input.n == len(input.p) == len(input.t)
        assert (self.p_bounds.lower <= x <= self.p_bounds.upper for x in input.p)
        assert (self.t_bounds.lower <= x <= self.t_bounds.upper for x in input.t)


class InputGenerator:
    generalConstraints = Constraints(n_bounds=Bounds(1, 20), p_bounds=Bounds(1, 10**8), t_bounds=Bounds(1, 10**8))

    ### IMPLEMENT GENERATORS BEGIN ###

    def all_random(self) -> Input:
        constraints = self.generalConstraints
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        p = randints(n, constraints.p_bounds.lower, constraints.p_bounds.upper)
        t = randints(n, constraints.t_bounds.lower, constraints.t_bounds.upper)
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def small_random(self) -> Input:
        constraints = Constraints(n_bounds=Bounds(1, 5), p_bounds=Bounds(1, 10**3), t_bounds=Bounds(1, 10**3))
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        p = randints(n, constraints.p_bounds.lower, constraints.p_bounds.upper)
        t = randints(n, constraints.t_bounds.lower, constraints.t_bounds.upper)
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def mid_random(self) -> Input:
        constraints = Constraints(n_bounds=Bounds(6, 10), p_bounds=Bounds(1, 10**3), t_bounds=Bounds(1, 10**3))
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        p = randints(n, constraints.p_bounds.lower, constraints.p_bounds.upper)
        t = randints(n, constraints.t_bounds.lower, constraints.t_bounds.upper)
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def large_random(self) -> Input:
        constraints = Constraints(n_bounds=Bounds(11, 20), p_bounds=Bounds(1, 10**3), t_bounds=Bounds(1, 10**3))
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        p = randints(n, constraints.p_bounds.lower, constraints.p_bounds.upper)
        t = randints(n, constraints.t_bounds.lower, constraints.t_bounds.upper)
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def max_random(self) -> Input:
        constraints = Constraints(
            n_bounds=Bounds(20, 20),
            p_bounds=Bounds(1, self.generalConstraints.p_bounds.upper),
            t_bounds=Bounds(1, self.generalConstraints.t_bounds.upper),
        )
        n = randint(constraints.n_bounds.lower, constraints.n_bounds.upper)
        p = randints(n, constraints.p_bounds.lower, constraints.p_bounds.upper)
        t = randints(n, constraints.t_bounds.lower, constraints.t_bounds.upper)
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def n_max(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n_bounds.upper
        p = randints(n, constraints.p_bounds.lower, constraints.p_bounds.upper)
        t = randints(n, constraints.t_bounds.lower, constraints.t_bounds.upper)
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def n_max_all_min(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n_bounds.upper
        p = [constraints.p_bounds.lower] * n
        t = [constraints.t_bounds.lower] * n
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def all_max(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n_bounds.upper
        p = [constraints.p_bounds.upper] * n
        t = [constraints.t_bounds.upper] * n
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    def half_min_half_max(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n_bounds.upper
        p = [constraints.p_bounds.lower] * n
        t = [constraints.t_bounds.upper] * (n // 2) + [constraints.t_bounds.lower] * (n - n // 2)
        input = Input(n, p, t)
        return self.validateAndReturn(input, constraints)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []
        for _ in range(3):
            generators.append(self.all_random)
        for _ in range(3):
            generators.append(self.small_random)
        for _ in range(3):
            generators.append(self.mid_random)
        for _ in range(5):
            generators.append(self.large_random)
        for _ in range(10):
            generators.append(self.max_random)
        for _ in range(10):
            generators.append(self.n_max)

        generators.append(self.n_max_all_min)
        generators.append(self.all_max)
        generators.append(self.half_min_half_max)

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
