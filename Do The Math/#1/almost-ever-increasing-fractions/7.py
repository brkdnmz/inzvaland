from ctypes.wintypes import tagMSG
import os
from glob import glob
from random import *
from time import sleep
from typing import List, TextIO, Tuple, Union

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

SMALL = 10
MED = 10**6
BIG = 10**12

NO = 7
TC_NAME = "both 1e12"
N_TC = 1


@numba.njit
def solve(t=1):
    """
        a/b, (a+1)/(b-1), (a+2)/(b-2)...\\
        How many integers?\\
        These are,\\
        (a+b)/b - 1, (a+b)/(b-1) - 1, (+b)/(b-2) - 1...\\
        Number of divisors of a+b that are <= b (pos & neg)
    """
    a_s, b_s, ans_s = [], [], []

    for _ in range(t):
        a = BIG
        b = BIG
        cnt = 0
        divisor = 0
        while (divisor+1) ** 2 <= a+b:
            divisor += 1
            if (a+b) % divisor:
                continue
            # 1 for neg divisor, (divisor <= b) for pos divisor
            cnt += 1 + (divisor <= b)

            if divisor**2 != a+b:
                cnt += 1 + ((a+b)//divisor <= b)

        a_s.append(a)
        b_s.append(b)
        ans_s.append(cnt)

    return a_s, b_s, ans_s


def write_2d(l: Union[List[List], List[Tuple]], out: TextIO, sep="\n", last=False):
    assert len(l)

    write_1d(l[0], out)
    for i, x in enumerate(l[1:]):
        write_1d(x, out, sep=" ", last=i+1 == len(l[1:]))


def write_1d(l: List[int], out: TextIO, sep=" ", last=False):
    assert len(l)

    out.write(f"{l[0]}")
    for x in l[1:]:
        out.write(sep + f"{x}")
    if not last:
        out.write("\n")


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")

    t = 10

    a_s, b_s, ans_s = solve(t)

    write_1d([t], input)
    write_2d(list(zip(a_s, b_s)), input)

    write_1d(ans_s, output, "\n", last=True)

    input.close()
    output.close()

os.system(f"zip -r \"{NO}. {TC_NAME} {N_TC}.zip\" input output")
os.system(f"copy gen.py {NO}.py")
