N = 10**5 + 5
is_prime = [True] * N
primes = []
for i in range(2, N):
    if not is_prime[i]:
        continue
    primes.append(i)
    for k in range(i * i,N, i):
        is_prime[k] = False


q = int(input())
while q:
    q -= 1
    x = int(input())
    n_divisors = 1
    for prime in primes:
        if prime**2 > x:
            break
        exp = 0
        while x % prime == 0:
            x //= prime
            exp += 1
        n_divisors *= exp + 1
    if x > 1:
        n_divisors *= 2
    print(n_divisors)
