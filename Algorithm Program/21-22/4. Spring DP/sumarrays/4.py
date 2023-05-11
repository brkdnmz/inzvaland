import glob
import os
from random import randint
import numba

import numpy as np
from sklearn.utils import shuffle

files = glob.glob("input/*")
for f in files:
    os.remove(f)
files = glob.glob("output/*")
for f in files:
    os.remove(f)

N = 10**5
A = 10**9


def solve():
    n = N
    k = n*(n+1)//2
    a = np.random.randint(-A, A+1, n, np.int64)
    prefix = np.zeros((n+1,), np.int64)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]

    @numba.njit
    def check(unsorted_prefix, l, r, sum):
        if l == r:
            return 0
        mid = (l+r)//2
        ans = check(unsorted_prefix, l, mid, sum) + \
            check(unsorted_prefix, mid+1, r, sum)

        p1 = l
        for p2 in range(mid+1, r+1):
            while p1 <= mid and unsorted_prefix[p2] - unsorted_prefix[p1] >= sum:
                ans += r-p2+1
                p1 += 1

        sorted_segment = np.zeros((r-l+1,), np.int64)
        ptr = 0
        p1 = l
        p2 = mid+1
        while p1 <= mid or p2 <= r:
            if p1 > mid:
                sorted_segment[ptr] = unsorted_prefix[p2]
                p2 += 1
            elif p2 > r:
                sorted_segment[ptr] = unsorted_prefix[p1]
                p1 += 1
            elif unsorted_prefix[p1] < unsorted_prefix[p2]:
                sorted_segment[ptr] = unsorted_prefix[p1]
                p1 += 1
            else:
                sorted_segment[ptr] = unsorted_prefix[p2]
                p2 += 1
            ptr += 1

        unsorted_prefix[l: r+1] = sorted_segment
        return ans

    l = -10**18
    r = 10**18
    while l < r:
        mid = (l+r+1)//2
        unsorted_prefix = prefix.copy()
        if check(unsorted_prefix, 0, n, mid) >= k:
            l = mid
        else:
            r = mid-1
    ans = l
    return n, k, a, ans


for tc in range(5):
    in_file = "input/input{}.txt".format(tc)
    input = open(in_file, "w")
    output = open("output/output{}.txt".format(tc), "w")
    n, k, a, ans = solve()
    input.write(str(n) + " " + str(k) + "\n")
    for i, x in enumerate(a):
        input.write(str(x))
        if i+1 != n:
            input.write(" ")
    output.write(str(ans))
    print("test case #", tc+1, "finished")
