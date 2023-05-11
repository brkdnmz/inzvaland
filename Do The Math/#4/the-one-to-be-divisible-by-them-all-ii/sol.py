n = int(input())
MOD = 10**9 + 7
is_p = [True for _ in range(n + 1)]
ans = 1


def calc_max_exp(i):
    exp = 1
    while i ** (exp + 1) <= n:
        exp += 1
    return exp


for i in range(2, n + 1):
    if not is_p[i]:
        continue
    ans *= calc_max_exp(i) + 1
    ans %= MOD
    for k in range(i * i, n + 1, i):
        is_p[k] = False

print(ans)
