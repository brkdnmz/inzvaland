# Or use the built-in gcd!
def gcd(a: int, b: int):
    if not a:
        return b
    return gcd(b % a, a)


q = int(input())
while q:
    q -= 1
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
