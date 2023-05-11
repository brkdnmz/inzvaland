def solve(n: int):
    phi = n
    d = 1
    while (d+1)**2 <= n:
        d += 1
        if n % d:
            continue
        while n % d == 0:
            n //= d
        phi //= d
        phi *= d-1
    if n> 1:
        phi //= n
        phi *= n-1
    return phi


print(solve(int(input())))
