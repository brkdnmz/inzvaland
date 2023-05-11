def required_rotation_angle(a1: int, a2: int) -> int:
    diff = abs(a2 - a1)
    return min(diff, 360 - diff)


def solve(r: "list[int]", a: "list[int]") -> int:
    n = len(r)
    ans = 0
    prefix_sum = 0
    all_sum = sum([x**2 for x in r])
    for i in range(1, n - 1):
        prefix_sum += r[i - 1] ** 2
        rotation_angle = required_rotation_angle(a[i - 1], a[i])
        optimal_cost = min(prefix_sum, all_sum - prefix_sum - r[i] ** 2)
        assert optimal_cost > 0
        ans += rotation_angle * optimal_cost
    return ans


n = int(input())
r = list(map(int, input().split()))
a = list(map(int, input().split()))

print(solve(r, a))
