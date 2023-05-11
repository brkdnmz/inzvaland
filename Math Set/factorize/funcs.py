from random import choice, randint
from typing import List, Tuple

from max_divisors import numbers_with_max_n_divisors
from numba import njit


@njit
def is_prime(num: int) -> bool:
    for i in range(2, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


@njit
def prev_prime(n: int) -> int:
    n -= 1
    while not is_prime(n):
        n -= 1
    return n


@njit
def next_prime(n: int) -> int:
    n += 1
    while not is_prime(n):
        n += 1
    return n


TestCase = Tuple[int, List[int]]
MOD = 10**9 + 7


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(2, self.N)
        return self.solve(n)

    def max(self) -> TestCase:
        n = self.N
        return self.solve(n)

    def max_prime(self) -> TestCase:
        n = prev_prime(self.N)
        return self.solve(n)

    def max_prime_times_2(self) -> TestCase:
        n = prev_prime(self.N // 2) * 2
        return self.solve(n)

    def max_product_of_large_primes(self) -> TestCase:
        smaller = int(self.N**0.5)
        larger = next_prime(smaller)
        smaller = prev_prime(smaller)
        while smaller * larger > self.N:
            smaller = prev_prime(smaller)

        n = smaller * larger
        return self.solve(n)

    def max_n_primes(self) -> TestCase:
        cur_prime = 2
        n = 1
        while n * cur_prime <= self.N:
            n *= cur_prime
            cur_prime = next_prime(cur_prime)
        return self.solve(n)

    def few_primes(self) -> TestCase:
        primes = [2, 3, 5, 7]
        cur = choice(primes)
        n = 1
        while n * cur <= self.N:
            n *= cur
            cur = choice(primes)
        return self.solve(n)

    def twos_power(self) -> TestCase:
        n = 1
        while n * 2 <= self.N:
            n *= 2
        return self.solve(n)

    def random_perfect_square(self) -> TestCase:
        n = randint(1, int(self.N**0.5)) ** 2
        return self.solve(n)

    def max_perfect_square(self) -> TestCase:
        n = int(self.N**0.5) ** 2
        return self.solve(n)

    def prime_square(self) -> TestCase:
        n = prev_prime(int(self.N**0.5)) ** 2
        return self.solve(n)

    def max_divisors(self) -> TestCase:
        n = numbers_with_max_n_divisors(self.N)[0]
        return self.solve(n)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.max,
            self.max_prime,
            self.max_prime_times_2,
            self.max_product_of_large_primes,
            self.max_n_primes,
            self.few_primes,
            self.twos_power,
            self.random_perfect_square,
            self.max_perfect_square,
            self.prime_square,
            self.max_divisors,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int) -> TestCase:
        self.validate(n)
        factorization = []
        init_n = n
        for d in range(2, n + 1):
            if d * d > n:
                break
            while n % d == 0:
                factorization.append(d)
                n //= d
        if n > 1:
            factorization.append(n)
        n = init_n
        return n, factorization

    def validate(self, n: int) -> None:
        assert 2 <= n <= self.N
