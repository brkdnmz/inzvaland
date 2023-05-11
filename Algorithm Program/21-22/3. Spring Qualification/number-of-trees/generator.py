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
N = 5000
dp = [0] * (N+5)
dp[1] = 1
for n_nodes in range(2, N+1):
    for base_tree_size in range(1, n_nodes):
        dp[n_nodes] += dp[base_tree_size] * dp[n_nodes - base_tree_size]
        dp[n_nodes] %= mod

ns = []

for tc in range(20):
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    n = randint(101, 4999)
    while ns.count(n) != 0:
        n = randint(101, 4999)
    ns.append(n)

    input.write(str(n))
    output.write(str(dp[n]))
