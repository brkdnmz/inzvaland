n = int(input())


# 963761198400

# def p(n: int) -> bool:
#     i = 1
#     while (i + 1) * (i + 1) <= n:
#         i += 1
#         if n % i == 0:
#             return False
#     return True


# while not p(n):
#     n -= 1


def factorize(n: int) -> "list[int]":
    p = 1
    exponents: "list[int]" = []
    while (p + 1) * (p + 1) <= n:
        p += 1
        if n % p:
            continue
        exp = 0
        while n % p == 0:
            n //= p
            exp += 1
        exponents.append(exp)
    if n > 1:
        exponents.append(1)
    return exponents


def find_n_divisors(factorization: "list[int]"):
    n_divs = 1
    for x in factorization:
        n_divs *= x + 1
    return n_divs


facs = [factorize(n), factorize(n + 1), factorize(n + 2)]
ans = find_n_divisors([2 * x for x in facs[1]])
if n % 2 == 0:
    sum = facs[0][0] + facs[2][0]
    facs[0].remove(facs[0][0])
    facs[2].remove(facs[2][0])
    facs[0].append(sum)
    pass
ans += find_n_divisors(facs[0]) * find_n_divisors(facs[2])
ans -= 1  # 1 is counted 2 times

print(ans)
