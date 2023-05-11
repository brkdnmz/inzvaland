import os
from collections import defaultdict
from glob import glob

import numba
import numpy as np
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

SMALL = 10**2
MED = 10**3
BIG = 10**6

LOWER = 1
UPPER = BIG
NO = 2
SET_NAME = f"med"
N_TC = 1


# @numba.njit
def generate():
    generator = Generator(n=10**4, low=10**5, high=10**9, n_high=100)
    return generator.generate_all()


prime_divisor = [0 for _ in range(BIG + 1)]
primes = []
for p in range(2, BIG + 1):
    if prime_divisor[p]:
        continue
    primes.append(p)
    prime_divisor[p] = p
    for k in range(p * p, BIG + 1, p):
        prime_divisor[k] = p


def solve(a: "list[int]"):
    answers = []
    exponents: "dict[int, int]" = defaultdict(int)
    for x in a:
        if x <= 10**6:
            while x > 1:
                divisor = prime_divisor[x]
                assert divisor > 1
                exponent = 0
                while x % divisor == 0:
                    exponent += 1
                    x //= divisor
                exponents[divisor] += exponent
        else:
            for p in primes:
                if p * p > x:
                    break
                if x % p:
                    continue
                assert p > 1
                exponent = 0
                while x % p == 0:
                    exponent += 1
                    x //= p
                exponents[p] += exponent
            if x > 1:
                exponents[x] += 1
        answers.append(pow(2, len(exponents), MOD))
    n_divisors = 2
    for p, e in exponents.items():
        n_divisors *= e + 1
        n_divisors %= MOD
    answers.append(n_divisors)
    return answers


a_s = generate()
for tc, a in enumerate(a_s):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")
    input.write(f"{len(a)}\n")
    input.write(" ".join([str(x) for x in a]))
    answers = solve(a)
    output.write("\n".join([str(answer) for answer in answers]))
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
