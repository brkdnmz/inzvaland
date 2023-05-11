from io import open_code
from pickletools import opcodes
from platform import java_ver
from random import *
import os
import glob

files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

N = 2 * 10**5
seg = [[0]*2 for _ in range(4*N+20)]
INF = 10**10


def update(cur, l, r, target, val):
    if not(l <= target <= r):
        return
    if l == r:
        seg[cur] = [val, val]
        return

    mid = (l+r)//2
    update(2*cur, l, mid, target, val)
    update(2*cur+1, mid+1, r, target, val)
    seg[cur] = [min(seg[2*cur][0], seg[2*cur+1][0]),
                max(seg[2*cur][1], seg[2*cur+1][1])]


def get(cur, l, r, tl, tr):
    if tl > r or tr < l:
        return [INF, -INF]
    if tl <= l and r <= tr:
        return seg[cur]

    mid = (l+r)//2
    left = get(2*cur, l, mid, tl, tr)
    right = get(2*cur+1, mid+1, r, tl, tr)
    return [min(left[0], right[0]), max(left[1], right[1])]


for tc in range(2):
    A = 10**9
    seg = [[0]*2 for _ in range(4*N+20)]
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    n = N
    k = 0
    a = [1 if randint(0, 3) else 0 for _ in range(n)]

    input.write(str(n) + " " + str(k) + "\n")
    for i, x in enumerate(a):
        input.write(str(x))
        if i+1 < len(a):
            input.write(" ")
        update(1, 0, n-1, i, x)

    l = 0
    for i in range(n):
        mn, mx = get(1, 0, n-1, l, i)
        while mx - mn > k:
            l += 1
            mn, mx = get(1, 0, n-1, l, i)

        output.write(str(l))
        if i+1 < n:
            output.write(" ")
