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
seg = [0]*(4*N+20)
lazy = [0]*(4*N+20)
INF = 10**10


def propagate(cur, l, r):
    seg[cur] += lazy[cur]
    if l != r:
        lazy[2*cur] += lazy[cur]
        lazy[2*cur+1] += lazy[cur]
    lazy[cur] = 0


def update(cur, l, r, tl, tr):
    if tl <= l and r <= tr:
        lazy[cur] += 1

    propagate(cur, l, r)

    if tl > r or tr < l:
        return
    if tl <= l and r <= tr:
        return

    mid = (l+r)//2
    update(2*cur, l, mid, tl, tr)
    update(2*cur+1, mid+1, r, tl, tr)
    seg[cur] = max(seg[2*cur], seg[2*cur+1])


def get(cur, l, r, tl, tr):
    propagate(cur, l, r)
    if tl > r or tr < l:
        return 0
    if tl <= l and r <= tr:
        return seg[cur]

    mid = (l+r)//2
    left = get(2*cur, l, mid, tl, tr)
    right = get(2*cur+1, mid+1, r, tl, tr)
    return max(left, right)


for tc in range(3):
    seg = [0]*(4*N+20)
    lazy = [0]*(4*N+20)
    input = open("input/input{}.txt".format(tc), "w")
    output = open("output/output{}.txt".format(tc), "w")

    n = N
    q = N

    input.write(str(n) + " " + str(q) + "\n")

    for i in range(q-1):
        type = randint(1, 4)
        if type < 4:
            i = randint(0, n-1)
            j = randint(i, n-1)
            update(1, 0, n-1, i, j)
            input.write("1 " + str(i) + " " + str(j) + "\n")
        else:
            i = 0
            j = n-1
            ans = get(1, 0, n-1, i, j)
            input.write("2 " + str(i) + " " + str(j) + "\n")
            output.write(str(ans) + "\n")

    i = 0
    j = n-1
    ans = get(1, 0, n-1, i, j)
    input.write("2 " + str(i) + " " + str(j))
    output.write(str(ans))
