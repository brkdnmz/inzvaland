def fast_exp(a, b, m):
    a %= m
    result = 1
    while b:
        if b % 2:
            result = result * a % m
        b //= 2
        a = a * a % m
    return result


a = 123456789101112
b = 10**18
m = 10**9 + 7

print(fast_exp(a, b, m))
print(pow(a, b, m))  # Built-in fast exponentiation!
