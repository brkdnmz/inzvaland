import os
from collections import defaultdict
from glob import glob
from symbol import namedexpr_test

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

N_SETS = 3
SET_NAMES = ["small", "big", "large"]

NS = [10**3, 10**4, 2 * 10**5]
QS = [10**3, 10**4, 2 * 10**5]


# @numba.njit
def generate(no: int):
    generator = Generator(N=NS[no], Q=QS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, ((n, q, edges, queries), answers) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{n} {q}\n")
        input.write("\n".join(f"{u} {v}" for u, v in edges))
        input.write("\n")
        input.write("\n".join(f"{u} {v}" for u, v in queries))
        output.write("\n".join(f"{lca} {dist}" for lca, dist in answers))
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    # os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
