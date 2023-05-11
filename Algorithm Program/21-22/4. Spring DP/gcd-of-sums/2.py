import glob
import os
from random import randint
import numba

import numpy as np
from sklearn.utils import shuffle

files = glob.glob("input/*")
for f in files:
  os.remove(f)
files = glob.glob("output/*")
for f in files:
  os.remove(f)

N = 10**5
A = 10**9


@numba.njit
def solve():
  n = N
  a = np.ones((n,), dtype=np.int0) * A
  total = a.sum()
  k = 1
  div = 2
  while 1:
    if div * div > total:
      break
    if total % div == 0:
      while total % div == 0:
        total /= div
      cur_k = 0
      cur_sum = 0
      for i in range(n):
        cur_sum += a[i]
        if cur_sum % div == 0:
          cur_k += 1
          cur_sum = 0
      k = max(k, cur_k)
    div += 1
  # total might be a prime number now
  if total > 1:
    cur_k = 0
    cur_sum = 0
    for i in range(n):
      cur_sum += a[i]
      if cur_sum % total == 0:
        cur_k += 1
        cur_sum = 0
    k = max(k, cur_k)
  return n, a, k


for tc in range(1):
  in_file = "input/input{}.txt".format(tc)
  input = open(in_file, "w")
  output = open("output/output{}.txt".format(tc), "w")

  n, a, k = solve()
  input.write(str(n) + "\n")
  for i, x in enumerate(a):
    input.write(str(x))
    if i+1 != n:
      input.write(" ")
  output.write(str(k))
  print("tc {} finished".format(tc+1))
  print("k={}".format(k))
