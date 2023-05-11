import glob
import os
from random import randint
import numba

import numpy as np


@numba.njit
def solve(n, a):
    dp = np.ones((n, n+1), dtype=np.int64)
    for i in range(n):
        cur_sum = a[i]
        for j in range(i-1, -1, -1):
            for n_parts in range(2, i+2):
                dp[i][n_parts] = max(
                    dp[i][n_parts], np.gcd(cur_sum, dp[j][n_parts-1]))
            cur_sum += a[j]
        dp[i][1] = cur_sum
    for k in range(n, 0, -1):
        if dp[n-1][k] > 1:
            return k


n = int(input())
a = np.array(list(map(int, input().split())))
print(solve(n, a))
