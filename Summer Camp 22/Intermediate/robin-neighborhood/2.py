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


# @numba.njit
def gen_tree_edges(n):
  edges = []
  nodes = list(range(1, n+1))
  # np.random.shuffle(nodes)
  shuffle(nodes)
  for i, node in enumerate(nodes):
    if i == 0:
      continue
    parent = nodes[randint(0, i-1)]
    u = node
    v = parent
    if randint(0, 1):
      u, v = v, u
    edges.append((u, v))
  return edges


# @numba.njit
def gen_adj(n, edges):
  adj = [[] for _ in range(n+1)]
  for edge in edges:
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])
  return adj


def dfs(cur, par, g, dp, val):
  dp[cur][1] = val[cur]
  for nxt in g[cur]:
    if nxt == par:
      continue
    dfs(nxt, cur, g, dp, val)
    dp[cur][1] += dp[nxt][0]
    dp[cur][0] += max(dp[nxt])


N = 2 * 10**5
V = 10**9


# @numba.njit
def solve(n, g):
  dp = [[0, 0] for _ in range(n+1)]
  val = np.random.randint(1, V+1, (n+1,), np.int0)
  dfs(1, 0, g, dp, val)
  return val[1:], max(dp[1])


for tc in range(5):
  n = N
  edges = gen_tree_edges(n)
  val, ans = solve(n, gen_adj(n, edges))

  input = open(f"input/input{tc}.txt", "w")
  output = open(f"output/output{tc}.txt", "w")

  input.write(f"{n}\n")
  for i, edge in enumerate(edges):
    input.write(f"{edge[0]} {edge[1]}\n")

  for i, c in enumerate(val):
    input.write(f"{c}")
    if i+1 != len(val):
      input.write(" ")

  output.write(f"{ans}")
