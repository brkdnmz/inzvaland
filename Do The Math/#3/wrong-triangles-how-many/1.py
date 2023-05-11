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

SMALL = 10**3
MED = 10**6
BIG = 10**12

LOWER = 1
UPPER = SMALL
NO = 1
SET_NAME = f"small"
N_TC = 5


@numba.njit
def generate():
    n = randint(LOWER, UPPER)
    div = 0
    ans = 0

    while (div + 1)**2 <= n:
        div += 1
        if n % div:
            continue
        ans += div % 2 == (n // div) % 2 and div != n // div

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
os.system(f"cp gen.py {NO}.py")
