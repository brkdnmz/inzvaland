N = 215
MOD = 10**9 + 7
dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1

factor = lambda a, b, c: 1 + (a + b + c > 0)


def rec(a: int, b: int, c: int) -> int:
    if ~dp[a][b][c]:
        return dp[a][b][c]
    ans = 0
    if a:
        ans += factor(a - 1, b, c) * rec(a - 1, b, c)
    if b:
        ans += factor(a, b - 1, c) * rec(a, b - 1, c)
    if c:
        ans += factor(a, b, c - 1) * rec(a, b, c - 1)
    if a and b:
        ans -= factor(a - 1, b - 1, c) * rec(a - 1, b - 1, c)
    if a and c:
        ans -= factor(a - 1, b, c - 1) * rec(a - 1, b, c - 1)
    if b and c:
        ans -= factor(a, b - 1, c - 1) * rec(a, b - 1, c - 1)
    if a and b and c:
        ans += factor(a - 1, b - 1, c - 1) * rec(a - 1, b - 1, c - 1)
    dp[a][b][c] = ans % MOD
    return dp[a][b][c]


def rec2(a: int, b: int, c: int) -> int:
    if a + b + c == 0:
        return 1
    if ~dp[a][b][c]:
        return dp[a][b][c]
    ans = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if i + j + k == a + b + c:
                    continue
                ans += rec2(i, j, k)
                ans %= MOD
    dp[a][b][c] = ans
    return ans


# q = int(input())
for a in range(10):
    for b in range(10):
        for c in range(10):
            dp = [[[-1] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]
            dp[0][0][0] = 1
            ans1 = rec(a, b, c)
            dp = [[[-1] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]
            dp[0][0][0] = 1
            ans2 = rec2(a, b, c)
            if ans1 != ans2:
                print(ans1, ans2, a, b, c)
