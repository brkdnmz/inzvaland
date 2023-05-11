MOD = 10**9 + 7


def solve(n: int, m: int, grid):
    number_of_ways = [[0] * (m + 1) for _ in range(n + 1)]
    number_of_ways[1][1] = 1 if grid[0][0] == "." else 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                continue
            number_of_ways[i + 1][j + 1] += number_of_ways[i][j + 1]
            number_of_ways[i + 1][j + 1] += number_of_ways[i + 1][j]
            number_of_ways[i + 1][j + 1] %= MOD
    return number_of_ways[n][m]


read = lambda: list(map(int, input().split()))

n, m = read()
grid = []
for i in range(n):
    grid.append(input())

print(list(grid[0]))
print(len(grid), len(grid[0]))

print(solve(n, m, grid))
