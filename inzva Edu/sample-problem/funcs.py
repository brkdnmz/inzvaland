from collections import defaultdict
from math import gcd
from random import choice, choices, randint
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


@njit
def prev_prime(n: int) -> int:
    while not is_prime(n):
        n -= 1
    return n


@njit
def next_prime(n: int) -> int:
    n += 1
    while not is_prime(n):
        n += 1
    return n


# ((n, m, grid), answer)
Grid = List[List[str]]
TestCase = Tuple[Tuple[int, int, Grid], int]
MOD = 10**9 + 7

# 2D Grid w/ obstacles


class Generator:
    def __init__(self, N: int) -> None:
        self.N = N

    def random(self) -> TestCase:
        n = randint(1, self.N)  # randint(a, b) -> [a, b]
        m = randint(1, self.N)
        grid = [["."] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                is_not_obstacle = randint(0, 1)
                if not is_not_obstacle:
                    grid[i][j] = "#"
        return self.solve(n, m, grid)

    def random_less_obstacles(self) -> TestCase:
        n = randint(1, self.N)
        m = randint(1, self.N)
        grid = [["."] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                is_not_obstacle = randint(0, 2)
                if not is_not_obstacle:
                    grid[i][j] = "#"
        return self.solve(n, m, grid)

    def random_even_less_obstacles(self) -> TestCase:
        n = randint(1, self.N)
        m = randint(1, self.N)
        grid = [["."] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                is_not_obstacle = randint(0, 5)
                if not is_not_obstacle:
                    grid[i][j] = "#"
        return self.solve(n, m, grid)

    def max(self) -> TestCase:
        n = self.N
        m = self.N
        grid = [["."] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                is_not_obstacle = randint(0, 10)
                if not is_not_obstacle:
                    grid[i][j] = "#"
        return self.solve(n, m, grid)

    def n_1(self) -> TestCase:
        n = 1
        m = self.N
        grid = [["."] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                is_not_obstacle = randint(0, 10)
                if not is_not_obstacle:
                    grid[i][j] = "#"
        return self.solve(n, m, grid)

    def m_1(self) -> TestCase:
        n = self.N
        m = 1
        grid = [["."] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                is_not_obstacle = randint(0, 10)
                if not is_not_obstacle:
                    grid[i][j] = "#"
        return self.solve(n, m, grid)

    def no_obstacles(self) -> TestCase:
        n = self.N
        m = randint(self.N // 2, self.N)
        grid = [["."] * m for _ in range(n)]
        return self.solve(n, m, grid)

    def all_obstacles(self) -> TestCase:
        n = self.N
        m = randint(self.N // 2, self.N)
        grid = [["#"] * m for _ in range(n)]
        return self.solve(n, m, grid)

    def generate_all(self) -> List[TestCase]:
        all: list[TestCase] = []
        all.append(self.random())
        print("random finished")
        all.append(self.random_less_obstacles())
        print("random_less_obstacles finished")
        all.append(self.random_even_less_obstacles())
        print("random_even_less_obstacles finished")
        all.append(self.max())
        print("max finished")
        all.append(self.n_1())
        print("n_1 finished")
        all.append(self.m_1())
        print("m_1 finished")
        all.append(self.no_obstacles())
        print("no_obstacles finished")
        all.append(self.all_obstacles())
        print("all_obstacles finished")
        return all

    def solve(self, n: int, m: int, grid: Grid) -> TestCase:
        self.validate(n, m, grid)
        number_of_ways = [[0] * (m + 1) for _ in range(n + 1)]
        number_of_ways[1][1] = 1 if grid[0][0] == "." else 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "#":
                    continue
                number_of_ways[i + 1][j + 1] += number_of_ways[i][j + 1]
                number_of_ways[i + 1][j + 1] += number_of_ways[i + 1][j]
                number_of_ways[i + 1][j + 1] %= MOD
        return ((n, m, grid), number_of_ways[n][m])

    def validate(self, n: int, m: int, grid: Grid) -> None:
        assert 1 <= n <= self.N
        assert 1 <= m <= self.N
        assert len(grid) == n
        assert len(grid[0]) == m

        for i in range(n):
            for j in range(m):
                assert grid[i][j] == "." or grid[i][j] == "#"
