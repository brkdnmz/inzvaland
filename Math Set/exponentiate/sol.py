MOD = 10**9 + 7


def sol1(a: int, b: int):
    a %= MOD
    b %= MOD - 1  # optional
    ans = 1
    while b:
        if b & 1:
            ans *= a
            ans %= MOD
        b >>= 1
        a *= a
        a %= MOD
    return ans


def sol2(a: int, b: int):
    return pow(a, b, 10**9 + 7)


a, b = map(int, input().split())

print(sol1(a, b))
