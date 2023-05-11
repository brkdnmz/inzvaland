def solve(n: int) -> int:
    ans = n - 1  # exclude 1 right now
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if not is_prime[i]:
            ans -= 1
            continue
        for k in range(i * i, n + 1, i):
            is_prime[k] = False
    return ans


print(solve(int(input())))
