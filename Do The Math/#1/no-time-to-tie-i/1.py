import os
from glob import glob
from random import *

import numba

# Create input and output folders if they don't exist
if not os.path.exists("input"):
    os.makedirs("input")
if not os.path.exists("output"):
    os.makedirs("output")

# Clear input and output folders if they contain anything
files = glob("input/*")
for f in files:
    os.remove(f)
files = glob("output/*")
for f in files:
    os.remove(f)

# You may define upper bounds for different levels as follows
SMALL = 10
MED = 10**6
BIG = 10**12

NO = 1
SET_NAME = "all"
N_TC = 20


@numba.njit
def generate_test_cases(t=1):
    b_s, ans_s = [], []

    def C(n, k):
        res = 1
        for x in range(n):
            res *= x+1
        for x in range(k):
            res //= x+1
        for x in range(n-k):
            res //= x+1
        return res
    for i in range(t):
        b = i+1
        ans = []
        for x in range(1, b+1):
            # x buttons, b places
            # b-x available empty spots
            if b-x >= x-1:
                # place x-1 empty spots between buttons
                # then distribute remaining b-2x+1 empty spots among x+1 places (leftmost & rightmost included) asdsad sad sad asd as
                ans.append(C(b-x+1, x))
            else:
                # place b-x empty spots between buttons
                # no empty spot will be left
                ans.append(C(x-1, b-x))
        ans_s.append(ans)
        b_s.append(b)
    return b_s, ans_s


def write_test_cases_to_file(l, out):
    """Write multiple test cases to the file `out`.

    Args:
        `l` (`List[List]`): Contains the test cases.
        `out`: File to write. Should pass `open("path-to-file", "w")`.
    """

    write_single_test_case_to_file(l[0], out)
    for i, x in enumerate(l[1:]):
        write_single_test_case_to_file(x, out, sep=" ", last=i+1 == len(l[1:]))


def write_single_test_case_to_file(l, out, sep=" ", last=False):
    """Write single test case to the file `out`.

    Args:
        `l` (`List`): Test case to write.
        `out`: File to write.
        `sep` (str, optional): Separator between the numbers in the test case. Defaults to " ".
        `last` (bool, optional): Whether this test case is the last. Defaults to False.
    """

    out.write(f"{l[0]}")
    for x in l[1:]:
        out.write(sep + f"{x}")
    if not last:
        out.write("\n")


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")

    b_s, ans_s = generate_test_cases(20)

    write_single_test_case_to_file([b_s[tc]], input, last=True)

    write_single_test_case_to_file(ans_s[tc], output, " ", last=True)

    input.close()
    output.close()

os.system(f"zip -r \"{NO}. {SET_NAME} {N_TC}.zip\" input output")
os.system(f"copy gen.py {NO}.py")
