l, r = map(int, input().split())
ans = [0] * 15
for j in range(l, r+1):
    for div in range(1, 17):
        if (j-1) % div:
            break
        if div >= 2:
            ans[div-2] += 1
for x in ans:
    print(x, end=" ")
