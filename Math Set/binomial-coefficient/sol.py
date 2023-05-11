MOD = 10**9 + 7

n, k = map(int, input().split())
numer, denom = 1, 1
for i in range(1, n + 1):
    numer *= i
    numer %= MOD
for i in range(1, k + 1):
    denom *= i
    denom %= MOD
for i in range(1, n - k + 1):
    denom *= i
    denom %= MOD
ans = numer * pow(denom, MOD - 2, MOD) % MOD
print(ans)
