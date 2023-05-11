import os
from glob import glob
from io import TextIOWrapper
from random import *
from typing import IO, List

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

SMALL = 50
MED = 250
BIG = 1000

indicated_prob = 0.6
NO = 2
SET_NAME = f"small indicated prob {indicated_prob}"
N_TC = 3


# @numba.njit
def generate_test_cases():
    t = randint(1, SMALL // 3)
    tot_rows = SMALL // 2
    tot_cols = SMALL // 2

    def gen_ints_sum_n(n: int, cnt: int) -> List[int]:
        assert n >= cnt >= 1
        cum_sums = list(np.random.choice(range(1, n), cnt - 1, replace=False))
        cum_sums.append(0)
        cum_sums.append(n)
        cum_sums.sort()
        return [cum_sums[i + 1] - cum_sums[i] for i in range(cnt)]

    def gen_grid(n: int, m: int, prob: float) -> List[str]:
        l, r = sorted(list(np.random.choice(range(m), 2)))
        u, d = sorted(list(np.random.choice(range(n), 2)))
        indicated_cnt = int(prob * (r - l + 1) * (d - u + 1))
        indicateds = []
        for i in range(u, d + 1):
            for j in range(l, r + 1):
                indicateds.append((i, j))
        shuffle(indicateds)
        indicateds = indicateds[:indicated_cnt]
        grid = [[0] * m for _ in range(n)]
        for i, j in indicateds:
            grid[i][j] = 1
        chars = [".", "*"]
        for i in range(n):
            grid[i] = [chars[grid[i][j]] for j in range(m)]
            grid[i] = "".join(grid[i])
        return grid

    # ns and ms are both > 1
    ns: List[int] = [2 * x for x in gen_ints_sum_n(tot_rows, t)]
    ms: List[int] = [2 * x for x in gen_ints_sum_n(tot_cols, t)]
    grids: List[List[str]] = []
    anss: List[int] = []

    assert len(ns) == t and min(ns) > 1 and sum(ns) <= SMALL
    assert len(ms) == t and min(ms) > 1 and sum(ms) <= SMALL

    for tc in range(t):
        n = ns[tc]
        m = ms[tc]
        grid = gen_grid(ns[tc], ms[tc], prob=indicated_prob)
        grids.append(grid)
        lmost = m
        rmost = 0
        umost = n
        bmost = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "*":
                    lmost = min(lmost, j)
                    rmost = max(rmost, j)
                    umost = min(umost, i)
                    bmost = max(bmost, i)
        ans = 0
        if lmost != m:
            ans = (lmost + 1) * (m - rmost) * (umost + 1) * (n - bmost)
        anss.append(ans)
    return ns, ms, grids, anss


def write_grid(input: TextIOWrapper, grid: List[str]):
    n = len(grid)
    for i in range(n):
        input.write(grid[i] + ("" if i + 1 == n else "\n"))


for tc in range(N_TC):
    input = open(f"input/input{tc}.txt", "w")
    output = open(f"output/output{tc}.txt", "w")

    ns, ms, grids, anss = generate_test_cases()
    t = len(ns)
    input.write(f"{t}\n")
    for i in range(t):
        end = "" if i + 1 == t else "\n"
        n = ns[i]
        m = ms[i]
        grid = grids[i]
        ans = anss[i]
        input.write(f"{n} {m}\n")
        write_grid(input, grid)
        input.write(end)
        output.write(f"{ans}")
        output.write(end)
    input.close()
    output.close()

os.system(f'zip -r "{NO}. {SET_NAME} {N_TC}.zip" input output')
os.system(f"copy gen.py {NO}.py")
