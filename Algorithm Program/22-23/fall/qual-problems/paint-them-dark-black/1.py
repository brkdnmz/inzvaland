import os
from glob import glob
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

MOD = 10**3 + 7

SMALL = 1000
MED = 10000
BIG = 100000

LOWER = 0 + 1
UPPER = SMALL
NO = 1
SET_NAME = f"small"
N_TC = 5


# @numba.njit
def generate():
    n = randint(LOWER, UPPER)
    m = randint(LOWER, n)

    def find_period(s: str):
        n = len(s)
        d = 0
        period = n
        while (d + 1) ** 2 <= n:
            d += 1
            if n % d:
                continue
            check = True
            for i in range(d, n - d + 1, d):
                check &= s[i : i + d] == s[:d]
            if check:
                period = min(period, d)
            check = True
            for i in range(n // d, n - n // d + 1, n // d):
                check &= s[i : i + n // d] == s[: n // d]
            if check:
                period = min(period, n // d)

        return period

    divs = []
    for i in range(1, m + 1):
        if m % i == 0:
            divs.append(i)

    period = divs[randint(0, len(divs) - 1)]
    seq = ["W"] * period
    cnt_b = randint(0, period // 2) * 2
    for i in range(cnt_b):
        seq[i] = "B"
    shuffle(seq)
    while find_period(seq) < period:
        seq = ["W"] * period
        cnt_b = randint(0, period // 2) * 2
        for i in range(cnt_b):
            seq[i] = "B"
        shuffle(seq)

    seq = seq * (m // period)
    seq = "".join(seq)
    ans = min(n - m + 1, period)

    return n, m, seq, ans


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    n, m, seq, ans = generate()
    input.write(f"{n} {m}\n{seq}")
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
