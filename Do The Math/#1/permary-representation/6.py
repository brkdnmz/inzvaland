import os
from glob import glob
from random import *

import numba
import numpy as np

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

SMALL = 5
MED = 10
BIG = 20

NO = 6
SET_NAME = "max limit, one swap"
N_TC = 3


@numba.njit
def generate_test_cases(t=1):
    n = BIG
    p = np.array([i + 1 for i in range(n)])
    swap_idx = [randint(0, n - 1), randint(0, n - 1)]
    p[swap_idx[0]], p[swap_idx[1]] = p[swap_idx[1]], p[swap_idx[0]]
    # shuffle(p)
    number = 1
    factorial_rep = []

    def fac(x):
        res = 1
        for i in range(x):
            res *= i + 1
        return res

    for i in range(n):
        cnt_smaller = 0
        for j in range(i + 1, n):
            cnt_smaller += p[j] < p[i]
        if i + 1 < n:
            factorial_rep.append(cnt_smaller)
        number += cnt_smaller * fac(n - 1 - i)
    return n, p, number, factorial_rep


def write_test_cases_to_file(l, out):
    write_single_test_case_to_file(l[0], out)
    for i, x in enumerate(l[1:]):
        write_single_test_case_to_file(x, out, sep=" ", last=i + 1 == len(l[1:]))


def write_single_test_case_to_file(l, out, sep=" ", last=False):
    out.write(f"{l[0]}")
    for x in l[1:]:
        out.write(sep + f"{x}")
    if not last:
        out.write("\n")


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")

    n, p, number, factorial_rep = generate_test_cases(1)

    write_single_test_case_to_file([n], input)
    write_single_test_case_to_file(p, input, sep=" ", last=True)

    write_single_test_case_to_file([number], output)
    write_single_test_case_to_file(factorial_rep, output, sep=" ", last=True)

    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
