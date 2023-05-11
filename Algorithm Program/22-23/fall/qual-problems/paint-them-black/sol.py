n, m = map(int, input().split())

MOD = 10**3 + 7
m -= 1
ans = 1
while m:
    m -= 1
    ans *= 2
    ans %= MOD

print(ans)
