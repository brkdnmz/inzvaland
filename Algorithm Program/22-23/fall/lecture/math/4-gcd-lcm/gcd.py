# https://ideone.com/U43wXa
from math import gcd


def gcd_iterative(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    while b:
        a %= b
        a, b = b, a

    return a

def gcd_recursive(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    if not b:
        return a

    return gcd_recursive(a%b, b)

def gcd_recursive_alt(a: int, b: int) -> int:
    if not a:
        return b

    return gcd_recursive_alt(b%a, a)

a = 152348643862835682
b = 4236438563286243

print(f"GCD (iterative):\t{gcd_iterative(a, b)}")
print(f"GCD (recursive):\t{gcd_recursive(a, b)}")
print(f"GCD (recursive v2):\t{gcd_recursive_alt(a, b)}")
print(f"GCD (built-in):\t\t{gcd(a, b)}")
