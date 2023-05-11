N = 3 * 10**6
# n_divisors = [0] * (N + 1)
prime_div = [0] * (N + 1)
for i in range(2, N + 1):
    if prime_div[i]:
        continue
    prime_div[i] = i
    for k in range(i * i, N + 1, i):
        prime_div[k] = i
    # for multiple in range(i, N + 1, i):
    #     n_divisors[multiple] += 1

MOD = 10**9 + 7

q = int(input())
while q:
    q -= 1
    n = int(input())
    n_divisors = 1
    while n > 1:
        p = prime_div[n]
        exp = 0
        while n % p == 0:
            n //= p
            exp += 1
        n_divisors *= exp + 1
    print(pow(3, n_divisors // 2, MOD) * pow(2, n_divisors % 2, MOD) % MOD)
