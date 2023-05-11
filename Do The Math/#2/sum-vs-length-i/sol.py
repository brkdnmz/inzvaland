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


ans = 0
for x in range(1, n + 1):
    ans += divs(x) != divs(x * (x + 1) // 2)

print(ans)
