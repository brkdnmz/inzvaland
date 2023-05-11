t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    lmost, rmost, umost, dmost = m, 0, n, 0
    for i in range(n):
        row = input()
        for j in range(m):
            if row[j] == ".":
                continue
            lmost = min(lmost, j)
            rmost = max(rmost, j)
            umost = min(umost, i)
            dmost = max(dmost, i)
    ans = 0
    if lmost < m:
        ans = (lmost + 1) * (m - rmost) * (umost + 1) * (n - dmost)
    print(ans)
