import random
from typing import List, Tuple, Union

from tqdm import tqdm

from generator_util import gen_tree, randint, randints


class Input:
    n: int
    m: int
    edges: List[Tuple[int, int]]

    def __init__(self, n: int, m: int, edges: List[Tuple[int, int]]) -> None:
        self.n = n
        self.m = m
        self.edges = edges


MultipleTestInput = List[Input]


class Bounds:
    lower: int
    upper: int

    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper


class Constraints:
    n: Bounds
    m: Bounds

    def __init__(self, n_bounds: Tuple[int, int], m_bounds: Tuple[int, int]) -> None:
        self.n = Bounds(*n_bounds)
        self.m = Bounds(*m_bounds)

    def validate(self, input: Union[Input, MultipleTestInput]) -> None:
        def validate_single(input: Input) -> None:
            assert self.n.lower <= input.n <= self.n.upper
            assert input.m == len(input.edges)
            assert self.m.lower <= input.m <= self.m.upper

        if type(input) == Input:
            validate_single(input)
        elif type(input) == MultipleTestInput:
            for input in input:
                validate_single(input)


class InputGenerator:
    generalConstraints = Constraints(n_bounds=(1, 2 * 10**5), m_bounds=(0, 2 * 10**5))

    ### IMPLEMENT GENERATORS BEGIN ###

    def random(self, n_bounds: Tuple[int, int], m_bounds: Tuple[int, int]) -> Input:
        constraints = Constraints(n_bounds, m_bounds)
        n = randint(constraints.n.lower, constraints.n.upper)
        m = randint(constraints.m.lower, constraints.m.upper)
        edges = [(randint(1, n), randint(1, n)) for _ in range(m)]
        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    def connected_random(self, n_bounds: Tuple[int, int], m_bounds: Tuple[int, int]) -> Input:
        constraints = Constraints(n_bounds, m_bounds)
        n = randint(constraints.n.lower, constraints.n.upper)
        m = randint(max(constraints.m.lower, n - 1), constraints.m.upper)
        edges = gen_tree(n)
        edges += [(randint(1, n), randint(1, n)) for _ in range(m - (n - 1))]
        random.shuffle(edges)
        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    def max_chain(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n.upper
        m = n - 1
        nodes = list(range(2, n + 1))
        random.shuffle(nodes)
        nodes = [1] + nodes
        edges = []
        for i in range(n - 1):
            u, v = nodes[i], nodes[i + 1]
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))

        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    def an_edge_case(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n.upper
        m = n - 1
        nodes = list(range(2, n + 1))
        random.shuffle(nodes)
        nodes = [1] + nodes
        edges = []
        for i in range(n - 1):
            u, v = nodes[min(i, 1)], nodes[i + 1]
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))

        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    def only_connected_to_first_few(self) -> Input:
        constraints = self.generalConstraints
        n = constraints.n.upper
        m = n - 1
        nodes = list(range(2, n + 1))
        random.shuffle(nodes)
        nodes = [1] + nodes
        edges = []
        for i in range(n - 1):
            u, v = nodes[randint(0, min(i, 10))], nodes[i + 1]
            if randint(0, 1):
                u, v = v, u
            edges.append((u, v))

        input = Input(n, m, edges)
        return self.validateAndReturn(input, constraints)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []

        for _ in range(3):
            generators.append(lambda: self.random(n_bounds=(1, 10), m_bounds=(0, 10**2)))
        for _ in range(3):
            generators.append(lambda: self.random(n_bounds=(10 + 1, 10**2), m_bounds=(0, 10**3)))
        for _ in range(3):
            generators.append(lambda: self.random(n_bounds=(10**2 + 1, 10**3), m_bounds=(0, 10**4)))
        for _ in range(3):
            generators.append(lambda: self.random(n_bounds=(10**3 + 1, 10**4), m_bounds=(0, 10**4)))
        for _ in range(3):
            generators.append(lambda: self.random(n_bounds=(10**4 + 1, 2 * 10**5), m_bounds=(0, 2 * 10**5)))
        for _ in range(3):
            generators.append(lambda: self.random(n_bounds=(2 * 10**5, 2 * 10**5), m_bounds=(2 * 10**5, 2 * 10**5)))

        generators.append(lambda: self.random(n_bounds=(2 * 10**5, 2 * 10**5), m_bounds=(0, 0)))

        for _ in range(3):
            generators.append(lambda: self.connected_random(n_bounds=(1, 10), m_bounds=(0, 10**2)))
        for _ in range(3):
            generators.append(lambda: self.connected_random(n_bounds=(10 + 1, 10**2), m_bounds=(0, 10**3)))
        for _ in range(3):
            generators.append(lambda: self.connected_random(n_bounds=(10**2 + 1, 10**3), m_bounds=(0, 10**4)))
        for _ in range(3):
            generators.append(lambda: self.connected_random(n_bounds=(10**3 + 1, 10**4), m_bounds=(0, 10**4)))
        for _ in range(3):
            generators.append(lambda: self.connected_random(n_bounds=(10**4 + 1, 2 * 10**5), m_bounds=(0, 2 * 10**5)))
        for _ in range(3):
            generators.append(
                lambda: self.connected_random(n_bounds=(2 * 10**5, 2 * 10**5), m_bounds=(2 * 10**5, 2 * 10**5))
            )

        generators.append(self.max_chain)
        generators.append(self.an_edge_case)

        for _ in range(5):
            generators.append(self.only_connected_to_first_few)

        inputs: List[Input] = []
        print("Generating inputs...")
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs

    def validateAndReturn(self, input: Input, constraints: Constraints):
        constraints.validate(input)
        self.generalConstraints.validate(input)
        return input
