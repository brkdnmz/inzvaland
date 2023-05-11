import glob
import os
from random import randint
import numba

import numpy as np
from sklearn.utils import shuffle

files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

N = 17


@numba.njit
def solve():
    n = 8
    n_edges = 12
    edges = np.zeros((n_edges, 2), np.int64)
    ptr = 0
    while ptr < n_edges:
        u = randint(1, n-1)
        v = randint(u+1, n)
        while 1:
            ok = True
            for i in range(ptr):
                if u == edges[i][0] and v == edges[i][1]:
                    ok = False
                    break
            if ok:
                break
            u = randint(1, n-1)
            v = randint(u+1, n)
        edges[ptr] = [u, v]
        ptr += 1
    connected = np.zeros((n, n), np.int64)
    for edge in edges:
        connected[edge[0]-1, edge[1] -
                  1] = connected[edge[1]-1, edge[0]-1] = True

    M = 1 << n
    dp = np.zeros((M, n), np.int64)
    for i in range(n):
        dp[1 << i][i] = 1
    ans = -n
    for m in range(M):
        for end in range(n):
            if not (m & 1 << end):
                continue
            for new_end in range(n):
                if m & 1 << new_end:
                    continue
                if not connected[end, new_end]:
                    continue
                dp[m | 1 << new_end][new_end] += dp[m][end]
            ans += dp[m][end]
    assert ans % 2 == 0
    ans //= 2
    return n, n_edges, edges, ans


for tc in range(1):
    in_file = "input/input{}.txt".format(tc)
    input = open(in_file, "w")
    output = open("output/output{}.txt".format(tc), "w")
    n, m, edges, ans = solve()
    input.write(str(n) + " " + str(m) + "\n")
    for i, edge in enumerate(edges):
        shuffle = randint(0, 1)
        if shuffle:
            edge = edge[[1, 0]]
        input.write(str(edge[0]) + " " + str(edge[1]))
        if i+1 != m:
            input.write("\n")
    output.write(str(ans))
