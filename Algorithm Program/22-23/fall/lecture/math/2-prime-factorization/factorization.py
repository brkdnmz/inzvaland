# https://ideone.com/uZvoXM
class Divisor:
    def __init__(self, prime: int, exponent: int) -> None:
        self.prime = prime
        self.exponent = exponent

    def __str__(self):
        return f"{self.prime}^{self.exponent}"


n = 10512969114312
initial_n = n
divisors: "list[Divisor]" = []

for i in range(2, n + 1):
    if i**2 > n:  # To break when exceeded sqrt(n)
        break
    if n % i:  # r > 0
        continue

    d = Divisor(i, 0)
    while n % i == 0:
        n //= i
        d.exponent += 1
    divisors.append(d)

if n > 1:
    divisors.append(Divisor(n, 1))

print(f"n = {initial_n} = {' * '.join(map(str, divisors))}")
