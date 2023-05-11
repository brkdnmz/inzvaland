t = int(input())

while t:
    t -= 1
    a, b = map(int, input().split())
    sum = a+b

    div = 0
    ans = 0
    while (div+1)**2 <= sum:
        div += 1
        if sum % div:
            continue
        ans += 1 + (div <= b)
        if div**2 != sum:
            ans += 1 + (sum//div <= b)
    print(ans)
