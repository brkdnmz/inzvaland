p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

max_ans = 0
targets = []

LIMIT = 10**12


def f(num, p_i, ans):
    global targets, max_ans
    if ans > max_ans:
        max_ans = ans
        targets = [num]
    elif ans == max_ans:
        targets.append(num)
    if p_i == len(p):
        return
    pw = 1
    while num * p[p_i] ** pw <= LIMIT:
        f(num * p[p_i] ** pw, p_i + 1, ans * ((pw + 1) ** 3 - pw**3))
        pw += 1


f(1, 0, 1)
print(targets)
