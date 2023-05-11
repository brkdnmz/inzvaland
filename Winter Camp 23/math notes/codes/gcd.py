def iterative_gcd(x, y):
    while x and y:
        if x >= y:
            x %= y
        else:
            y %= x
    return x if x else y


def iterative_gcd_v2(x, y):
    while y:
        x, y = y, x % y
    return x


def recursive_gcd(x, y):
    if not y:
        return x
    return recursive_gcd(y, x % y)
