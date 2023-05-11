import os
from glob import glob
from io import TextIOWrapper
from random import *
from re import M
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

MOD = 10**3 + 7
N_CHARS = 23

SMALL = 1000
MED = 10000
BIG = 100000

LOWER = MED + 1
UPPER = BIG
NO = 3
SET_NAME = f"big"
N_TC = 5


@numba.njit
def generate():
    n = randint(LOWER, UPPER)
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)

    ans_nonzero = randint(0, 3)
    m = divs[randint(0, len(divs) - 1)]
    if not ans_nonzero:
        while m in divs:
            m = randint(1, n)
    assert m <= n <= UPPER and LOWER <= n
    if ans_nonzero:
        assert n % m == 0

    ans = 0
    if n % m == 0:
        ans = 1
        for _ in range(m):
            ans = ans * N_CHARS % MOD

    return n, m, ans


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    n, m, ans = generate()
    input.write(f"{n} {m}")
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
