import os
from glob import glob
from math import log, log2
from random import *

import numba
import numpy as np

if not os.path.exists("input"):
    os.makedirs("input")
if not os.path.exists("output"):
    os.makedirs("output")

files = glob("input/*")
for f in files:
    os.remove(f)
files = glob("output/*")
for f in files:
    os.remove(f)

SMALL = 10**3
MED = 10**6
BIG = 10**12

LOWER = BIG
UPPER = BIG
NO = 6
SET_NAME = f"odd, max n. of divisors"
N_TC = 1

p = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


# @numba.njit
def generate():

    def max_divs(bound):
        ans = [1]
        max_divs_(0, 1, bound, 1, [0], ans)
        return ans[0]

    def max_divs_(p_itr, cur, bound, div_cnt, max_cnt, ans):
        if p_itr == len(p):
            if div_cnt > max_cnt[0]:
                max_cnt[0] = div_cnt
                ans[0] = cur
            return
        exp = 0
        while cur <= bound:
            exp += 1
            max_divs_(p_itr + 1, cur, bound, div_cnt * (exp + 1), max_cnt, ans)
            cur *= p[p_itr]

    n = max_divs(BIG)
    div = 0
    ans = 0

    while (div + 1)**2 <= n:
        div += 1
        if n % div:
            continue
        ans += div % 2 == (n // div) % 2 and div != n // div

    return n, ans


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    n, ans = generate()
    input.write(f"{n}")
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"cp gen.py {NO}.py")
