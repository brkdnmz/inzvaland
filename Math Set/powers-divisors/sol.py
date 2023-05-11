MOD = 10**9 + 7


def solve(n: int):
    ans = 1
    pwr = n
    for i in range(2, n + 1):
        if i * i > n:
            break
        exp = 0
        while n % i == 0:
            n //= i
            exp += 1
        ans *= pwr * exp + 1
        ans %= MOD
    if n > 1:
        ans *= pwr + 1
    return ans % MOD


print(solve(int(input())))
