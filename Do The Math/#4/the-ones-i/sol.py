n = int(input())

ans = 1

for i in range(2, n):
    if i**2 > n:
        break
    if n % i:
        continue
    exp = 0
    while n % i == 0:
        n //= i
        exp += 1
    ans *= (exp + 1) ** 3 - exp**3
if n > 1:
    ans *= 2**3 - 1


print(ans)
