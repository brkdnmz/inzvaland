import os
from glob import glob
from random import *

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
MED = 1000
BIG = 5000

NO = 1
SET_NAME = "small"
N_TC = 5

MOD = 10**9 + 7


@numba.njit
def generate_test_cases(t=1):
    b, ans = 0, []

    C = [[0]*5005 for _ in range(5005)]
    for i in range(5005):
        for j in range(i+1):
            if j == 0:
                C[i][j] = 1
            elif i == 0:
                C[i][j] = 0
            else:
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

    b = randint(1, SMALL)
    for x in range(1, b+1):
        # x buttons, b places
        # b-x available empty spots
        if b-x >= x-1:
            # place x-1 empty spots between buttons
            # then distribute remaining b-2x+1 empty spots among x+1 places (leftmost & rightmost included) asdsad sad sad asd as
            ans.append(C[b-x+1][x])
        else:
            # place b-x empty spots between buttons
            # no empty spot will be left
            ans.append(C[x-1][b-x])
    return b, ans


def write_test_cases_to_file(l, out):
    write_single_test_case_to_file(l[0], out)
    for i, x in enumerate(l[1:]):
        write_single_test_case_to_file(x, out, sep=" ", last=i+1 == len(l[1:]))


def write_single_test_case_to_file(l, out, sep=" ", last=False):
    out.write(f"{l[0]}")
    for x in l[1:]:
        out.write(sep + f"{x}")
    if not last:
        out.write("\n")


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")

    b, ans = generate_test_cases(1)

    write_single_test_case_to_file([b], input, last=True)

    write_single_test_case_to_file(ans, output, " ", last=True)

    input.close()
    output.close()

os.system(f"zip -r \"{NO}. {SET_NAME} {N_TC}.zip\" input output")
os.system(f"copy gen.py {NO}.py")
