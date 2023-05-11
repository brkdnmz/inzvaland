from math import gcd

a, b = map(int, input().split())
print(max(a, b) // gcd(a, b))
