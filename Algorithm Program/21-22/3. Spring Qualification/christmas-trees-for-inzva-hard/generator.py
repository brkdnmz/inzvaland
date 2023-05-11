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
N = 500
dp = [[0] * (N+5) for _ in range(N+5)]
dp[1] = [1] * (N+5)

for n_nodes in range(2, N+5):
    for depth in range(1, n_nodes):
        for base_tree_size in range(1, n_nodes):
            subtree_size = n_nodes - base_tree_size
            dp[n_nodes][depth] += dp[base_tree_size][depth] * \
                dp[subtree_size][depth-1]
            dp[n_nodes][depth] -= dp[base_tree_size][depth-1] * \
                (dp[subtree_size][depth-2] if depth > 1 else 0)
            dp[n_nodes][depth] %= mod
    for depth in range(1, N+5):
        dp[n_nodes][depth] += dp[n_nodes][depth-1]
        dp[n_nodes][depth] %= mod

ns = []
ls = []

for tc in range(20):
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    n = 500
    l = randint(1, n-1)
    while ls.count(l):
        l = randint(1, n-1)
    ls.append(l)

    input.write(str(n) + " " + str(l))
    ans = (dp[n][n] - dp[n][l-1]) % mod
    output.write(str(ans))
