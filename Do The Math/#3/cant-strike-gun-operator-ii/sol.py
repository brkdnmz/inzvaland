m, r = map(int, input().split())
MOD = 10**9 + 7
ans = 0
for last_reload_size in range(1, r + 1):
    ans += (m - last_reload_size + 1) * pow(2, max(
        0, r - last_reload_size - 1), MOD)
    ans %= MOD
print(ans)
