from random import randint
import numba
import os
import glob

# dp[1]*cnt[i-1] + cnt[1]*m*dp[i-1] -> dp[1]*cnt[i-1] must be excluded
# dp[2]*cnt[i-2] + cnt[2]*m*dp[i-2]
# dp[3]*cnt[i-3] + cnt[3]*m*dp[i-3]
# ...
# dp[i-1]*cnt[1] + cnt[i-1]*m*dp[1]

# shortcut:

# dp[1]*cnt[i-1](m + 1)
# dp[2]*cnt[i-2](m + 1)
# dp[3]*cnt[i-3](m + 1)
# ...
# dp[i-1]*cnt[1](m + 1)

mod = 10**9 + 7


@numba.njit
def calc(n, m):
    def mul(a, b):
        return a*b % mod

    dp = [0] * (n+2)
    cnt = [0] * (n+2)
    dp[1] = cnt[1] = 1
    for i in range(2, n+2):
        for j in range(1, i):
            cnt[i] += mul(cnt[j], cnt[i-j])
            cnt[i] %= mod
        for j in range(1, i):
            dp[i] += mul(mul(dp[j], cnt[i-j]), m+1)
            dp[i] %= mod
        dp[i] -= dp[1]*cnt[i-1]
        dp[i] %= mod
    return dp[n+1]


files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

for tc in range(20):
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")
    n = randint(101, 5000)
    m = randint(1, 10**9)
    input.write(str(n) + " " + str(m))
    output.write(str(calc(n, m)))
