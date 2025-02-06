n, q = map(int, input().split())

a = list(map(int, input().split()))

mn, mx = min(a), max(a)

nearest = [-(10**9), -(10**9)]
ans = [0] * n
for i, x in enumerate(a):
    side = x - mn > mx - x
    ans[i] = nearest[side]
    if 2 * x == mn + mx:
        ans[i] = max(ans[i], nearest[not side])
    nearest[x == mn] = i

nearest = [10**9, 10**9]

for i in range(n - 1, -1, -1):
    side = a[i] - mn > mx - a[i]
    maybe = nearest[side]
    if i - ans[i] > maybe - i or (
        i - ans[i] == maybe - i and a[i] - a[ans[i]] > a[maybe] - a[i]
    ):
        ans[i] = maybe
    if 2 * a[i] == mn + mx:
        maybe = nearest[not side]
        if i - ans[i] > maybe - i or (
            i - ans[i] == maybe - i and a[i] - a[ans[i]] > a[maybe] - a[i]
        ):
            ans[i] = maybe
    nearest[x == mn] = i

while q:
    q -= 1
    g = int(input())
    print(ans[g - 1] + 1)
