n = int(input())


def p(x):
    for i in range(2, x + 1):
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True


def calc_max_exp(i):
    exp = 0
    while i ** (exp + 1) <= n:
        exp += 1
    return exp


ans = 1
mod = 10**9 + 7

for i in range(2, n + 1, 1):
    if not p(i):
        continue
    ans *= calc_max_exp(i) + 1
    ans %= mod

print(ans)
