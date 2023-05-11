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




for a in range(N + 1):
    for b in range(N + 1):
        for c in range(N + 1):
            ans = 0
            if a:
                ans += factor(a - 1, b, c) * dp[a - 1][b][c]
            if b:
                ans += factor(a, b - 1, c) * dp[a][b - 1][c]
            if c:
                ans += factor(a, b, c - 1) * dp[a][b][c - 1]
            if a and b:
                ans -= factor(a - 1, b - 1, c) * dp[a - 1][b - 1][c]
            if a and c:
                ans -= factor(a - 1, b, c - 1) * dp[a - 1][b][c - 1]
            if b and c:
                ans -= factor(a, b - 1, c - 1) * dp[a][b - 1][c - 1]
            if a and b and c:
                ans += factor(a - 1, b - 1, c - 1) * dp[a - 1][b - 1][c - 1]

            dp[a][b][c] = ans % MOD


q = int(input())
while q:
    q -= 1
    a, b, c = map(int, input().split())
    print(dp[a][b][c])
