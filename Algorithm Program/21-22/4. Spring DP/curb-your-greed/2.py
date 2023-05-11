import glob
import os
from random import randint
from cv2 import bitwise_and
import numba

import numpy as np

files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

N = 17
T = 10**5


@numba.njit
def solve():
    n = 17
    M = 1 << n
    g = np.random.randint(1, 10**9, (n, n))
    dp = [-10**18]*M
    dp[0] = 0
    for i in range(n):
        for m in range(M-1, -1, -1):
            for j in range(n):
                if m & 1 << j:
                    continue
                dp[m | 1 << j] = max(dp[m | 1 << j], dp[m] + g[i][j])
    return n, g, dp[M-1]


for tc in range(10):
    in_file = "input/input{}.txt".format(tc)
    input = open(in_file, "w")
    output = open("output/output{}.txt".format(tc), "w")

    n, g, ans = solve()
    input.write(str(n) + "\n")
    np.savetxt("save_array.txt", g, fmt="%i")
    input.writelines(open("save_array.txt").readlines())
    output.write(str(ans))
    print(tc+1, "completed")
