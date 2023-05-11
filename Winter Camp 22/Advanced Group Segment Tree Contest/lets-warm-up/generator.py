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
A = 10**9
seg = [0]*(4*N+5)


def add(cur, l, r, target, val):
    if not(l <= target <= r):
        return
    if l == r:
        seg[cur] += val
        return

    mid = (l+r)//2
    add(2*cur, l, mid, target, val)
    add(2*cur+1, mid+1, r, target, val)
    seg[cur] = max(seg[2*cur], seg[2*cur+1])


def get(cur, l, r, tl, tr):
    if tl > r or tr < l:
        return 0
    if tl <= l and r <= tr:
        return seg[cur]

    mid = (l+r)//2
    return max(get(2*cur, l, mid, tl, tr), get(2*cur+1, mid+1, r, tl, tr))


for tc in range(2):
    N = 2 * 10**5
    A = 10**9
    seg = [0]*(4*N+5)
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    n = N
    q = N
    a = [randint(0, 1) for i in range(n)]
    for i in range(n):
        add(1, 0, n-1, i, a[i])

    input.write(str(n) + " " + str(q) + "\n")
    for i, x in enumerate(a):
        input.write(str(x))
        if i+1 < n:
            input.write(" ")
    input.write("\n")

    # Last query is preserved for type-2
    for i in range(q-1):
        prob = randint(1, 3)
        # type = randint(1, 2)
        if prob == 1:
            i = randint(0, n-1)
            x = randint(0, 1)
            add(1, 0, n-1, i, x)
            input.write("1 " + str(i) + " " + str(x) + "\n")
        else:
            i = 0
            j = n-1
            ans = get(1, 0, n-1, i, j)
            input.write("2 " + str(i) + " " + str(j) + "\n")
            output.write(str(ans) + "\n")

    # Last query
    i = randint(0, n-1)
    j = randint(i, n-1)
    ans = get(1, 0, n-1, i, j)
    input.write("2 " + str(i) + " " + str(j))
    output.write(str(ans))
