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

N = 500
V = 10**5


def solve():
    def create_p(n, min_depth):
        nodes = np.array(list(range(2, n+1)))
        np.random.shuffle(nodes)
        p = np.zeros((n+1,), dtype=np.int0)
        for i, node in enumerate(nodes):
            prev_nodes = np.concatenate((np.ones((1,)), nodes[:i]))
            if not min_depth:
                p[node] = prev_nodes[randint(0, i)]
            else:
                p[node] = prev_nodes[-1]
                min_depth -= 1
        return p

    @numba.njit
    def dfs(cur, g, dp, max_of_level, level):
        dp[cur][1][1] = val[cur]
        dp[cur][0][0] = 0
        for nxt in g[cur]:
            if not nxt:
                break
            level[nxt] = level[cur]+1
            dfs(nxt, g, dp, max_of_level, level)
            ndp = dp[cur].copy()
            for nxt_cnt in range(n):
                for tot_cnt in range(n, -1, -1):
                    ndp[tot_cnt][0] = max(
                        ndp[tot_cnt][0], dp[cur][tot_cnt - nxt_cnt][0] + dp[nxt][nxt_cnt][0])
                    ndp[tot_cnt][0] = max(
                        ndp[tot_cnt][0], dp[cur][tot_cnt - nxt_cnt][0] + dp[nxt][nxt_cnt][1])
                    ndp[tot_cnt][1] = max(
                        ndp[tot_cnt][1], dp[cur][tot_cnt - nxt_cnt][1] + dp[nxt][nxt_cnt][0])
            dp[cur] = ndp
        for cnt in range(n+1):
            max_of_level[level[cur]] = max(
                max_of_level[level[cur]], dp[cur][cnt][0]*cnt, dp[cur][cnt][1]*cnt)
    n = randint(1, N)
    p = create_p(n, randint(0, n-1))[2:]
    g = [[] for _ in range(n+1)]
    for i in range(n-1):
        g[p[i]].append(i+2)
    for i in range(n+1):
        g[i] = np.array(g[i], np.int64)
        g[i] = np.concatenate(
            (g[i], np.zeros((n - len(g[i]),), np.int64)))
    g = np.array(g)
    dp = np.zeros((n+1, n+1, 2), np.int64)
    dp.fill(-10**10)
    val = np.random.randint(-V//1000, V+1, (n+1,))
    level = np.zeros((n+1,), np.int64)
    level[1] = 1
    max_of_level = np.zeros((n+1,), np.int64)
    dfs(1, g, dp, max_of_level, level)
    return n, val[1:], p, max_of_level[1:]


for tc in range(5):
    in_file = "input/input{}.txt".format(tc)
    input = open(in_file, "w")
    output = open("output/output{}.txt".format(tc), "w")
    n, val, p, ans = solve()
    input.write(str(n) + "\n")
    for i, cur in enumerate(val):
        input.write(str(cur))
        if i+1 != n:
            input.write(" ")
        else:
            input.write("\n")
    for i, cur in enumerate(p):
        input.write(str(cur))
        if i+1 != n-1:
            input.write(" ")

    for i, cur in enumerate(ans):
        output.write(str(cur))
        if i+1 != n:
            output.write(" ")
    print("tc", tc+1)
