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


@numba.njit
def solve(primes):
  n = N
  base = randint(1, 10**4)
  s = np.ones((n, ), np.int0) * base
  ans = base
  for p in primes:
    if min(s) * p > V:
      break
    mn1, mn2 = 100, 100
    for i in range(n):
      mx = int(math.log(V//s[i]) / math.log(p))
      if not mx:
        if 0 <= mn1:
          mn2 = mn1
          mn1 = 0
        elif 0 < mn2:
          mn2 = 0
        continue
      mx = max(1, mx - 4)
      exp = randint(1, mx)
      s[i] *= p**exp
      if exp <= mn1:
        mn2 = mn1
        mn1 = exp
      elif exp < mn2:
        mn2 = exp
    ans *= p**mn2

  return n, s, ans


for tc in range(15):
  n, s, ans = solve(primes)
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{n}\n")
  for i, si in enumerate(s):
    input.write(f"{si}")
    if i+1 != n:
      input.write(" ")

  output.write(str(ans))
