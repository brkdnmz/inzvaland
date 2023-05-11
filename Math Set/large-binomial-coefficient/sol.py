MOD = 998244353

n, k = map(int, input().split())
k = min(k, n - k)
numer, denom = 1, 1
for i in range(k):
    numer *= n - i
    numer %= MOD
    denom *= i + 1
    denom %= MOD

ans = numer * pow(denom, MOD - 2, MOD) % MOD
print(ans)
