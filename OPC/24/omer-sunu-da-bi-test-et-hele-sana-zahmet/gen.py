import subprocess

testcases = [
    (10**5, 10**3),
    (10**6, 10**2),
    (10**7, 10**1),
    (10**8, 10**0),
    (10**4 // 2, 10**4 * 2),
    (10**4 // 3, 10**4 * 3),
    (10**4 // 4, 10**4 * 4),
    (10**4 // 5, 10**4 * 5),
    (10**4 // 6, 10**4 * 6),
    (10**4 // 7, 10**4 * 7),
    (10**4 // 8, 10**4 * 8),
    (10**4 // 9, 10**4 * 9),
]

# for n, m in testcases:
#     p = subprocess.run(
#         ["./a.exe"], input=f"{n} {m}", stdout=subprocess.PIPE, encoding="ascii"
#     )
#     print(n, m, p.stdout)

for n in range(10**4 - 100, 10**4 + 1):
    m = 10**8 // n
    p = subprocess.run(
        ["./a.exe"], input=f"{n} {m}", stdout=subprocess.PIPE, encoding="ascii"
    )
    print(n, m, p.stdout)
