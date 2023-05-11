from collections import defaultdict, deque
from enum import Enum
from glob import glob
from importlib import machinery
import os
from random import *
from re import T
import numba
import numpy as np
from sklearn.metrics import pair_confusion_matrix

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

N = [10**3, 10**9,     10**18]
P = [10,    10**3,      10**5]
M = [10,    10**3,      10**5]


# @numba.njit
def solve():
  n = 10**18
  p = np.random.randint(1, 10**5 + 1, (11,))
  m = np.ones((11,), np.int0)
  portions = []
  cycle_start = [0] * 11
  for i in range(11):
    portions.append([])
    vis = [False] * m[i]
    cur = p[i] % m[i]
    pos_of = defaultdict(int)
    while not vis[cur]:
      pos_of[cur] = len(portions[i])
      portions[i].append(cur)
      vis[cur] = True
      cur = cur * (i+1) % m[i]
    cycle_start[i] = pos_of[cur]
  sums = [[0] * (len(portions[i]) + 1) for i in range(11)]
  for i in range(11):
    for j in range(1, len(portions[i]) + 1):
      sums[i][j] = sums[i][j-1] + portions[i][j-1]

  def is_ovf(a, b, c):
    # a * b exceeds c
    if a == 0 or b == 0:
      return c < 0
    return a > c // b
  lo, hi = 0, n + 1
  while lo < hi:
    mid = (lo + hi + 1) // 2
    total = n
    for i in range(11):
      n_portions = len(portions[i])
      days_left = mid

      if portions[i][-1] == 0 or days_left <= n_portions:
        total -= sums[i][min(days_left, n_portions)]
        if total < 0:
          break
        continue

      total -= sums[i][n_portions]
      days_left -= n_portions

      n_cycle = n_portions - cycle_start[i]
      # sums[i] is 1-indexed (not cycle_start[i] - 1)
      cycle_sum = sums[i][-1] - sums[i][cycle_start[i]]
      if is_ovf(days_left // n_cycle, cycle_sum, total):
        total = -1
        break
      total -=\
          days_left // n_cycle * cycle_sum \
          + sums[i][cycle_start[i] + days_left % n_cycle] \
          - sums[i][cycle_start[i]]
    if total < 0:
      hi = mid-1
    else:
      lo = mid
  ans = lo if lo <= n else -1
  return n, p, m, ans


for tc in range(2):
  n, p, m, ans = solve()
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{n}\n")
  for i in range(11):
    input.write(f"{p[i]} {m[i]}")
    if i+1 != 11:
      input.write("\n")

  output.write(f"{ans}")
