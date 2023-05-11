p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

max_cnt = 0
targets = []

LIMIT = 10**12


def f(num, p_i, cnt):
    global targets, max_cnt
    if cnt > max_cnt:
        max_cnt = cnt
        targets = [num]
    elif cnt == max_cnt:
        targets.append(num)
    if p_i == len(p):
        return
    pw = 1
    while num * p[p_i]**pw <= LIMIT:
        f(num * p[p_i]**pw, p_i + 1, cnt * (pw + 1))
        pw += 1


f(1, 0, 1)
print(targets)
