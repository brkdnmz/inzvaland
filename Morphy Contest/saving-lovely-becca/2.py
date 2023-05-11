import os
from glob import glob

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

MOD = 10**9 + 7

TINY = 10
SMALL = 10**2
MED = 10**4
BIG = 3 * 10**5

NO = 2
SET_NAME = f"small"
N_TC = 1


# @numba.njit
def generate():
    generator = Generator(N=SMALL, R=50, A=359)
    return generator.generate_all()


testcases = generate()
for tc, [r, a, ans] in enumerate(testcases):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    input.write(f"{len(r)}\n")
    input.write(" ".join([str(x) for x in r]) + "\n")
    input.write(" ".join([str(x) for x in a]))
    output.write(f"{ans}")
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
