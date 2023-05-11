# Or use the built-in gcd!
def gcd(a: int, b: int):
    if not a:
        return b
    return gcd(b % a, a)


n = int(input())
a = list(map(int, input().split()))

ans = 0
for x in a:
    ans = gcd(ans, x)

print(ans)
