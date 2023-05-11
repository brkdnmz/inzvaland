m, r = map(int, input().split())
MOD = 10**9 + 7

# pw2 = [1 in range(r)]
# for i in range(1, r):
#     pw2[i] = pw2[i - 1] * 2 % MOD

ans = pow(2, r - 1, MOD)  # all scenarios
# cases to exclude
for i in range(r - m):
    # put m+1+i in one
    # distribute the rest r - (m+1+i)
    biggest = m + 1 + i
    exc = 1  # m+1+i == r
    if r - biggest > 0:
        exc = pow(2, r - biggest, MOD)  #only on one side
    if r - biggest > 1:
        exc += (r - biggest - 1) * pow(2, r - biggest - 2, MOD) % MOD
    exc %= MOD
    ans -= exc
    ans %= MOD
print(ans)
