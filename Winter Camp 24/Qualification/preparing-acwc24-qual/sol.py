n = int(input())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = 0
for i in range(1, 1 << n):
    setters, testers = [], []
    for j in range(n):
        if i & (1 << j):
            setters.append(p[j])
        else:
            testers.append(t[j])
        testers.append(t[j])
    setters.sort(reverse=True)
    testers.sort(reverse=True)
    cur = 0
    for j, S in enumerate(setters):
        cur += (S + testers[j]) * testers[j]
    ans = max(ans, cur)

print(ans)
