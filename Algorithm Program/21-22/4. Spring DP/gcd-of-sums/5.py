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
  n = randint(N//2, N)
  a = np.zeros((n,), np.int0)
  x = randint(1, A//100)
  for i in range(n):
    a[i] = x * randint(1, A//x)
  return n, a, n


for tc in range(5):
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
