from math import isqrt
from random import choice, choices, randint, sample
from typing import Dict, List, Tuple, Type

from numba import njit

TestCase = Tuple[Tuple[int, List[int], List[int]], float]


class Generator:
    def __init__(self, D: int, N: int) -> None:
        self.D = D
        self.N = N

    def random(self) -> TestCase:
        d = randint(1, self.D)
        otis = choices(range(1, self.N+1), k=3)
        maeve = choices(range(1, self.N+1), k=4)
        return self.solve(d, otis, maeve)

    def d_max_others_min(self) -> TestCase:
        d = self.D
        otis = [1]*3
        maeve = [1]*4
        return self.solve(d, otis, maeve)
    def d_min_others_max(self) -> TestCase:
        d = 1
        otis = [self.N]*3
        maeve = [self.N]*4
        return self.solve(d, otis, maeve)

    def d_large(self) -> TestCase:
        d = randint(self.D//2, self.D)
        otis = choices(range(1, self.N+1), k=3)
        maeve = choices(range(1, self.N+1), k=4)
        return self.solve(d, otis, maeve)

    def d_small(self) -> TestCase:
        d = randint(1, isqrt(self.D))
        otis = choices(range(1, self.N+1), k=3)
        maeve = choices(range(1, self.N+1), k=4)
        return self.solve(d, otis, maeve)

    def d_large_others_small(self) -> TestCase:
        d = randint(self.D//2, self.D)
        otis = choices(range(1, isqrt(self.N) + 1), k=3)
        maeve = choices(range(1, isqrt(self.N) + 1), k=4)
        return self.solve(d, otis, maeve)

    def d_small_others_large(self) -> TestCase:
        d = randint(1, isqrt(self.D))
        otis = choices(range(self.N//2, self.N+1), k=3)
        maeve = choices(range(self.N//2, self.N+1), k=4)
        return self.solve(d, otis, maeve)

    def all_max(self) -> TestCase:
        d = self.D
        otis = [self.N]*3
        maeve = [self.N]*4
        return self.solve(d, otis, maeve)

    def all_min(self) -> TestCase:
        d = 1
        otis = [1]*3
        maeve = [1]*4
        return self.solve(d, otis, maeve)


    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random,
            self.random,
            self.d_max_others_min,
            self.d_min_others_max,
            self.d_large,
            self.d_small,
            self.d_large_others_small,
            self.d_small_others_large,
            self.all_max,
            self.all_min,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, d: int, otis: List[int], maeve: List[int]) -> TestCase:
        self.validate(d, otis, maeve)
        l, r = 0, d
        for i in range(10**5):
            mid = (l+r)/2
            otis_after_mid = 0
            for x in otis:
                otis_after_mid = mid * otis_after_mid + x
            otis_after_mid *= mid
            maeve_after_mid = 0
            for x in maeve:
                maeve_after_mid = mid * maeve_after_mid + x
            maeve_after_mid *= mid
            if d < otis_after_mid + maeve_after_mid:
                r = mid
            else:
                l = mid
        return (d, otis, maeve), l

    def validate(self, d: int, otis: List[int], maeve: List[int]) -> None:
        assert 1 <= d <= self.D
        assert len(otis) == 3
        assert len(maeve) == 4
        assert (1 <= x <= self.N for x in otis)
        assert (1 <= x <= self.N for x in maeve)
