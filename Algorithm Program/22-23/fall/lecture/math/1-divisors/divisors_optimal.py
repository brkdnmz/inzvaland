# https://ideone.com/KPYli3
n = 1234567891011
positive_divisors = []

for i in range(1, n + 1):
    if i**2 > n:  # To break when exceeded sqrt(n)
        break
    if n % i:  # r > 0
        continue

    # i is a divisor!
    positive_divisors.append(i)
    # n/i is another divisor!
    if i != n // i:  # or i*i != n, i**2 != n, ...
        positive_divisors.append(n // i)

n_positive_divisors = len(positive_divisors)
print(f"n: {n}")
print(f"Number of positive divisors: {n_positive_divisors}")
print(f"Number of all divisors: {2*n_positive_divisors}")
print("Positive divisors:")
print(" ".join(map(str, positive_divisors)))
