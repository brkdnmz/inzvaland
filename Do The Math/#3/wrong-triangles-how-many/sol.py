n = int(input())

ans = 0
for i in range(1, int(n**0.5) + 1):
    if n % i or i**2 == n:
        continue
    ans += i % 2 == (n // i) % 2

print(ans)
