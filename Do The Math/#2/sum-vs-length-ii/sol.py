n = int(input())


def is_p(x):
    div = 1
    while (div + 1) ** 2 <= x:
        div += 1
        if x % div == 0:
            return False
    return True


def divs(x):
    div = 1
    ret = 0
    while (div + 1) ** 2 <= x:
        div += 1
        if x % div:
            continue
        ret += 1 + (div**2 != x)
    return ret


ans = n - 1
for x in range(2, n + 1, 4):
    ans -= is_p(x + 1)

print(ans)
