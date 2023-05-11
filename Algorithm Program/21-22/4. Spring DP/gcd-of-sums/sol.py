import glob
import os
from random import randint
import numba

import numpy as np


@numba.njit
def solve(n, a):
  total = a.sum()
  print(total)
  k = 1
  div = 2
  while div * div <= total:
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
  return k


n = int(input())
a = np.array(list(map(int, input().split())))
print(solve(n, a))
