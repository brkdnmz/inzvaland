n, m = map(int, input().split())

MOD = 10**3 + 7
N_CHARS = 23
ans = 0
if n % m == 0:
    ans = 1
    for _ in range(m):
        ans = ans * N_CHARS % MOD

print(ans)
