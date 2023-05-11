from collections import defaultdict, deque
from enum import Enum
from glob import glob
import os
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

N = [10**3, 10**6,     10**11]
R = [10,    10**4,  5 * 10**4]
A = [10,    10**2,      10**3]


@numba.njit
def solve():
  n = 10**11
  r = np.ones((11,), np.int0) * 1
  a = [np.ones((r[i],), np.int0) * 1 for i in range(11)]
  sums = [np.zeros((r[i] + 1,), np.int0) for i in range(11)]
  for i in range(11):
    for j in range(1, r[i] + 1):
      sums[i][j] = sums[i][j-1] + a[i][j-1]
  lo, hi = 0, n
  while lo < hi:
    mid = (lo + hi + 1) // 2
    total = n
    for i in range(11):
      total -= mid // r[i] * sums[i][-1] + sums[i][mid % r[i]]
    if total < 0:
      hi = mid-1
    else:
      lo = mid
  ans = lo
  return n, r, a, ans


for tc in range(1):
  n, r, a, ans = solve()
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{n}\n")
  for i in range(11):
    input.write(f"{r[i]}\n")
    a_str = " ".join(map(str, a[i]))
    if i+1 != 11:
      a_str += "\n"
    input.write(a_str)

  output.write(f"{ans}")
