import glob
import os
from random import randint
import numba

import numpy as np
from sklearn.utils import shuffle
from torch import rand

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
  total = N * A

  def p(x):
    i = 2
    while i*i <= x:
      if x % i == 0:
        return False
      i += 1
    return True
  while not p(total):
    total -= 1

  a = np.ones((n,), np.int0) * A
  for i in range(N*A - total):
    a[randint(0, n-1)] -= 1
  return n, a, 1


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
