n = 2**3 * 3**2 * 7**3 * 43**2 * 59
exps = {}  # May use dictionary (hashmap)!
for d in range(2, n + 1):
    if d * d > n:
        break
    if n % d:
        continue
    exp = 0
    while n % d == 0:
        n //= d
        exp += 1

    exps[d] = exp

if n > 1:
    exps[n] = 1

n_divisors = 1
for prime, exp in exps.items():
    n_divisors *= exp + 1

print(n_divisors)
