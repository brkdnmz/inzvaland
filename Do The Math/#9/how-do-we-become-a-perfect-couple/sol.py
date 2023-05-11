def solve(n: int):
    d = 1
    mask = 1
    init_n = n
    while (d + 1) ** 2 <= n:
        d += 1
        if n % d:
            continue
        in_mask = False
        while n % d == 0:
            n //= d
            in_mask ^= 1
        if in_mask:
            mask *= d
    if n > 1:
        mask *= n
    ans = int((init_n // mask) ** 0.5)
    return ans


print(solve(int(input())))
