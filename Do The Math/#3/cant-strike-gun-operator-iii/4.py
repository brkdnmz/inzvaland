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
BIG = 10**6

LOWER = MED + 1
UPPER = BIG
NO = 4
SET_NAME = f"min"
N_TC = 1

MOD = 10**9 + 7


# @numba.njit
def generate():
    m = 1
    r = 1
    ans = pow(2, r - 1, MOD)  # all scenarios
    # cases to exclude
    for i in range(r - m):
        # put m+1+i in one
        # distribute the rest r - (m+1+i)
        biggest = m + 1 + i
        exc = 1  # m+1+i == r
        if r - biggest > 0:
            exc = pow(2, r - biggest, MOD)  #only on one side
        if r - biggest > 1:
            exc += (r - biggest - 1) * pow(2, r - biggest - 2, MOD) % MOD
        exc %= MOD
        ans -= exc
        ans %= MOD
    return m, r, ans


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    m, r, ans = generate()
    input.write(f"{m} {r}")
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"cp gen.py {NO}.py")
