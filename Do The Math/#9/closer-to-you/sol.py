def solve(n: int):
    ans = n
    for i in range(2, n + 1):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            ans += n
    if n > 1:
        ans += 1
    return ans


print(solve(int(input())))
