import sys
from random import choice, choices, randint, sample, shuffle
from typing import List, Tuple

TestData = Tuple[List[int], List[int], int]


class Generator:
    def __init__(self, N: int, R: int, A: int) -> None:
        self.N = N
        self.R = R
        self.A = A

    def required_rotation_angle(self, a1: int, a2: int) -> int:
        a1 %= 360
        a2 %= 360
        diff = abs(a2 - a1)
        return min(diff, 360 - diff)

    def random(self) -> TestData:
        r = [randint(1, self.R) for _ in range(self.N)]
        a = [randint(0, self.A) for _ in range(self.N - 1)]
        return self.solve_and_return_test(r, a)

    def always_180_degrees_max_ans(self) -> TestData:
        r = [self.R for _ in range(self.N)]
        normalized_angle = randint(0, 179)
        a = []
        for i in range(self.N - 1):
            current_angle = normalized_angle + i % 2 * 180
            current_angle += 360 * randint(0, (self.A - current_angle) // 360)
            a.append(current_angle)
        return self.solve_and_return_test(r, a)

    def first_sphere_max_others_min(self) -> TestData:
        r = [1 for _ in range(self.N)]
        r[0] = self.R
        a = [randint(0, self.A) for _ in range(self.N - 1)]
        return self.solve_and_return_test(r, a)

    def last_sphere_max_others_min(self) -> TestData:
        r = [1 for _ in range(self.N)]
        r[-1] = self.R
        a = [randint(0, self.A) for _ in range(self.N - 1)]
        return self.solve_and_return_test(r, a)

    def already_unfolded(self) -> TestData:
        r = [randint(1, self.R) for _ in range(self.N)]
        angle = randint(0, 359)
        max_coef = (self.A - angle) // 360
        a = [angle + 360 * randint(0, max_coef) for _ in range(self.N - 1)]
        return self.solve_and_return_test(r, a)

    def only_one_rotation_required(self) -> TestData:
        r = [randint(1, self.R) for _ in range(self.N)]
        angles = sample(list(range(360)), 2)
        second_angle_start = randint(1, self.N - 2)
        a = [0 for i in range(self.N - 1)]
        for i in range(self.N - 1):
            cur_angle = angles[i >= second_angle_start]
            a[i] = cur_angle + 360 * randint(0, (self.A - cur_angle) // 360)
        return self.solve_and_return_test(r, a)

    def generate_all(self) -> "list[tuple[list[int], list[int], int]]":
        tests = []
        tests.append(self.random())
        tests.append(self.always_180_degrees_max_ans())
        tests.append(self.first_sphere_max_others_min())
        tests.append(self.last_sphere_max_others_min())
        tests.append(self.already_unfolded())
        tests.append(self.only_one_rotation_required())
        return tests

    def solve(self, r: List[int], a: List[int]) -> int:
        ans = 0
        prefix_sum = 0
        all_sum = sum([x**2 for x in r])
        for i in range(1, self.N - 1):
            prefix_sum += r[i - 1] ** 2
            rotation_angle = self.required_rotation_angle(a[i - 1], a[i])
            optimal_cost = min(prefix_sum, all_sum - prefix_sum - r[i] ** 2)
            assert optimal_cost > 0
            ans += rotation_angle * optimal_cost
        return ans

    def solve_and_return_test(self, r: List[int], a: List[int]) -> TestData:
        ans = self.solve(r, a)
        self.validate(r, a)
        return r, a, ans

    def validate(self, r: "list[int]", a: "list[int]") -> None:
        ANS_LIMIT = sys.maxsize
        assert len(r) == self.N and len(a) == len(r) - 1
        for i in range(self.N):
            assert 0 <= r[i] <= self.R
        for i in range(self.N - 1):
            assert 0 <= a[i] <= self.A
        real_ans = 0
        prefix_sum = 0
        all_sum = sum(r)
        for i in range(1, self.N - 1):
            prefix_sum += r[i - 1]
            rotation_angle = self.required_rotation_angle(a[i - 1], a[i])
            optimal_cost = min(prefix_sum, all_sum - prefix_sum - r[i])
            assert optimal_cost > 0
            real_ans += rotation_angle * optimal_cost
        assert self.solve(r, a) <= ANS_LIMIT
