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

NS = [10**6, 10**9, 10**12]
MS = [10**3, 10**5, 10**5]


# @numba.njit
def generate(no: int):
    generator = Generator(N=NS[no], M=MS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, ((n, m, lines), ans) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{n} {m}\n")
        input.write(" ".join([str(x) for x in lines]))
        output.write(f"{ans}")
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    # os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
