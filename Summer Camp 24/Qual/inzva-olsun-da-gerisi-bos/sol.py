from math import log2

s = input().strip()
n = len(s)
size = int(log2(n))
if 2**size != n:
    size += 1
length = 2**size
tree = [0] * (length * 2)

a, b = 0, 0
letter = {}
for i in range(97, 123):
    letter[chr(i)] = 0
while b < n and (
    (letter["a"] < 3)
    or (letter["b"] < 1)
    or (letter["d"] < 1)
    or (letter["e"] < 1)
    or (letter["g"] < 1)
    or (letter["i"] < 3)
    or (letter["k"] < 1)
    or (letter["l"] < 2)
    or (letter["n"] < 2)
    or (letter["o"] < 2)
    or (letter["p"] < 1)
    or (letter["r"] < 1)
    or (letter["s"] < 3)
    or (letter["u"] < 1)
    or (letter["v"] < 1)
    or (letter["z"] < 1)
):
    letter[s[b]] += 1
    b += 1
val = {
    "a": 3,
    "b": 1,
    "d": 1,
    "e": 1,
    "g": 1,
    "i": 3,
    "k": 1,
    "l": 2,
    "n": 2,
    "o": 2,
    "p": 1,
    "r": 1,
    "s": 3,
    "u": 1,
    "v": 1,
    "z": 1,
}
# inzvaolsundagerisiboskalp
count = 2**size
tree[count] = b
count += 1
a += 1
last = {
    "a": -1,
    "b": -1,
    "d": -1,
    "e": -1,
    "g": -1,
    "i": -1,
    "k": -1,
    "l": -1,
    "n": -1,
    "o": -1,
    "p": -1,
    "r": -1,
    "s": -1,
    "u": -1,
    "v": -1,
    "z": -1,
}
nextt = {}
pre = {}
while a < n:
    if s[a - 1] not in last:
        tree[count] = b - a
        count += 1
        a += 1
    else:
        if last[s[a - 1]] != -1:
            nextt[last[s[a - 1]]] = a - 1
        pre[a - 1] = last[s[a - 1]]
        nextt[a - 1] = -1
        last[s[a - 1]] = a - 1

        char = s[a - 1]
        letter[char] -= 1
        v = val[char]
        while b < n and letter[char] < v:
            letter[s[b]] += 1
            b += 1

        tree[count] = b - a
        count += 1
        a += 1

if s[a - 1] in last:
    if last[s[a - 1]] != -1:
        nextt[last[s[a - 1]]] = a - 1
    pre[a - 1] = last[s[a - 1]]
    nextt[a - 1] = -1
    last[s[a - 1]] = a - 1

for i in range(length * 2 - 1, 1, -2):
    tree[i // 2] = tree[i] + tree[i - 1]
# print(tree[length:])
# print(tree)
# print(pre)
# print()
# print(nextt)

for _ in range(int(input())):
    d = input().split()
    if d[0] == "1":
        a = int(d[1]) - 1
        # print(s[a-4:a+5])
        if a not in pre:
            continue
        check = a
        for i in range(val[s[a]]):
            bup = check
            check = pre[check]
            # print(check)
            target = a
            for _ in range(val[s[a]] - i):
                target = nextt[target]
                if target == -1:
                    break
            if target == -1:
                target = n
            else:
                target += 1
            for j in range(check + 1, bup + 1):
                if target > j + tree[length + j]:
                    start = length + j
                    v = target - j - tree[length + j]
                    tree[start] += v
                    while start > 1:
                        tree[start // 2] += v
                        start //= 2
                else:
                    break
            if check == -1:
                break
        pre[nextt[a]] = pre[a]
        nextt[pre[a]] = nextt[a]
        del pre[a]
        # print(tree[length:])

        # target = nextt[check]+1
        # if target == -1:
        #     target = n+1
        # for i in range(check+1, a+1):
        #     if target > i + tree[length+i]:
        #         start = length + i
        #         v = target-i-tree[length+i]
        #         tree[start] += v
        #         while start > 1:
        #             tree[start//2] += v
        #             start //= 2
        # pre[nextt[a]] = pre[a]
        # nextt[pre[a]] = nextt[a]
        # del pre[a]
        # print(tree[length:])
    else:
        ans = 0
        left = length + int(d[1]) - 1
        right = length + int(d[2])
        while left < right:
            if left % 2 == 1:
                ans += tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                ans += tree[right]
            left //= 2
            right //= 2
        print(ans)
