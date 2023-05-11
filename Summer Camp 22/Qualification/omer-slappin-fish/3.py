from collections import defaultdict, deque
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


def gen_grid(n, m):
  g = [['~']*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      g[i][j] = 'F' if not randint(0, 30) else '~'
  return g


N = 2 * 10**5


def solve():
  n = randint(1, int(N ** 0.5) * 3)
  m = N // n
  assert n*m <= N
  g = gen_grid(n, m)
  q = deque([])
  fish_dist = [[10**9]*m for _ in range(n)]
  omer_dist = [[10**9]*m for _ in range(n)]
  omer_dist[0][0] = 0
  q.append((0, 0))
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  def safe(i, j):
    return 0 <= i < n and 0 <= j < m
  # Perform BFS from Omer
  while len(q):
    cur = q.popleft()
    ci, cj = cur
    for d in range(4):
      i = ci + dx[d]
      j = cj + dy[d]
      if not safe(i, j):
        continue
      if omer_dist[i][j] <= omer_dist[ci][cj] + 1:
        continue
      omer_dist[i][j] = omer_dist[ci][cj] + 1
      q.append((i, j))
  # Perform multisource BFS from the fish
  for i in range(n):
    for j in range(m):
      if g[i][j] == 'F':
        q.append((i, j))
        fish_dist[i][j] = 0
  is_slap = [[0]*m for _ in range(n)]
  while len(q):
    cur = q.popleft()
    ci, cj = cur
    if omer_dist[ci][cj] >= fish_dist[ci][cj]:
      is_slap[ci][cj] = 1
    for d in range(4):
      i = ci + dx[d]
      j = cj + dy[d]
      if not safe(i, j):
        continue
      if fish_dist[i][j] <= fish_dist[ci][cj] + 1:
        continue
      fish_dist[i][j] = fish_dist[ci][cj] + 1
      q.append((i, j))
  # Calculate the minimum number of slaps until each cell
  min_slaps = [[10**9]*m for _ in range(n)]
  min_slaps[0][0] = is_slap[0][0]
  q.append((0, 0))
  while len(q):
    cur = q.popleft()
    ci, cj = cur
    for d in range(4):
      i = ci + dx[d]
      j = cj + dy[d]
      if not safe(i, j):
        continue
      if min_slaps[i][j] <= min_slaps[ci][cj] + is_slap[i][j]:
        continue
      min_slaps[i][j] = min_slaps[ci][cj] + is_slap[i][j]
      q.append((i, j))
  return n, m, g, min_slaps[n-1][m-1]


for tc in range(5):
  n, m, g, ans = solve()
  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{n} {m}\n")
  for i in range(n):
    for j in range(m):
      input.write(g[i][j])
    if i+1 != n:
      input.write("\n")
  output.write(str(ans))
