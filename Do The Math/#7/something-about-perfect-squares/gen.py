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

N_SETS = 4
SET_NAMES = ["tiny", "small", "big", "large"]

QS = [10**2, 10**3, 10**4, 4 * 10**5]
NS = [10**2, 10**6, 10**9, 10**18]


# @numba.njit
def generate(no: int):
    generator = Generator(Q=QS[no], N=NS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, queries in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{len(queries)}\n")
        input.write("\n".join([f"{x} {y}" for (x, y, _) in queries]))
        output.write("\n".join([f"{ans}" for (_, _, ans) in queries]))
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
