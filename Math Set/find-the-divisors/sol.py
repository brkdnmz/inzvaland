def solve(n: int):
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)
    divisors.sort()
    return divisors


divisors = solve(int(input()))
print(len(divisors))
print(" ".join(str(x) for x in divisors))
