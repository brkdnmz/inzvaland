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

LOWER = BIG // 3
UPPER = BIG
NO = 6
SET_NAME = f"same"
N_TC = 5

MOD = 10**9 + 7


# @numba.njit
def generate():
    r = randint(LOWER, UPPER)
    m = r
    ans = pow(2, r - 1, MOD)
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
