n = 13012023
n_divisors = 0

for d in range(1, n + 1):
    if n % d == 0:
        n_divisors += 1

print(n_divisors)
