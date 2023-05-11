import glob
import os
from random import randint
import numba

import numpy as np

files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

N = 500
T = 10**5


@numba.njit
def solve():
    n = 100
    food = np.random.randint(1, 3, (n+1, n+1, n+1))
    dp = np.full((n+1, n+1, n+1), -10**18, np.int64)
    next_move = np.full((n+1, n+1, n+1), 3)
    dp[n, n, n] = food[n, n, n]
    choices = np.array([
        [0, 0, -1],
        [-1, 0, 0],
        [0, -1, 0],
    ])
    moves = ["F", "R", "U"]
    for c in range(n, 0, -1):
        for r in range(n, 0, -1):
            for d in range(n, 0, -1):
                for i, ch in enumerate(choices):
                    nc = c + ch[0]
                    nr = r + ch[1]
                    nd = d + ch[2]
                    new_val = dp[c, r, d] + food[nc, nr, nd]
                    if dp[nc, nr, nd] <= new_val:
                        if dp[nc, nr, nd] == new_val and next_move[nc, nr, nd] > i:
                            next_move[nc, nr, nd] = i
                        elif dp[nc, nr, nd] < new_val:
                            dp[nc, nr, nd] = new_val
                            next_move[nc, nr, nd] = i

    path = ""
    cur = np.array([1, 1, 1])
    while next_move[cur[0], cur[1], cur[2]] <= 2:
        path += moves[next_move[cur[0], cur[1], cur[2]]]
        cur -= choices[next_move[cur[0], cur[1], cur[2]]]

    return n, food, dp[1, 1, 1], path


for tc in range(3):
    in_file = "input/input{}.txt".format(tc)
    input = open(in_file, "w")
    output = open("output/output{}.txt".format(tc), "w")

    n, food, ans, path = solve()
    input.write(str(n) + "\n")
    # c, r, d -> d, r, c
    food = food.transpose((2, 1, 0))
    food = food[1:, 1:, 1:].reshape((n**2, n))
    np.savetxt("save_array.txt", food, fmt="%i")
    input.writelines(open("save_array.txt").readlines())
    output.write(str(ans) + "\n")
    output.write(path)
    print(tc+1, "completed")
