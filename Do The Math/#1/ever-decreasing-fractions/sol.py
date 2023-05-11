t = int(input())

while t:
    t -= 1
    a, b = map(int, input().split())
    cnt = 0
    for i in range(b, abs(a-b) + 1):
        cnt += (a-b) % i == 0
    if a == b:
        cnt = -1
    print(cnt)
