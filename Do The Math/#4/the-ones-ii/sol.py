n, m = map(int, input().split())
MOD = 10**9 + 7
ans = 1


def pow(base, exp):
    res = 1
    while exp:
        exp -= 1
        res *= base
        res %= MOD
    return res


for i in range(2, n):
    if i**2 > n:
        break
    if n % i:
        continue
    exp = 0
    while n % i == 0:
        n //= i
        exp += 1
    ans *= (pow(exp + 1, m) - pow(exp, m) + MOD) % MOD
    ans %= MOD
if n > 1:
    ans *= (pow(2, m) - 1 + MOD) % MOD
    ans %= MOD


print(ans)
