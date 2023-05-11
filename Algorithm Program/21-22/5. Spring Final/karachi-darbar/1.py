from bisect import bisect_left
from collections import defaultdict
import os
from random import *
from cv2 import magnitude
import numba
import numpy as np

if not os.path.exists("input"):
  os.makedirs("input")
if not os.path.exists("output"):
  os.makedirs("output")

N = 10**9
M = 2 * 10**5


# @numba.njit
def solve():
  n = randint(1, N)
  m = randint(1, M)
  s = randint(1, M)
  a = np.zeros((m, 2), np.int0)
  l = np.zeros((m,), np.int0)
  r = np.zeros((m,), np.int0)
  for i in range(m):
    a[i][0] = randint(1, n)
    a[i][1] = randint(a[i][0], n)
    l[i] = a[i][0]
    r[i] = a[i][1]
  l.sort()
  r.sort()
  b = np.zeros((s, 2), np.int0)
  ans = np.zeros((s,), np.int0)
  for i in range(s):
    b[i][0] = randint(1, n)
    b[i][1] = randint(b[i][0], n)
    cl, cr = b[i]
    ans[i] = bisect_left(l, cr+1) - bisect_left(r, cl)
  return n, m, s, a, b, ans


for tc in range(10):
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")
  n, m, s, a, b, ans = solve()
  input.write(f"{n} {m}\n")
  for l, r in a:
    input.write(f"{l} {r}\n")

  input.write(f"{s}\n")

  for i, [l, r] in enumerate(b):
    input.write(f"{l} {r}")
    if i+1 < s:
      input.write("\n")
  for i, x in enumerate(ans):
    output.write(f"{x}")
    if i+1 < s:
      output.write("\n")
