import os
from glob import glob
from random import *
from math import *
from typing import List, TextIO
import numba

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

SMALL = 100
MED = 10**3
BIG = 10**6

NO = 4
TC_NAME = "l 1 r 1e6"
N_TC = 1


@numba.njit
def solve():
    """
        If `longest(S+) >= i`, then `a-1` is divisible by all integers from `1` to `i+1`.\\
        `a-1` is a multiple of `lcm(1, 2, 3, ..., i+1)`.
    """
    l = 1
    r = BIG
    ans = [0] * 15
    lcm = 1
    for i in range(15):
        lcm = lcm * (i+2) // gcd(lcm, i+2)
        ans[i] = (r-1) // lcm - max(0, l-2) // lcm + (l == 1)

    return l, r, ans


def write_1d(l: List[int], out: TextIO, sep=" ", last=False):
    assert len(l)

    out.write(f"{l[0]}")
    for x in l[1:]:
        out.write(sep + f"{x}")
    if not last:
        out.write("\n")


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")

    l, r, ans = solve()

    write_1d([l, r], input, last=True)

    write_1d(ans, output, last=True)

    input.close()
    output.close()

os.system(f"zip -r \"{NO}. {TC_NAME} {N_TC}.zip\" input output")
os.system(f"copy gen.py {NO}.py")
