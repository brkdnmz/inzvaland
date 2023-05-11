from collections import defaultdict
import os
from random import *
import numba

if not os.path.exists("input"):
  os.makedirs("input")
if not os.path.exists("output"):
  os.makedirs("output")

ans = {}
pref = defaultdict()
suf = defaultdict()


def solve(len):
  if len in ans.keys():
    return ans[len]
  if len <= 1:
    pref[len] = suf[len] = 0
    ans[len] = 1
    return
  l, r = len//2, (len+1)//2
  solve(l)
  solve(r)
  pref[len] = max(pref[l], 1 + pref[r])
  suf[len] = max(suf[r], suf[l] + 1)
  ans[len] = max(1 + pref[r], pref[l] + 1, suf[l] + pref[r])


ns = []
for tc in range(10):
  n = randint(2, 100)
  while n in ns:
    n = randint(2, 100)
  ns.append(n)
  solve(n)
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")
  input.write(str(n))
  output.write(str(ans[n]))
