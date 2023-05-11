def solve(n: int):
    factorization = []
    for i in range(2, n + 1):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            factorization.append(i)
    if n > 1:
        factorization.append(n)
    return factorization


factorization = solve(int(input()))
print(" ".join(str(x) for x in factorization))
