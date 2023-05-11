N = 3 * 10**6
MOD = 10**9 + 7
is_prime = [1 for _ in range(N + 1)]
ans = [1 for _ in range(N + 1)]

for i in range(2, N + 1):
    ans[i] = ans[i - 1]
    if not is_prime[i]:
        continue
    ans[i] *= i
    ans[i] %= MOD
    for k in range(i * i, N + 1, i):
        is_prime[k] = 0

n = int(input())
print(" ".join([f"{ans[d]}" for d in list(map(int, input().split()))]))
