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
NO = 3
SET_NAME = f"big"
N_TC = 5

MOD = 10**9 + 7


# @numba.njit
def generate():
    r, m = sorted(sample([i for i in range(LOWER, UPPER + 1)], 2))
    ans = 0
    for last_reload_size in range(1, r + 1):
        ans += (m - last_reload_size + 1) * pow(
            2, max(0, r - last_reload_size - 1), MOD)
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
