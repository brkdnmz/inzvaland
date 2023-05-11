from glob import glob
import math
import os
from random import *
import numba
import numpy as np
from numba.typed import List

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

N = 10**5
V = 10**6

sm_p = np.array([0] * (V+1))
primes = List([2])


@numba.njit
def precalc_p(sm_p, primes: list):
  for i in range(2, V+1):
    if sm_p[i]:
      continue
    if i > 2:
      primes.append(i)
    for j in range(i, V+1, i):
      sm_p[j] = i


precalc_p(sm_p, primes)


# @numba.njit
def solve(primes):
  n = N
  p = primes[randint(len(primes)//2, len(primes) - 1)]
  s = np.ones((n, ), np.int0) * p
  one_indices = sorted(sample(range(n-1), randint(1, n//10)))
  for i in range(1, len(one_indices)):
    if one_indices[i] == one_indices[i-1] + 1:
      one_indices[i] += 1
    s[one_indices] = 1
  return n, s, 1


for tc in range(5):
  n, s, ans = solve(primes)
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{n}\n")
  for i, si in enumerate(s):
    input.write(f"{si}")
    if i+1 != n:
      input.write(" ")

  output.write(str(ans))
