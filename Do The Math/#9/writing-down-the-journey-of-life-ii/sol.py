from math import gcd


def solve(n: int, lines: "list[int]"):
    overall_gcd = n + 1
    for line in lines:
        overall_gcd = gcd(overall_gcd, line)
    ans = -1  # exclude divisor = overall_gcd
    for i in range(1, overall_gcd + 1):
        if i * i > overall_gcd:
            break
        if overall_gcd % i:
            continue
        ans += 1 + (i * i != overall_gcd)
    return ans


read = lambda: list(map(int, input().split()))

n, m = read()
lines = read()
print(solve(n, lines))
