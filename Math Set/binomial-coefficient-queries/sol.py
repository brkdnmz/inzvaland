MOD = 10**9 + 7
N = 10**6

f = [0] * (N + 1)
invf = [0] * (N + 1)
f[0] = 1
for i in range(1, N + 1):
    f[i] = f[i - 1] * i % MOD
invf[-1] = pow(f[-1], MOD - 2, MOD)
for i in range(N - 1, -1, -1):
    invf[i] = invf[i + 1] * (i + 1) % MOD


def C(n: int, k: int):  # O(1)
    return f[n] * invf[k] % MOD * invf[n - k] % MOD


def C_alt(n: int, k: int):  # O(log(MOD))
    return f[n] * pow(f[n - k] * f[k] % MOD, MOD - 2, MOD) % MOD


q = int(input())
while q:
    q -= 1
    n, k = map(int, input().split())
    print(C(n, k))
