# https://ideone.com/7CYqnz
n = 10**6


def sieve(n: int) -> "list[bool]":
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = 1
    for i in range(2, n + 1):
        for multiple in range(2 * i, n + 1, i):
            is_prime[multiple] = False
    return is_prime


is_prime = sieve(n)
n_primes = 0
for i in range(2, n + 1):
    n_primes += is_prime[i]

print("Number of primes up to", n, "=", n_primes)
