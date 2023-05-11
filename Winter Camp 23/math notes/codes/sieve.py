n = 10**7
is_prime = [1] * (n + 1)
n_primes = 0

for i in range(2, n + 1):
    if not is_prime[i]:
        continue
    n_primes += 1
    for k in range(2 * i, n + 1, i):
        is_prime[k] = 0

print(n_primes)
