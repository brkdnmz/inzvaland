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
BIG = 878279787138836568

LOWER = BIG
UPPER = BIG
NO = 5
SET_NAME = f"max"
N_TC = 1


@numba.njit
def generate():
    n = randint(LOWER, UPPER)
    ans = n // 2 - n // 4 + 1 + (n >= 4)
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
