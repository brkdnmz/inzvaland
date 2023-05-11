import os
from collections import defaultdict
from glob import glob
from symbol import namedexpr_test

import numba
import numpy as np
from sklearn.preprocessing import quantile_transform

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

DS = [10**3, 10**6, 10**9]
NS = [5, 10, 1000]

# @numba.njit
def generate(no: int):
    generator = Generator(N=NS[no], D=DS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, ((d, otis, maeve), ans) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{d}\n")
        input.write(" ".join(map(str, otis)))
        input.write("\n")
        input.write(" ".join(map(str, maeve)))
        output.write(f"{ans:.2f}")
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    # os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
