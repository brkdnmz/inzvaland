N = 5 * 10**6 + 5
spf = [0] * N
for i in range(2, N):
    if spf[i]:
        continue
    spf[i] = i
    for k in range(i * i, N, i):
        if not spf[k]:
            spf[k] = i


q = int(input())
while q:
    q -= 1
    x = int(input())
    n_divisors = 1
    primes = []
    while x > 1:
        p = spf[x]
        exp = 0
        while x % p == 0:
            x //= p
            exp += 1
            primes.append(p)
        n_divisors *= exp + 1
    print(n_divisors)
    print(" ".join(map(str, primes)))
