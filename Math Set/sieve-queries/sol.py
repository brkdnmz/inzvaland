N = 5 * 10**6
n_primes = [1] * (N + 1)
n_primes[0] = n_primes[1] = 0
for i in range(2, N + 1):
    n_primes[i] += n_primes[i - 1]
    if n_primes[i] == n_primes[i - 1]:
        continue
    for k in range(i * i, N + 1, i):
        n_primes[k] = 0

q = int(input())
while q:
    q -= 1
    l, r = map(int, input().split())
    print(n_primes[r] - n_primes[l - 1])
