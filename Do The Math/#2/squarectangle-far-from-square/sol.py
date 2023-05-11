from math import gcd

n = int(input())


def phi(x):
    res = x
    div = 1
    while (div + 1) ** 2 <= x:
        div += 1
        if x % div:
            continue
        x //= div
        res //= div
        res *= div - 1
        while x % div == 0:
            x //= div
    if x > 1:
        res //= x
        res *= x - 1
    return res


ans = 0
for y in range(2, n + 1):
    ans += phi(y)
print(ans)
