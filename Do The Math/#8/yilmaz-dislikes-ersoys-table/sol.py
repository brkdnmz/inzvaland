from collections import defaultdict

MOD = 10**9 + 7


def solve(n: int) -> int:
    return (pow(2, n, MOD) - 1 - n - n * (n - 1) // 2) % MOD


print(solve(int(input())))
