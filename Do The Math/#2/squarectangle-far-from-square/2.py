import os
from glob import glob
from io import TextIOWrapper
from random import *
from typing import IO, List

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

SMALL = 1000
MED = 10000
BIG = 100000

LOWER = SMALL + 1
UPPER = MED
NO = 2
SET_NAME = f"med"
N_TC = 5


@numba.njit
def generate():
    n = randint(LOWER, UPPER)

    def phi(x):
        res = x
        div = 1
        while (div + 1) ** 2 <= x:
            div += 1
            if x % div:
                continue
            x //= div
            res //= div
            res *= div - 1
            while x % div == 0:
                x //= div
        if x > 1:
            res //= x
            res *= x - 1
        return res

    ans = 0
    for i in range(2, n + 1):
        ans += phi(i)

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
os.system(f"copy gen.py {NO}.py")
