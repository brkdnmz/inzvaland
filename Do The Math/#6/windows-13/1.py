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
MED2 = 10**5
BIG = 10**6

NO = 1
SET_NAME = f"small"
N_TC = 1


# @numba.njit
def generate():
    generator = Generator(Q=10, N=100, S=1)
    return generator.generate_all()


testcases = generate()
for tc, queries in enumerate(testcases):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    input.write(f"{len(queries)}\n")
    input.write("\n".join([f"{n} {s}" for (n, s, _) in queries]))
    output.write("\n".join([f"{ans}" for (_, _, ans) in queries]))
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
