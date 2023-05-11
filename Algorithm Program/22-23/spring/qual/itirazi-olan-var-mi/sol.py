from bisect import bisect_left


def solve(n: int, a: "list[int]"):
    prefix_max = [0] * n
    suffix_max = [0] * n
    for i in range(n):
        prefix_max[i] = max(prefix_max[i - 1] if i else 0, a[i])
    for i in range(n - 1, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1] if i + 1 < n else 0, a[i])
    suffix_max.reverse()
    ans = []
    for i in range(n):
        l_i = bisect_left(prefix_max, a[i], 0, i + 1)
        r_i = bisect_left(suffix_max, a[i], 0, n - i)
        r_i = n - 1 - r_i
        print(l_i, r_i)


n = int(input())
a = list(map(int, input().split()))

solve(n, a)
