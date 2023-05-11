p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


# LIMIT = 10**12


def numbers_with_max_n_divisors(limit: int) -> "list[int]":
    max_cnt = 0
    targets: list[int] = []

    def helper(num: int, p_i: int, cnt: int) -> None:
        nonlocal targets, max_cnt, limit
        if cnt > max_cnt:
            max_cnt = cnt
            targets = [num]
        elif cnt == max_cnt:
            targets.append(num)
        if p_i == len(p):
            return
        pw = 1
        while num * p[p_i] ** pw <= limit:
            helper(num * p[p_i] ** pw, p_i + 1, cnt * (pw + 1))
            pw += 1

    helper(1, 0, 1)

    return targets
