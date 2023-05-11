import glob
import os
from random import *

files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

mod = 10**9 + 7
N = 100
dp = [[0] * (N+1) for _ in range(N+1)]
dp[1][0] = 1

for n_nodes in range(2, N+1):
    for base_tree_size in range(1, n_nodes):
        for d1 in range(n_nodes):
            for d2 in range(n_nodes):
                dp[n_nodes][max(d1, d2+1)] += dp[base_tree_size][d1] * \
                    dp[n_nodes - base_tree_size][d2]
                dp[n_nodes][max(d1, d2+1)] %= mod


ns = []
ls = []

for tc in range(10):
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    n = 100
    l = randint(1, n-1)
    while ls.count(l):
        l = randint(1, n-1)
    ls.append(l)

    input.write(str(n) + " " + str(l))
    ans = 0
    for i in range(l, n+1):
        ans += dp[n][i]
    output.write(str(ans % mod))
