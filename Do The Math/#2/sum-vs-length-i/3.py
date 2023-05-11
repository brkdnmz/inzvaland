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

SMALL = 100
MED = 500
BIG = 1000

LOWER = MED + 1
UPPER = BIG
NO = 3
SET_NAME = f"big"
N_TC = 5


@numba.njit
def generate():
    n = randint(LOWER, UPPER)

    def is_p(x):
        div = 1
        while (div + 1) ** 2 <= x:
            div += 1
            if x % div == 0:
                return False
        return True

    ans = n - 1
    for x in range(2, n + 1, 4):
        ans -= is_p(x + 1)

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
