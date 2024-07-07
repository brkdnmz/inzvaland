from bisect import bisect_right

mod = 10**9 + 7


def generate(armutlar, secimler, i=0, mask=0, toplam=0):
    if i == len(armutlar):
        secimler.append([mask, toplam])
        return
    generate(armutlar, secimler, i + 1, mask, toplam)
    if not i or not (mask >> (i - 1) & 1):
        generate(armutlar, secimler, i + 1, mask | (1 << i), (toplam + armutlar[i]) % mod)


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    l, r = [], []
    for i in range(n):
        if i < n // 2:
            l.append(a[i])
        else:
            r.append(a[i])

    lchoices, rchoices = [], []
    generate(l, lchoices)
    generate(r, rchoices)

    lsize = n // 2
    rsize = n - n // 2
    rsums = [[[], []], [[], []]]
    for mask, summ in rchoices:
        l_taken = rsize and (mask >> (rsize - 1) & 1)
        r_taken = mask & 1
        rsums[l_taken][r_taken].append(summ)
    for i in [0, 1]:
        for j in [0, 1]:
            rsums[i][j].sort()

    max_ans = 0
    for mask, summ in lchoices:
        l_taken = lsize and (mask >> (lsize - 1) & 1)
        r_taken = mask & 1

        for i in range(0, (not r_taken) + 1):
            for j in range(0, (not l_taken) + 1):
                target_sums = rsums[i][j]
                it = bisect_right(target_sums, mod - 1 - summ)
                if it:
                    max_ans = max(max_ans, summ + target_sums[it - 1])
    return max_ans


if __name__ == "__main__":
    ans = solve()
    print(ans)
