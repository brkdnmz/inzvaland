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

NS = [10**3, 10**6, 5 * 10**6]
QS = [10, 10**3, 10**5]


# @numba.njit
def generate(no: int):
    generator = Generator(N=NS[no], Q=QS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, ((q, queries), ans) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{q}\n")
        input.write("\n".join(map(str, queries)))
        output.write(
            "\n".join(f"{ans[i][0]}\n" + (" ".join(map(str, ans[i][1]))) for i in range(q))
        )
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    # os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
