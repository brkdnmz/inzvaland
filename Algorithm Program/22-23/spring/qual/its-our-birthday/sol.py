from collections import defaultdict
from math import gcd

MOD = 10**9 + 7


def solve(n, a):
    dp = defaultdict(int)
    dp[(0, 1)] = 1
    for x in a:
        ndp = dp.copy()
        for (p, q) in dp:
            # p/q + 1/x
            pp = p * x + q
            qq = q * x
            if pp > qq:
                continue
            g = gcd(pp, qq)
            pp //= g
            qq //= g
            ndp[(pp, qq)] += dp[(p, q)]
            ndp[(pp, qq)] %= MOD
        dp = ndp
    return dp[(1, 1)]


n = int(input())
a = list(map(int, input().split()))

print(solve(n, a))
