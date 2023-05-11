# https://ideone.com/GQYCm3
def binary_exponentiation(base: int, exponent: int, mod: int, take_exponent_mod=False) -> int:
    result = 1
    while exponent:
        if exponent & 1:  # or exponent % 2
            result = result * base % mod
        exponent >>= 1  # or exponent /= 2
        base = base * base % mod
    return result


base = 10**18
exponent = 10**18
mod = 10**9 + 7

print(f"{base}^{exponent} modulo {mod}: {binary_exponentiation(base, exponent, mod)}")
print(
    f"{base}^{exponent % mod} modulo {mod} (took exponent mod m): {binary_exponentiation(base, exponent, mod, take_exponent_mod=True)}"
)

# Python has built-in binary exponentiation: pow(base, exponent, mod)!
print(f"{base}^{exponent} modulo {mod} (built-in): {pow(base, exponent, mod)}")
