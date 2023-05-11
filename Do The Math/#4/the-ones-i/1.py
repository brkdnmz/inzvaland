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

SMALL = 10**6
MED = 10**9
BIG = 10**12

LOWER = 1
UPPER = SMALL
NO = 1
SET_NAME = f"small"
N_TC = 3

MOD = 10**9 + 7


@numba.njit
def generate():
    n = randint(LOWER, UPPER)
    ans = 1
    init_n = n
    for i in range(2, n):
        if i**2 > n:
            break
        if n % i:
            continue
        exp = 0
        while n % i == 0:
            n //= i
            exp += 1
        ans *= (exp + 1) ** 3 - exp**3
    if n > 1:
        ans *= 2**3 - 1
    n = init_n
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
