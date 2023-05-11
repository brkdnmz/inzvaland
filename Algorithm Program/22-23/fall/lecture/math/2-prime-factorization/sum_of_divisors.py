# https://ideone.com/hsETTx
n = 10512969114312


def calc_geometric_sum(prime: int, exponent: int) -> int:
    return (prime ** (exponent + 1) - 1) // (prime - 1)


def calc_divisors_sum_without_formula(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        # i * i is faster than i**2. I first realized while testing this code!
        if i * i > n:
            break
        if n % i:
            continue
        sum += i
        if i * i != n:
            sum += n // i
    return sum


def calc_divisors_sum_with_formula(n: int) -> int:
    sum = 1
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        exponent = 0
        while n % i == 0:
            n /= i
            exponent += 1
        sum *= calc_geometric_sum(i, exponent)
    if n > 1:
        sum *= calc_geometric_sum(n, 1)
    return sum


print("n =", n)
print("Sum of divisors w/ formula\t=", calc_divisors_sum_with_formula(n))
print("Sum of divisors w/o formula\t=", calc_divisors_sum_without_formula(n))
