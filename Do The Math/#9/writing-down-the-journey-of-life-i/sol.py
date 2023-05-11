def solve(n: int):
    ans = 0
    for i in range(1, n + 2):
        if i * i > n + 1:
            break
        if (n + 1) % i:
            continue
        ans += 1 + (i * i != n + 1)
    ans -= 1  # n+1 must be excluded, should be less than n horizontal rules
    return ans


print(solve(int(input())))
