N = 10**7
P = 10**7
MOD = 10**9 + 7
lpf = [0] * (P + 1)

q = int(input())

for i in range(2, P + 1):
    if lpf[i]:
        continue
    for k in range(i, P + 1, i):
        lpf[k] = i

pre = [1]
f = 1
for i in range(1, N + 1):
    f *= i
    f %= MOD
    pre.append(pre[-1] * f)
    pre[-1] %= MOD


def get_trailing_zeros_up_to(x: int, k: int):
    p = lpf[k]
    pw = p
    exp = 1
    cnt = 0
    while pw <= x:
        m = x // pw - 1
        # 1 1 1 ... 2 2 2 ... m m m
        # each pw times
        cnt += m * (m + 1) // 2 * pw
        cnt += (x - (m + 1) * pw + 1) * (m + 1)
        pw *= p
        exp += 1
    return cnt


while q:
    q -= 1
    l, r, k = map(int, input().split())

    ans = pre[r] * pow(pow(k, get_trailing_zeros_up_to(r, k), MOD), MOD - 2, MOD)
    div = (
        pre[l - 1]
        * pow(pow(k, get_trailing_zeros_up_to(l - 1, k), MOD), MOD - 2, MOD)
        % MOD
    )
    ans *= pow(div, MOD - 2, MOD)
    ans %= MOD

    print(ans)
