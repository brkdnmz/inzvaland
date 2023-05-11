from collections import defaultdict

N = 10**6
MOD = 10**9 + 7
prime_divisor = [0 for _ in range(N + 1)]
primes = []
for p in range(2, N + 1):
    if prime_divisor[p]:
        continue
    primes.append(p)
    prime_divisor[p] = p
    for k in range(p * p, N + 1, p):
        prime_divisor[k] = p


def solve(a: "list[int]"):
    answers = []
    exponents: "dict[int, int]" = defaultdict(int)
    for x in a:
        if x <= 10**6:
            while x > 1:
                divisor = prime_divisor[x]
                exponent = 0
                while x % divisor == 0:
                    exponent += 1
                    x //= divisor
                exponents[divisor] += exponent
        else:
            for p in primes:
                if p * p > x:
                    break
                if x % p:
                    continue
                exponent = 0
                while x % p == 0:
                    exponent += 1
                    x //= p
                exponents[p] += exponent
            if x > 1:
                exponents[x] += 1
        answers.append(pow(2, len(exponents), MOD))
    n_divisors = 2
    for p, e in exponents.items():
        n_divisors *= e + 1
        n_divisors %= MOD
    answers.append(n_divisors)
    return answers


n = int(input())
a = list(map(int, input().split()))

print("\n".join([str(x) for x in solve(a)]))
