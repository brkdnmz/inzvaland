N = 3 * 10**6
S = 10
n_divisors = [0 for _ in range(N + S + 1)]

for i in range(1, N + S + 1):
    n_divisors[i] += n_divisors[i - 1]
    for k in range(i, N + S + 1, i):
        n_divisors[k] += 1


def solve(n: int, s: int) -> int:
    ans = n_divisors[n + s] - n_divisors[n - 1]
    for i in range(1, s + 1):
        ans -= (n + s) // i - (n - 1) // i - 1  # excluding extra counts
    return ans


q = int(input())
while q:
    q -= 1
    n, s = map(int, input().split())
    print(solve(n, s))
