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

SMALL = 10**2
MED = 10**3
BIG = 10**5

LOWER = 1
UPPER = SMALL
NO = 1
SET_NAME = f"small"
N_TC = 3

MOD = 10**9 + 7


# @numba.njit
def generate():
    n = randint(LOWER, UPPER)
    is_p = [True for _ in range(n + 1)]
    ans = 1

    def calc_max_exp(i):
        exp = 1
        while i ** (exp + 1) <= n:
            exp += 1
        return exp

    for i in range(2, n + 1):
        if not is_p[i]:
            continue
        ans *= calc_max_exp(i) + 1
        ans %= MOD
        for k in range(i * i, n + 1, i):
            is_p[k] = False
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
