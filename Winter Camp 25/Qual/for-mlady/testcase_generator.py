import random
from typing import List, Tuple

from tqdm import tqdm

from util import make_square_free, next_prime, prev_prime, randint, randints

Query = Tuple[int, int, int]


class Input:
    def __init__(self, q: int, queries: List[Query]) -> None:
        self.q = q
        self.queries = queries


MultipleTestInput = List[Input]

N = 10**7
K = 10**7
Q = 5 * 10**5


class InputGenerator:

    ### IMPLEMENT GENERATORS BEGIN ###

    def small_random(self) -> Input:
        q = 10**4
        queries = []
        for _ in range(q):
            l, r = sorted(random.choices(range(1, 100 + 1), k=2))
            k = make_square_free(randint(2, 100 + 1))
            queries.append((l, r, k))
        return Input(q, queries)

    def mid_random(self) -> Input:
        q = 10**5
        queries = []
        for _ in range(q):
            l, r = sorted(random.choices(range(1, 10**5 + 1), k=2))
            k = make_square_free(randint(2, 10**4 + 1))
            queries.append((l, r, k))
        return Input(q, queries)

    def max_random(self) -> Input:
        q = Q
        queries = []
        for _ in range(q):
            l, r = sorted(random.choices(range(1, N + 1), k=2))
            k = make_square_free(randint(2, K + 1))
            queries.append((l, r, k))
        return Input(q, queries)

    def max_prime(self) -> Input:
        q = Q
        queries = []
        k = prev_prime(K)
        for _ in range(q):
            l, r = sorted(random.choices(range(1, N + 1), k=2))
            queries.append((l, r, k))
        return Input(q, queries)

    def distinct_primes(self) -> Input:
        q = Q
        queries = []
        k = K
        for _ in range(q):
            l, r = sorted(random.choices(range(1, N + 1), k=2))
            k = prev_prime(k)
            queries.append((l, r, k))
            if k == 2:
                k = K
        return Input(q, queries)

    def min_prime(self) -> Input:
        q = Q
        queries = []
        for _ in range(q):
            l, r = sorted(random.choices(range(1, N + 1), k=2))
            k = 2
            queries.append((l, r, k))
        return Input(q, queries)

    def max_ranges_max_prime(self) -> Input:
        q = Q
        queries = []
        k = prev_prime(K)
        for _ in range(q):
            l, r = 1, N
            queries.append((l, r, k))
        return Input(q, queries)

    def max_ranges_min_prime(self) -> Input:
        q = Q
        queries = []
        for _ in range(q):
            l, r = 1, N
            k = 2
            queries.append((l, r, k))
        return Input(q, queries)

    def max_ranges_distinct_primes(self) -> Input:
        q = Q
        queries = []
        k = K
        for _ in range(q):
            l, r = 1, N
            k = prev_prime(k)
            queries.append((l, r, k))
            if k == 2:
                k = K
        return Input(q, queries)

    def min_ranges_distinct_primes(self) -> Input:
        q = Q
        queries = []
        k = K
        for _ in range(q):
            l = randint(1, N)
            r = l
            k = prev_prime(k)
            queries.append((l, r, k))
            if k == 2:
                k = K
        return Input(q, queries)

    def max_number_of_prime_divisors(self) -> Input:
        q = Q
        queries = []
        k = 1
        p = 2
        while k * p <= N:
            k *= p
            p = next_prime(p)
        for _ in range(q):
            l, r = sorted(random.choices(range(1, N + 1), k=2))
            queries.append((l, r, k))
        return Input(q, queries)

    ### IMPLEMENT GENERATORS END ###

    def generate(self) -> List[Input]:
        generators = []

        generators.append(self.small_random)
        generators.append(self.mid_random)
        generators.append(self.max_random)
        generators.append(self.max_prime)
        generators.append(self.distinct_primes)
        generators.append(self.min_prime)
        generators.append(self.max_ranges_max_prime)
        generators.append(self.max_ranges_min_prime)
        generators.append(self.max_ranges_distinct_primes)
        generators.append(self.min_ranges_distinct_primes)
        generators.append(self.max_number_of_prime_divisors)

        print("Generating inputs...")
        inputs: List[Input] = []
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
