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

SMALL = 10**6
MED = 10**9
BIG = 10**12

LOWER = 1
UPPER = 1
NO = 4
SET_NAME = f"min"
N_TC = 3

MOD = 10**9 + 7


# @numba.njit
def generate(m_idx):
    n = 1
    ms = [1, randint(2, 10**6 - 1), 10**6]
    m = ms[m_idx]
    ans = 1
    init_n = n
    for i in range(2, n):
        if i**2 > n:
            break
        if n % i:
            continue
        exp = 0
        while n % i == 0:
            n //= i
            exp += 1
        ans *= (pow(exp + 1, m, MOD) - pow(exp, m, MOD) + MOD) % MOD
        ans %= MOD
    if n > 1:
        ans *= (pow(2, m, MOD) - 1 + MOD) % MOD
        ans %= MOD
    n = init_n
    return n, m, ans


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    n, m, ans = generate(m_idx=tc)
    input.write(f"{n} {m}")
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
