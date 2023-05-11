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


NO = 2
SET_NAME = f"small"

QS = [10**2, 10**3, 10**4, 2 * 10**5]
NS = [10**2, 10**3, 10**5, 5 * 10**6]

# @numba.njit
def generate():
    generator = Generator(Q=QS[NO - 1], N=NS[NO - 1])
    return generator.generate_all()


testcases = generate()
for tc, queries in enumerate(testcases):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    input.write(f"{len(queries)}\n")
    input.write("\n".join([f"{n}" for (n, _) in queries]))
    output.write("\n".join([f"{ans}" for (_, ans) in queries]))
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME}.zip" input output')
os.system(f"copy gen.py {NO}.py")
