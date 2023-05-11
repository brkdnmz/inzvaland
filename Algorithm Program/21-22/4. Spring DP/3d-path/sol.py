def solve(n, food):
    dp = [[[-10**9]*(n+1) for i in range(n+1)] for i in range(n+1)]
    next_move = [[[3]*(n+1) for i in range(n+1)] for i in range(n+1)]
    dp[n][n][n] = food[n][n][n]
    choices = [
        [0, 0, -1],
        [-1, 0, 0],
        [0, -1, 0],
    ]
    moves = ["F", "R", "U"]
    for c in range(n, 0, -1):
        for r in range(n, 0, -1):
            for d in range(n, 0, -1):
                for i, ch in enumerate(choices):
                    nc = c + ch[0]
                    nr = r + ch[1]
                    nd = d + ch[2]
                    new_val = dp[c][r][d] + food[nc][nr][nd]
                    if dp[nc][nr][nd] <= new_val:
                        if dp[nc][nr][nd] == new_val and next_move[nc][nr][nd] > i:
                            next_move[nc][nr][nd] = i
                        elif dp[nc][nr][nd] < new_val:
                            dp[nc][nr][nd] = new_val
                            next_move[nc][nr][nd] = i

    path = ""
    cur = [1, 1, 1]
    while next_move[cur[0]][cur[1]][cur[2]] <= 2:
        path += moves[next_move[cur[0]][cur[1]][cur[2]]]
        sub = choices[next_move[cur[0]][cur[1]][cur[2]]]
        cur[0] -= sub[0]
        cur[1] -= sub[1]
        cur[2] -= sub[2]
    return dp[1][1][1], path


n = int(input())
food = [[[0]*(n+1) for i in range(n+1)] for i in range(n+1)]
for depth in range(n):
    for row in range(n):
        line = list(map(int, input().split()))
        for col in range(n):
            food[col+1][row+1][depth+1] = line[col]
ans, path = solve(n, food)
print(ans)
print(path)
