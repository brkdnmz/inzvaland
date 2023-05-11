def solve(n: int):
    ans = 1
    for i in range(2, n + 1):
        if i * i > n:
            break
        exp = 0
        while n % i == 0:
            n //= i
            exp += 1
        ans *= 2 * exp + 1
    if n > 1:
        ans *= 3
    return ans


print(solve(int(input())))
