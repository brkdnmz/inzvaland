import glob
import os
from random import *

files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

N = 5000
dp = [1] * N
ans = [0] * N
ans[0] = 1
for line in range(1, N):
    ndp = [0] * N
    for indentation in range(N):
        ndp[indentation] = dp[N-1] - \
            (dp[indentation-2] if indentation >= 2 else 0)
        ndp[indentation] %= 10**9 + 7
    dp = ndp
    for indentation in range(1, N):
        dp[indentation] += dp[indentation-1]
        dp[indentation] %= 10**9 + 7
    ans[line] = dp[N-1]

ns = []
for tc in range(20):
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    n = randint(101, 4999)
    while ns.count(n) != 0:
        n = randint(101, 4999)
    ns.append(n)

    input.write(str(n) + " 1")
    output.write(str(ans[n-1]))
