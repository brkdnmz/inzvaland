h, m = map(int, input().split())
n = 60 * h + m

for d in range(1, n + 1):
    if d * d > n:
        break
    if n % d:
        continue
    if (d + 1) % 60 == 0 or (n // d + 1) % 60 == 0:
        print("YES")
        exit()
print("NO")
