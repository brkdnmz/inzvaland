import os
from collections import defaultdict
from glob import glob
from symbol import namedexpr_test
from typing import List

import numba
import numpy as np

from funcs import Generator, TestCase

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

NS = [10, 50, 100, 1000]


def generate(no: int) -> List[TestCase]:
    generator = Generator(N=NS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, ((n, m, grid), ans) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{n} {m}\n")
        input.write("\n".join(["".join(grid[i]) for i in range(n)]))
        output.write(f"{ans}")
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    print(f"Set #{no} done")
