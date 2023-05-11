n = int(input())
p = [0 for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    p[x - 1] = y - 1
ans = n**2
for i in range(n):
    vis = [0 for _ in range(n)]
    cur = i
    while not vis[cur]:
        ans -= 1
        vis[cur] = 1
        cur = p[cur]
print(ans)
