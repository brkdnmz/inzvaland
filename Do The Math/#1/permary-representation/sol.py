def solve():
    n = int(input())
    p = list(map(int, input().split()))
    number = 1
    factorial_rep = []

    def fac(x):
        res = 1
        for i in range(x):
            res *= i + 1
        return res

    for i in range(n):
        cnt_smaller = 0
        for j in range(i + 1, n):
            cnt_smaller += p[j] < p[i]
        if i + 1 < n:
            factorial_rep.append(cnt_smaller)
        number += cnt_smaller * fac(n - 1 - i)
    print(number)
    for x in factorial_rep:
        print(x, end=" ")


solve()
