from collections import defaultdict

A = 5 * 10**6 + 5
MOD = 10**9 + 7

prime_factor = [0] * A
for i in range(2, A):
    if prime_factor[i]:
        continue
    for k in range(i, A, i):
        prime_factor[k] = i

exponents = defaultdict(int)
n = int(input())
a = list(map(int, input().split()))

for x in a:
    while x > 1:
        p = prime_factor[x]
        exp = 0
        while x % p == 0:
            x //= p
            exp += 1
        exponents[p] = max(exponents[p], exp)

ans = 1
for prime, exp in exponents.items():
    for j in range(exp):
        ans *= prime
        ans %= MOD
print(ans)
