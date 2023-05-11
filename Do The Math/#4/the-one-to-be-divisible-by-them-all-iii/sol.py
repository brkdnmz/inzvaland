q = int(input())
N = 5 * 10**6

is_p = [True for _ in range(N + 1)]
n_primes = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    n_primes[i] = n_primes[i - 1]
    if not is_p[i]:
        continue
    n_primes[i] += 1
    for k in range(i * i, N + 1, i):
        is_p[k] = False


for _ in range(q):
    n = int(input())
    print(n_primes[n])
