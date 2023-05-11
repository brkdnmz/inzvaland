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

SMALL = 10
MED = 100
BIG = 1000

LOWER = 1
UPPER = SMALL
NO = 1
SET_NAME = f"small"
N_TC = 5


# @numba.njit
def generate():
    n = randint(LOWER, UPPER)
    p = [i for i in range(n)]
    shuffle(p)
    ans = 0
    for i in range(n):
        vis = [False for _ in range(n)]
        cur = i
        while not vis[cur]:
            vis[cur] = True
            ans += 1
            cur = p[cur]
    ans = n**2 - ans
    r = []
    for i in range(n):
        r.append([i + 1, p[i] + 1])
    shuffle(r)
    return n, r, ans


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    n, r, ans = generate()
    input.write(f"{n}\n")
    for i, [x, y] in enumerate(r):
        input.write(f"{x} {y}")
        input.write("\n" if i + 1 < n else "")
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
