from bisect import bisect_left
from collections import defaultdict
from glob import glob
import os
from random import *
import numba
import numpy as np
from sklearn.metrics import r2_score

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


N = 5
M = 10
X = 10


# @numba.njit
def solve():
  m = randint(1, M)
  qs = np.zeros((m, 4), np.int0)
  vals = np.zeros((2*m, 2), np.int0)
  for i in range(m):
    t = randint(1, 2)
    l = randint(-N, N)
    r = randint(l, N)
    x = randint(-X, X)
    qs[i] = [t, l, r, x]
    vals[2*i] = [l, i]
    vals[2*i+1] = [r, i]
  ranks = -np.ones((m, 2), np.int0)
  vals = vals[vals[:, 0].argsort()]
  rank = -1
  last = -N-1
  val_of_rank = np.zeros((2*m,), np.int0)
  for endpoint, i in vals:
    assert endpoint >= last
    if endpoint > last:
      last = endpoint
      rank += 1
    if ranks[i][0] == -1:
      ranks[i][0] = rank
    else:
      ranks[i][1] = rank
    val_of_rank[rank] = endpoint

  seg = np.zeros((8*m+5,), np.int0)
  lazy = np.zeros((8*m+5,), np.int0)

  def get_cnt(l, r):
    return val_of_rank[r] - val_of_rank[l] + 1

  def prop(c, l, r):
    seg[c] += get_cnt(l, r) * lazy[c]
    if l != r:
      lazy[2*c] += lazy[c]
      lazy[2*c+1] += lazy[c]
    lazy[c] = 0

  def upd(c, l, r, tl, tr, x):
    prop(c, l, r)
    if l > tr or tl > r:
      return
    if tl <= l and r <= tr:
      lazy[c] = x
      prop(c, l, r)
      return

    mid = (l+r)//2
    upd(2*c, l, mid, tl, tr, x)
    upd(2*c+1, mid, r, tl, tr, x)
    seg[c] = seg[2*c] + seg[2*c+1]

  def get(c, l, r, tl, tr):
    prop(c, l, r)
    if l > tr or tl > r:
      return 0
    if tl <= l and r <= tr:
      return seg[c]
    mid = (l+r)//2
    ans = get(2*c, l, mid, tl, tr)
    ans += get(2*c+1, mid+1, r, tl, tr)
    seg[c] = seg[2*c] + seg[2*c+1]
    return ans
  ans = np.zeros((2*m,), np.int0)
  ans_ptr = 0
  brute = defaultdict(int)
  for i, [t, l, r, x] in enumerate(qs):
    actual_l = ranks[i][0]
    actual_r = ranks[i][1]
    assert actual_l <= actual_r and actual_r <= rank
    if t == 1:
      upd(1, 0, 2*m-1, actual_l, actual_r, x)
      for ii in range(l, r+1):
        brute[ii] += x
    else:
      ans[ans_ptr] = get(1, 0, 2*m-1, actual_l, actual_r)
      ans_ptr += 1
      brute_ans = 0
      for ii in range(l, r+1):
        brute_ans += brute[ii]
      if ans[ans_ptr-1] != brute_ans:
        print(qs)
        print(vals)
        print(ranks)
        print(val_of_rank)
        print(ans[ans_ptr-1], brute_ans)
        exit()
  ans = ans[:ans_ptr]
  return m, qs, ans


for tc in range(10):
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")
  m, qs, ans = solve()
  input.write(f"{m}\n")
  for i, [t, l, r, x] in enumerate(qs):
    input.write(f"{t} {l} {r}")
    if t == 1:
      input.write(f" {x}")
    if i+1 < m:
      input.write("\n")
  for i, x in enumerate(ans):
    output.write(f"{x}")
    if i+1 < len(ans):
      output.write("\n")
