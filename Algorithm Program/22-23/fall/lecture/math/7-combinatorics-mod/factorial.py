# https://ideone.com/rskzqd
from random import randint
from sys import setrecursionlimit

setrecursionlimit(10**6)

MOD = 10**9 + 7


def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
        res %= MOD
    return res


def factorial_recursive(n: int) -> int:
    if not n:
        return 1
    return n * factorial_recursive(n - 1) % MOD


def print_factorials(bound: int) -> int:
    n_examples = 10
    for i in range(n_examples):
        n = randint(0, bound)
        print(f"{n}!:")
        print(f"{factorial(n)} (iterative)")
        print(f"{factorial_recursive(n)} (recursive)")


bound = 10**5
print_factorials(bound)
