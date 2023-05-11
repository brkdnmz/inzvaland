# https://ideone.com/0Cj8MK
n = 123456
positive_divisors = []
for i in range(1, n + 1):
    if n % i:  # r > 0
        continue
    # i is a divisor!
    positive_divisors.append(i)

n_positive_divisors = len(positive_divisors)
print(f"n: {n}")
print(f"Number of positive divisors: {n_positive_divisors}")
print(f"Number of all divisors: {2*n_positive_divisors}")
print("Positive divisors:")
print(" ".join(map(str, positive_divisors)))
