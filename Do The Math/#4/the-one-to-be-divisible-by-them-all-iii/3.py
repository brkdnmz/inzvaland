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

SMALL = 10**3
MED = 10**5
BIG = 5 * 10**6
Q_SMALL = 10**2
Q_MED = 10**3
Q_BIG = 10**5

LOWER = MED + 1
UPPER = BIG
Q_LOWER = Q_MED + 1
Q_UPPER = Q_BIG
NO = 3
SET_NAME = f"big"
N_TC = 3

MOD = 10**9 + 7


@numba.njit
def generate():
    q = randint(Q_LOWER, Q_UPPER)
    ns = [randint(LOWER, UPPER) for _ in range(q)]
    anss = []
    is_p = [True for _ in range(UPPER + 1)]
    n_primes = [0 for _ in range(UPPER + 1)]

    for i in range(2, UPPER + 1):
        n_primes[i] = n_primes[i - 1]
        if not is_p[i]:
            continue
        n_primes[i] += 1
        for k in range(i * i, UPPER + 1, i):
            is_p[k] = False

    for n in ns:
        anss.append(n_primes[n])
    return q, ns, anss


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    q, ns, anss = generate()
    input.write(f"{q}\n")
    for i, n in enumerate(ns):
        input.write(f"{n}\n")
        output.write(f"{anss[i]}\n")
    # input.seek(input.tell() - 1, os.SEEK_SET)
    input.truncate(input.tell() - 2)
    # output.seek(output.tell() - 1, os.SEEK_SET)
    output.truncate(output.tell() - 2)
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
