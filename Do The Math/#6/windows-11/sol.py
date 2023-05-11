n = int(input())

# n(n+2)
# (n+1)^2
answers: "list[int]" = []
for i in range(1, n * (n + 2)):
    if i * i > n * (n + 2):
        break
    if n * (n + 2) % i:
        continue
    answers.append(i)
    answers.append(n * (n + 2) // i)

for i in range(1, n + 1 + 1):
    if (n + 1) ** 2 % i:
        continue
    if i != 1:
        answers.append(i)
    if i != n + 1:
        answers.append((n + 1) ** 2 // i)

answers.sort()
file = open("ans", "w")
file.write(" ".join([str(x) for x in answers]))
print(" ".join([str(x) for x in answers]))
