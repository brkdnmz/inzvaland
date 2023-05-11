from random import randint, shuffle
from typing import List, Tuple

from numba import njit


@njit
def is_prime(num: int) -> bool:
    for i in range(2, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


TestCase = Tuple[int, int, int]


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        h1 = randint(1, self.N)
        h2 = randint(1, self.N)
        return self.solve(h1, h2)

    def same_random(self) -> TestCase:
        h1 = randint(1, self.N)
        h2 = h1
        return self.solve(h1, h2)

    def same_max(self) -> TestCase:
        h1 = self.N
        h2 = self.N
        return self.solve(h1, h2)

    def same_max_prime(self) -> TestCase:
        h1 = self.N
        while not is_prime(h1):
            h1 -= 1
        h2 = h1
        return self.solve(h1, h2)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random done")
        all.append(self.same_random())
        print("same_random done")
        all.append(self.same_max())
        print("same_max done")
        all.append(self.same_max_prime())
        print("same_max_prime done")
        return all

    def solve(self, h1: int, h2: int) -> TestCase:
        smaller, larger = h1, h2
        if smaller > larger:
            smaller, larger = larger, smaller
        ans = (larger - smaller) // 2
        same_sum_products = []  # i * (h1 + h2 - i) for i <= h1
        for i in range(1, smaller + 1):
            j = h1 + h2 - i
            same_sum_products.append(i * j)
        product = h1 * h2
        same_product_sums = []
        for i in range(1, product + 1):
            if i * i > product:
                break
            if product % i:
                continue
            same_product_sums.append(i + product // i)
        ans += len(set([h1 + h2, *same_product_sums, *same_sum_products]))
        self.validate(h1, h2, ans)
        return h1, h2, ans

    def validate(self, h1: int, h2: int, ans: int) -> None:
        assert 1 <= h1 <= self.N and 1 <= h2 <= self.N
        futures = set()
        futures.add(h1 + h2)
        for i in range(1, h1 + h2):
            futures.add(i * (h1 + h2 - i))
        product = h1 * h2
        for i in range(1, product + 1):
            if i * i > product:
                break
            if product % i:
                continue
            futures.add(i + product // i)
        print(ans, len(futures))
        assert ans == len(futures)
