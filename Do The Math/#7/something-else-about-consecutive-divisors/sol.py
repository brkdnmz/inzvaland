from math import gcd

lcm = [1]
K = 1000
N = 10**18
for i in range(1, K + 5):
    lcm.append(1)
    cur_lcm = lcm[i - 1] * i // gcd(lcm[i - 1], i)
    cur_lcm = min(cur_lcm, N + 1)
    if cur_lcm > N:
        lcm.pop()
        break
    lcm[i] = cur_lcm


def calc_up_to_bound(bound: int, k: int) -> int:
    return bound // (lcm[k] if k < len(lcm) else N + 1) - bound // (
        lcm[k + 1] if k + 1 < len(lcm) else N + 1
    )


def calc_within_bounds(l: int, r: int, k: int) -> int:
    return calc_up_to_bound(r, k) - calc_up_to_bound(l - 1, k)


q = int(input())

while q:
    q -= 1
    l, r, k = map(int, input().split())
    print(calc_within_bounds(l, r, k))
