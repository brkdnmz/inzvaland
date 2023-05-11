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

N = 10**6
seg = [0]*(4*N+20)


def update(cur, l, r, target, op):
    if not(l <= target <= r):
        return
    if l == r:
        if op == 0:
            seg[cur] |= 1
        else:
            seg[cur] ^= 1
        return

    mid = (l+r)//2
    update(2*cur, l, mid, target, op)
    update(2*cur+1, mid+1, r, target, op)
    seg[cur] = seg[2*cur] + seg[2*cur+1]


def get(cur, l, r, tl, tr):
    if tl > r or tr < l:
        return 0
    if tl <= l and r <= tr:
        return seg[cur]

    mid = (l+r)//2
    return get(2*cur, l, mid, tl, tr) + get(2*cur+1, mid+1, r, tl, tr)


for tc in range(5):
    A = 10**9
    seg = [0]*(4*N+20)
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    q = randint(1, 10**3)

    input.write(str(q) + "\n")

    flipped = False
    # Last query is preserved for type-2
    for i in range(q-1):
        type = randint(1, 4)
        if type == 1:
            i = randint(0, 10**3)
            update(1, 0, N, i, op=0)
            input.write("1 " + str(i) + "\n")
        elif type == 2:
            i = randint(0, 10**3)
            update(1, 0, N, i, op=1)
            input.write("2 " + str(i) + "\n")
        elif type == 3:
            flipped = not flipped
            input.write("3\n")
        else:
            i = randint(0, 10**3)
            j = randint(0, 10**3-i)
            if not j:
                ans = 0
            else:
                ans = get(1, 0, N, i, min(N, i+j-1))
                if flipped:
                    ans = min(N, i+j-1) - i + 1 - ans
            input.write("4 " + str(i) + " " + str(j) + "\n")
            output.write(str(ans) + "\n")

    # Last query
    i = randint(0, 10**3)
    j = randint(0, 10**3-i)
    if not j:
        ans = 0
    else:
        ans = get(1, 0, N, i, min(N, i+j-1))
        if flipped:
            ans = min(N, i+j-1) - i + 1 - ans
    input.write("4 " + str(i) + " " + str(j))
    output.write(str(ans))
