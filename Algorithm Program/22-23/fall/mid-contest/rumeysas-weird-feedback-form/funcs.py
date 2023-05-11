from random import randint, shuffle

from numba import int64, njit
from numba.experimental import jitclass


@njit
def is_prime(num: int) -> bool:
    for i in range(2, num + 1):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


# @jitclass([("n", int64), ("low", int64), ("high", int64), ("n_high", int64)])
class Generator:
    def __init__(self, n: int, low: int, high: int, n_high: int) -> None:
        self.n = n
        self.low = low
        self.high = high
        self.n_high = min(n, n_high)

    def next_prime(self, num: int) -> int:
        num += 1
        while not is_prime(num):
            num += 1
        return num

    def prev_prime(self, num: int) -> int:
        num -= 1
        while not is_prime(num):
            num -= 1
        return num

    def max_distinct_primes(self) -> "list[int]":
        a: list[int] = []
        cur_prime = 2
        cnt_high = 0
        for _ in range(self.n):
            cur_number = 1
            while cur_number * cur_prime <= (self.high if cnt_high < self.n_high else self.low):
                cur_number *= cur_prime
                cur_prime = self.next_prime(cur_prime)
            small_prime = 2
            while cur_number * small_prime <= (self.high if cnt_high < self.n_high else self.low):
                cur_number *= small_prime
                small_prime = self.next_prime(small_prime)
            cnt_high = min(cnt_high + 1, self.n_high)
            a.append(cur_number)
        return self.prepared(a)

    def only_biggest_prime(self) -> "list[int]":
        biggest_prime_low = self.prev_prime(self.low + 1)
        biggest_prime_high = self.prev_prime(self.high + 1)
        a = [biggest_prime_low for _ in range(self.n)]
        for i in range(self.n_high):
            a[i] = biggest_prime_high

        return self.prepared(a)

    def random_big_primes(self, n_distinct: int) -> "list[int]":
        cur_prime = self.prev_prime(self.high + 1)
        primes = []
        for _ in range(min(self.n_high, n_distinct)):
            primes.append(cur_prime)
            cur_prime = self.prev_prime(cur_prime)
        a = [primes[randint(0, len(primes) - 1)] for _ in range(self.n_high)]
        primes.clear()
        cur_prime = self.prev_prime(self.low + 1)
        for _ in range(min(self.n_high, n_distinct)):
            primes.append(cur_prime)
            cur_prime = self.prev_prime(cur_prime)
        a += [primes[randint(0, len(primes) - 1)] for _ in range(self.n - self.n_high)]

        return self.prepared(a)

    def two_times_biggest_prime(self):
        biggest_prime_high = self.prev_prime(self.high // 2)
        a = [2 * biggest_prime_high for _ in range(self.n_high)]
        biggest_prime_low = self.prev_prime(self.low // 2)
        a += [2 * biggest_prime_low for _ in range(self.n - self.n_high)]

        return self.prepared(a)

    def closest_two_biggest_primes(self):
        smaller_high = self.prev_prime(int(self.high**0.5))
        larger_high = self.next_prime(smaller_high)
        while smaller_high * larger_high > self.high:
            smaller_high = self.prev_prime(smaller_high)
        assert smaller_high * larger_high <= self.high
        a = [smaller_high * larger_high for _ in range(self.n_high)]
        smaller_low = self.prev_prime(int(self.low**0.5))
        larger_low = self.next_prime(smaller_low)
        while smaller_low * larger_low > self.low:
            smaller_low = self.prev_prime(smaller_low)
        assert smaller_low * larger_low <= self.low
        a += [smaller_low * larger_low for _ in range(self.n - self.n_high)]

        return self.prepared(a)

    def min_case(self):
        return self.prepared([1 for _ in range(self.n)])

    def max_case(self):
        a = [self.high for _ in range(self.n_high)]
        a += [self.low for _ in range(self.n - self.n_high)]

        return self.prepared(a)

    def max_exponent(self):
        pw2_low = 1
        pw2_high = 1
        while pw2_high * 2 <= self.high:
            pw2_high *= 2
        while pw2_low * 2 <= self.low:
            pw2_low *= 2
        a = [pw2_high for _ in range(self.n_high)]
        a += [pw2_low for _ in range(self.n - self.n_high)]
        return self.prepared(a)

    def random(self):
        a = [randint(1, self.high) for _ in range(self.n_high)]
        a += [randint(1, self.low) for _ in range(self.n - self.n_high)]
        return self.prepared(a)

    def several_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17]
        a = []
        for _ in range(self.n_high):
            num = 1
            idx = randint(0, len(primes) - 1)
            while num * primes[idx] <= self.high:
                num *= primes[idx]
                idx = randint(0, len(primes) - 1)
            a.append(num)
        for _ in range(self.n - self.n_high):
            num = 1
            idx = randint(0, len(primes) - 1)
            while num * primes[idx] <= self.low:
                num *= primes[idx]
                idx = randint(0, len(primes) - 1)
            a.append(num)

        return self.prepared(a)

    def generate_all(self) -> "list[list[int]]":
        all = []
        all.append(self.max_distinct_primes())
        print("max_distinct_primes done")
        all.append(self.only_biggest_prime())
        print("only_biggest_prime done")
        all.append(self.random_big_primes(200))
        print("random_big_primes done")
        all.append(self.two_times_biggest_prime())
        print("two_times_biggest_prime done")
        all.append(self.closest_two_biggest_primes())
        print("closest_two_biggest_primes done")
        all.append(self.min_case())
        print("min_case done")
        all.append(self.max_case())
        print("max_case done")
        all.append(self.max_exponent())
        print("max_exponent done")
        all.append(self.random())
        print("random done")
        all.append(self.several_primes())
        print("several_primes done")
        return all

    def prepared(self, a: "list[int]") -> "list[int]":
        shuffle(a)
        self.validate(a)
        return a

    def validate(self, a: "list[int]") -> None:
        cnt_high = 0
        assert len(a) == self.n
        for i in range(len(a)):
            if cnt_high == self.n_high:
                assert a[i] <= self.low
            cnt_high += a[i] > self.low
            assert cnt_high <= self.n_high
            assert a[i] <= self.high
