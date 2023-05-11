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

SET_NAMES = ["small", "big", "large"]
N_SETS = len(SET_NAMES)

NS = [10**6, 10**9, 10**12]


# @numba.njit
def generate(no: int):
    generator = Generator(N=NS[no])
    return generator.generate_all()


for no in range(N_SETS):
    testcases = generate(no)
    for tc, (n, phi) in enumerate(testcases):
        input = open(f"input/input{tc}.txt", "w")
        output = open(f"output/output{tc}.txt", "w")
        input.write(f"{n}")
        output.write(f"{phi}")
        input.close()
        output.close()

    os.system(f'zip -r "{no}. {SET_NAMES[no]}.zip" input output')
    # os.system(f"copy gen.py {no}.py")

    print(f"Set #{no} done")
