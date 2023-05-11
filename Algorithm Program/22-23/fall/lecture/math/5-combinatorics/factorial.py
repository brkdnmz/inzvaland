# https://ideone.com/sGIb7X
def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def factorial_recursive(n: int) -> int:
    if not n:
        return 1
    return n * factorial_recursive(n - 1)


def print_factorials(n: int) -> int:
    for i in range(n + 1):
        print(f"{i}!:", end="")
        if i < 10:
            print("\t", end="")
        print(" ", end="")

        print(f"{factorial(i)} (iterative), {factorial_recursive(i)} (recursive)")


n = 25
print_factorials(n)
