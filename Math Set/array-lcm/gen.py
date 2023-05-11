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

NS = [10, 10**4, 2 * 10**5]
AS = [10**5, 10**6, 5 * 10**6]


# @numba.njit
def generate(no: int):
    generator = Generator(N=NS[no], A=AS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, ((n, a), ans) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{n}\n")
        input.write(" ".join(map(str, a)))
        output.write(f"{ans}")
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    # os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
