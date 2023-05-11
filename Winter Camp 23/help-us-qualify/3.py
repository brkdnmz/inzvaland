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

N_SETS = 4
SET_NAMES = ["tiny", "small", "big", "large"]

HS = [10**2, 100**6, 10**9, 10**12]


# @numba.njit
def generate(no: int):
    generator = Generator(H=HS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, ((a, b), ans) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{a} {b}")
        output.write(f"{ans}")
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
