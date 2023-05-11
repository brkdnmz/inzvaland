import os
from collections import defaultdict
from glob import glob

import numba
import numpy as np

from funcs import Generator

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

MOD = 10**9 + 7

SMALL = 10**2
MED = 10**3
BIG = 10**6

LOWER = 1
UPPER = BIG
NO = 1
SET_NAME = f"big"
N_TC = 1


# @numba.njit
def generate():
    generator = Generator(N=BIG)
    return generator.generate_all()


testcases = generate()
for tc, [h1, h2, ans] in enumerate(testcases):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    input.write(f"{h1} {h2}\n")
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
