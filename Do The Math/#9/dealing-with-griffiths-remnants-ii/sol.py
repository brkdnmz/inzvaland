from math import gcd


def solve(n: str):
    exp = 2
    seen_dot = False
    n_int = 0
    for c in n:
        if c == ".":
            seen_dot = True
            continue
        exp += seen_dot
        digit = ord(c) - ord("0")
        n_int = 10 * n_int + digit
    return n_int // gcd(n_int, 10**exp)


print(solve(input()))
