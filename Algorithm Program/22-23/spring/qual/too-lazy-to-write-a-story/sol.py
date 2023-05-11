def solve(n: int, a: "list[int]"):
    ans = 0
    sorted_a = sorted([(a[i], i) for i in range(n)])
    for i in range(1, n):
        ans += abs(sorted_a[i][1] - sorted_a[i - 1][1])

    print(ans)


n = int(input())
a = list(map(int, input().split()))

solve(n, a)
