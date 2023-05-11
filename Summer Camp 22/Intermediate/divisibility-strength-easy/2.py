from glob import glob
import math
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

P = 10**6 + 5
is_p = np.array([1] * P)
p_cnt = np.array([0] * P)


@numba.njit
def precalc_p(p_cnt, is_p):
  is_p[0] = is_p[1] = 0
  for i in range(2, P):
    p_cnt[i] += p_cnt[i-1]
    if not is_p[i]:
      continue
    for j in range(i*i, P, i):
      is_p[j] = 0
    cur = i
    while cur < P:
      p_cnt[cur] += 1
      cur *= i


precalc_p(p_cnt, is_p)


def solve(ns):
  ans = np.zeros_like(ns)
  for i, n in enumerate(ns):
    ans[i] = p_cnt[n+1]
  return ans


Q = 10**5
N = 10**6
for tc in range(1):
  q = Q
  ns = N * np.ones((q, ), np.int0)
  ans = solve(ns)
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{q}\n")
  for i, n in enumerate(ns):
    input.write(f"{n}")
    if i+1 != q:
      input.write("\n")

  for i, n in enumerate(ans):
    output.write(f"{n}")
    if i+1 != q:
      output.write("\n")
