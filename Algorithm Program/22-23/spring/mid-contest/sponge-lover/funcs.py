from random import choice, choices, randint, sample
from typing import Dict, List, Tuple, Type

from numba import njit

TestCase = Tuple[Tuple[int, List[int], List[int]], List[int]]


class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.seg = [0] * (4 * n + 5)

    def get(self, tl: int, tr: int) -> int:
        return self.__get(1, 0, self.n - 1, tl, tr)

    def __get(self, c: int, l: int, r: int, tl: int, tr: int) -> int:
        if tl > r or tr < l:
            return 0
        if tl <= l and r <= tr:
            return self.seg[c]
        mid = (l + r) >> 1
        return self.__get(2 * c, l, mid, tl, tr) + self.__get(2 * c + 1, mid + 1, r, tl, tr)

    def add(self, target: int, val: int):
        self.__add(1, 0, self.n - 1, target, val)

    def __add(self, c: int, l: int, r: int, target: int, val: int):
        if not (l <= target <= r):
            return
        if l == r:
            self.seg[c] += val
            return
        mid = (l + r) >> 1
        self.__add(2 * c, l, mid, target, val)
        self.__add(2 * c + 1, mid + 1, r, target, val)
        self.seg[c] = self.seg[2 * c] + self.seg[2 * c + 1]


def get_ranks(l: List[int]) -> List[int]:
    n = len(l)
    id_to_rank = [0] * n
    l_with_ids = [(x, i) for i, x in enumerate(l)]
    l_with_ids.sort()
    for sorted_i, (x, i) in enumerate(l_with_ids):
        id_to_rank[i] = sorted_i
    return id_to_rank


LIMIT = 10**9


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(self.N // 2, self.N)
        dishes = sample(range(1, LIMIT + 1), k=n)
        sponges = sample(range(1, LIMIT + 1), k=n)
        return self.solve(n, dishes, sponges)

    def max_random(self) -> TestCase:
        n = self.N
        dishes = sample(range(1, LIMIT + 1), k=n)
        sponges = sample(range(1, LIMIT + 1), k=n)
        return self.solve(n, dishes, sponges)

    def dishes_sorted(self) -> TestCase:
        n = self.N
        dishes = sorted(sample(range(1, LIMIT + 1), k=n))
        sponges = sample(range(1, LIMIT + 1), k=n)
        return self.solve(n, dishes, sponges)

    def sponges_sorted(self) -> TestCase:
        n = self.N
        dishes = sorted(sample(range(1, LIMIT + 1), k=n))
        sponges = sorted(sample(range(1, LIMIT + 1), k=n))
        return self.solve(n, dishes, sponges)

    def dishes_sorted_reverse(self) -> TestCase:
        n = self.N
        dishes = sorted(sample(range(1, LIMIT + 1), k=n), reverse=True)
        sponges = sorted(sample(range(1, LIMIT + 1), k=n))
        return self.solve(n, dishes, sponges)

    def sponges_sorted_reverse(self) -> TestCase:
        n = self.N
        dishes = sorted(sample(range(1, LIMIT + 1), k=n))
        sponges = sorted(sample(range(1, LIMIT + 1), k=n), reverse=True)
        return self.solve(n, dishes, sponges)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        methods = (
            self.random,
            self.random,
            self.max_random,
            self.max_random,
            self.dishes_sorted,
            self.sponges_sorted,
            self.dishes_sorted_reverse,
            self.sponges_sorted_reverse,
        )

        for method in methods:
            all.append(method())
            print(f"{method.__name__} done")
        return all

    def solve(self, n: int, dishes: List[int], sponges: List[int]) -> TestCase:
        segtree = SegTree(n)
        dish_id_to_rank = get_ranks(dishes)
        sponge_id_to_rank = get_ranks(sponges)
        sponge_rank_to_id = [0] * n
        for i, rank in enumerate(sponge_id_to_rank):
            sponge_rank_to_id[rank] = i
        sponge_orders = []
        for dish_i in range(n):
            nth_dish = dish_id_to_rank[dish_i]
            nth_sponge = sponge_rank_to_id[nth_dish]
            sponge_orders.append(nth_sponge - segtree.get(0, nth_sponge) + 1)
            segtree.add(nth_sponge, 1)
        return (n, dishes, sponges), sponge_orders

    def validate(self, n: int, dishes: List[int], sponges: List[int]) -> None:
        assert 1 <= n <= self.N
        assert len(dishes) == n and len(sponges) == n
        assert len(set(dishes)) == n and len(set(sponges)) == n
        assert (1 <= x <= LIMIT for x in dishes)
        assert (1 <= x <= LIMIT for x in sponges)
