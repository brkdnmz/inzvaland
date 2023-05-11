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


@numba.njit
def solve():
  c = randint(1, 10**5)
  n = [0] * c
  for i in range(c):
    n[i] = randint(1, 10**9)
  k = randint(1, 10**9)

  l, r = 0, 10**18
  while l < r:
    mid = (l+r+1)//2
    tot = 0
    for i in range(c):
      tot += min(n[i], mid)
    assert tot >= 0
    if tot//mid >= k:
      l = mid
    else:
      r = mid-1
  return c, n, k, l


for tc in range(10):
  c, n, k, ans = solve()
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{c} {k}\n")
  for i in range(c):
    input.write(f"{n[i]}")
    if i+1 != c:
      input.write(" ")

  output.write(f"{ans}")
