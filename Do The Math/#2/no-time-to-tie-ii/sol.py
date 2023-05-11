MOD = 10**9 + 7
C = [[0]*5005 for _ in range(5005)]
for i in range(5005):
    for j in range(i+1):
        if j == 0:
            C[i][j] = 1
        elif i == 0:
            C[i][j] = 0
        else:
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

b = int(input())
for x in range(1, b+1):
    # x buttons, b places
    # b-x available empty spots
    if b-x >= x-1:
        # place x-1 empty spots between buttons
        # then distribute remaining b-2x+1 empty spots among x+1 places (leftmost & rightmost included) asdsad sad sad asd as
        print(C[b-x+1][x], end=" ")
    else:
        # place b-x empty spots between buttons
        # no empty spot will be left
        print(C[x-1][b-x], end=" ")
