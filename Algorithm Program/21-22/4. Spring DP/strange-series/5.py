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

N = 10**18
A = 100
mod = 10**9 + 7


@numba.njit
def solve():
    def mul_ans(m1, cur):
        res = np.zeros_like(cur, np.int64)
        for i in range(100):
            for j in range(100):
                res[i] += m1[i][j] * cur[j] % mod
                res[i] %= mod
        return res

    def mul_self(m1):
        res = np.zeros_like(m1, np.int64)
        for i in range(100):
            for j in range(100):
                for k in range(100):
                    res[i][j] += m1[i][k] * m1[k][j] % mod
                    res[i][j] %= mod
        return res

    n = N
    a = np.random.randint(A, A+1, 100)
    matrix = np.zeros((100, 100), np.int64)
    matrix[0, :] = a
    matrix[1:, :-1] = np.identity(99)
    cur = np.zeros((100,), np.int64)
    cur[0] = 1
    nn = n
    while n:
        if n & 1:
            cur = mul_ans(matrix, cur)
        matrix = mul_self(matrix)
        n >>= 1
    n = nn
    return n, a, cur[0]


for tc in range(1):
    in_file = "input/input{}.txt".format(tc)
    input = open(in_file, "w")
    output = open("output/output{}.txt".format(tc), "w")
    n, a, ans = solve()
    input.write(str(n) + "\n")
    for i, x in enumerate(a):
        input.write(str(x))
        if i+1 != 100:
            input.write(" ")
    output.write(str(ans))
