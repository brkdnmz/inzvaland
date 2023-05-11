import os
from collections import defaultdict
from glob import glob

import numba
import numpy as np

from Generator import Generator

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

NS = [10, 50, 100]


# @numba.njit
def generate(no: int):
    generator = Generator(N=NS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, (points, alpha, ans) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(
            f"{points.ilkkan.x} {points.ilkkan.y} {points.yilmaz.x} {points.yilmaz.y} {points.ersoy.x} {points.ersoy.y}\n{alpha}"
        )
        output.write(f"{ans:.4f}")
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
