from math import floor, log2
from typing import List

from tqdm import tqdm

from util import prev_prime, randint, randints


class Input:
    k: int
    s: int
    m: List[int]

    def __init__(self, k: int, s: int, m: List[int]) -> None:
        self.k = k
        self.s = s
        self.m = m


K = 10**14
S = 10**6
M = 10**7


class InputGenerator:

    def small_random(self) -> Input:
        k = randint(1, 10**5)
        s = randint(1, 20)
        m = randints(s, 1, 5)
        input = Input(k, s, m)
        return input

    def mid_random(self) -> Input:
        k = randint(10**5 + 1, 10**9)
        s = randint(20 + 1, 10**3)
        m = randints(s, 5 + 1, 10**5)
        input = Input(k, s, m)
        return input

    def max_random(self) -> Input:
        k = prev_prime(K)
        s = S
        m = randints(s, 10**5 + 1, M)
        input = Input(k, s, m)
        return input

    def only_twos_powers(self) -> Input:
        k = 2 ** randint(0, floor(log2(K)))
        s = S
        m = [2**e for e in randints(s, 0, floor(log2(M)))]
        input = Input(k, s, m)
        return input

    def twos_max_power(self) -> Input:
        k = 2 ** floor(log2(K))
        s = S
        m = [2 ** floor(log2(M))] * s
        input = Input(k, s, m)
        return input

    def max_prime(self) -> Input:
        k = 2 ** floor(log2(K))
        s = S
        m = [prev_prime(M)] * s
        input = Input(k, s, m)
        return input

    def random_max_primes(self) -> Input:
        k = 2 ** floor(log2(K))
        cur_prime = M
        primes = []
        n_primes = 10**5
        for _ in range(n_primes):
            cur_prime = prev_prime(cur_prime)
            primes.append(cur_prime)
        s = S
        m = []
        for _ in range(s // 3):
            m.append(primes[randint(0, n_primes // 3 - 1)])
        for _ in range(s // 3):
            m.append(primes[randint(n_primes // 3, 2 * n_primes // 3 - 1)])
        for _ in range(s - 2 * (s // 3)):
            m.append(primes[randint(2 * n_primes // 3, n_primes - 1)])
        input = Input(k, s, m)
        return input

    def primes_decreasing(self) -> Input:
        k = 2 ** floor(log2(K))
        cur_p = M
        m = []
        while cur_p > 2:
            cur_p = prev_prime(cur_p)
            m.append(cur_p)
        s = len(m)
        input = Input(k, s, m)
        return input

    def k_max_prime_then_twos_powers(self) -> Input:
        k = prev_prime(K)
        s = S
        m = [2**e for e in randints(s, 0, floor(log2(M)))]
        input = Input(k, s, m)
        return input

    def smart_random(self) -> Input:
        k = prev_prime(K)
        cur_p = M // 2
        half_primes = []
        while cur_p > 2:
            cur_p = prev_prime(cur_p)
            half_primes.append(cur_p)
        s = S
        m = [half_primes[randint(0, min(i, len(half_primes) - 1))] for i in range(s)]
        for i in range(s):
            if not randint(0, 9):
                m[i] *= 2
        input = Input(k, s, m)
        return input

    def generate(self) -> List[Input]:
        generators = []

        for _ in range(5):
            generators.append(self.small_random)
        for _ in range(5):
            generators.append(self.mid_random)
        for _ in range(2):
            generators.append(self.max_random)

        generators.append(self.only_twos_powers)
        generators.append(self.twos_max_power)
        generators.append(self.max_prime)
        generators.append(self.random_max_primes)
        generators.append(self.primes_decreasing)
        generators.append(self.k_max_prime_then_twos_powers)
        generators.append(self.smart_random)

        inputs: List[Input] = []
        print("Generating inputs...")
        for generate in tqdm(generators):
            inputs.append(generate())
        return inputs
