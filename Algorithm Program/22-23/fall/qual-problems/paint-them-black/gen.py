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

LOWER = 1
UPPER = 1
NO = 5
SET_NAME = f"min"
N_TC = 1


@numba.njit
def generate():
    n = randint(LOWER, UPPER)
    m = randint(LOWER, n)

    ans = 1
    for _ in range(m - 1):
        ans = ans * 2 % MOD

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
