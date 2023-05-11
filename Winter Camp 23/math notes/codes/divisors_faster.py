n = 1234567**2
n_divisors = 0

for d in range(1, n + 1):
    if d * d > n:
        break
    if n % d:
        continue
    n_divisors += 1
    k = n // d
    n_divisors += d != k

print(n_divisors)
