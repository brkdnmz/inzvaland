MOD = 10**9 + 7


def solve(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    if not b:
        return pow(2, max(0, a - 1), MOD)
    dp = [0] * (b + 1)
    for i in range(a + 1):
        ndp = [0] * (b + 1)
        if not i:
            ndp[0] = 1
        for j in range(b + 1):
            if i:
                ndp[j] = (1 + (i + j > 1)) * dp[j]
            if j:
                ndp[j] += (1 + (i + j > 1)) * ndp[j - 1]
            if i and j:
                ndp[j] -= (1 + (i > 1 or j > 1)) * dp[j - 1]
            ndp[j] %= MOD
        dp = ndp
    return dp[b] % MOD


print(solve(*map(int, input().split())))
