import random
from collections import defaultdict
from string import ascii_lowercase
from typing import Callable, List, Literal, Tuple

from tqdm import tqdm

from util import randint, randints

Query1Type = Tuple[Literal[1], int]
Query2Type = Tuple[Literal[2], int, int]
QueryType = Query1Type | Query2Type


class Input:
    def __init__(self, s: str, queries: List[QueryType]) -> None:
        self.s = s
        self.queries = queries


N = 5 * 10**6
Q = 2 * 10**5

TARGET_STR = "inzvaolsundagerisiboskalp"


def random_type1_query(n: int) -> Query1Type:
    i = randint(1, n)
    return (1, i)


def type2_query_random(n: int) -> Query2Type:
    i, j = sorted(random.choices(range(1, n + 1), k=2))
    return (2, i, j)


def type2_query_max(n: int) -> Query2Type:
    return (2, 1, n)


def type2_query_same(n: int) -> Query2Type:
    i = randint(1, n)
    return (2, i, i)


def type2_query_long(n: int) -> Query2Type:
    length = randint(max(1, n - 10), n)
    i = randint(1, n - length + 1)
    j = i + length - 1
    return (2, i, j)


def get_random_type_2_query() -> Callable[[int], Query2Type]:
    return random.choice([type2_query_random, type2_query_max, type2_query_same, type2_query_long])


class InputGenerator:

    ### IMPLEMENT GENERATORS BEGIN ###

    def random(
        self,
        n_bounds: Tuple[
            int,
            int,
        ],
        q_bounds: Tuple[int, int],
        letters: str,
        type2_w: float,
    ) -> Input:
        s = "".join(random.choices(letters, k=randint(*n_bounds)))
        q = randint(*q_bounds)
        queries: List[QueryType] = []
        for _ in range(q - 1):
            q_type = random.choices([1, 2], [1 - type2_w, type2_w])[0]
            queries.append(random_type1_query(len(s)) if q_type == 1 else get_random_type_2_query()(len(s)))
        queries.append(type2_query_max(len(s)))
        return Input(s, queries)

    def all_type1_single_type2(
        self,
        n_bounds: Tuple[
            int,
            int,
        ],
        q_bounds: Tuple[int, int],
        letters: str,
    ) -> Input:
        s = "".join(random.choices(letters, k=randint(*n_bounds)))
        q = randint(*q_bounds)
        queries: List[QueryType] = []
        for _ in range(q - 1):
            i = randint(1, len(s))
            queries.append((1, i))
        queries.append((2, 1, len(s)))
        return Input(s, queries)

    def erase_from_beginning(
        self,
        n_bounds: Tuple[
            int,
            int,
        ],
        q_bounds: Tuple[int, int],
        letters: str,
        type2_w: float,
    ) -> Input:
        s = "".join(random.choices(letters, k=randint(*n_bounds)))
        q = randint(*q_bounds)
        queries: List[QueryType] = []
        erase_pos = 1
        for _ in range(q - 1):
            q_type = random.choices([1, 2], [1 - type2_w, type2_w])[0]
            if q_type == 1:
                queries.append((1, erase_pos))
                erase_pos += 1
                erase_pos = min(len(s), erase_pos)
            else:
                queries.append(get_random_type_2_query()(len(s)))
        queries.append(type2_query_max(len(s)))
        return Input(s, queries)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        print("Generating inputs...")
        inputs: List[Input] = []
        for type2_w in [0.5]:
            for _ in range(2):
                for letters in [ascii_lowercase, TARGET_STR]:
                    args = ((1, 10**2), (1, 10**2), letters, type2_w)
                    inputs.append(self.random(*args))
        for type2_w in [0.25, 0.5, 0.75, 1]:
            for _ in range(2):
                for letters in [ascii_lowercase, TARGET_STR]:
                    args = ((10**2 + 1, 10**4), (10**2 + 1, 10**4), ascii_lowercase, type2_w)
                    inputs.append(self.random(*args))
        for type2_w in [0.2, 0.8]:
            for letters in [ascii_lowercase, TARGET_STR]:
                args = ((10**5, 2 * 10**5), (10**5, 2 * 10**5), letters, type2_w)
                inputs.append(self.random(*args))
        for type2_w in [0.1, 0.5, 0.9]:
            for letters in [ascii_lowercase, TARGET_STR]:
                args = ((5 * 10**6, 5 * 10**6), (2 * 10**5, 2 * 10**5), letters, type2_w)
                inputs.append(self.random(*args))
                inputs.append(self.erase_from_beginning(*args))

        inputs.append(self.all_type1_single_type2((5 * 10**6, 5 * 10**6), (2 * 10**5, 2 * 10**5), ascii_lowercase))
        inputs.append(self.all_type1_single_type2((5 * 10**6, 5 * 10**6), (2 * 10**5, 2 * 10**5), TARGET_STR))

        return inputs
