from collections import defaultdict

dp = defaultdict(int)


def solve(n: int) -> int:
    if dp[n]:
        return dp[n]
    if n == 1:
        return 1
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        if i != n:
            dp[n] += solve(i)
        if i * i != n and i != 1:
            dp[n] += solve(n // i)
    return dp[n]


print(solve(int(input())))
