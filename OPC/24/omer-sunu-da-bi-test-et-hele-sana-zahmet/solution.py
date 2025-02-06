from math import gcd


def brute_force(n: int, m: int):
    ans = 0
    for left in range(1, n):
        for top in range(1, m):
            g = gcd(top, left)
            i = left + top // g
            j = top + left // g
            cnt = 0
            while i <= n and j <= m:
                cnt += max(i - left, top) % min(i - left, top) == 0
                i += top // g
                j += left // g
            ans += cnt
    return ans


def unoptimized(n: int, m: int):
    ans = 0
    n_squares = 0
    for a in range(1, n):
        for b in range(1, m):
            a1 = (n - a) // b
            a2 = (m - b) // a
            ans += min(a1, a2)
            n_squares += min(a1, a2) > 0
    return ans * 2 - n_squares


def fast(n: int, m: int):
    ans = 0
    n_squares = 0
    for a in range(1, n):
        n_squares += max(0, min(n, m) - a)

        def f(b: int):
            return b**2 - m * b - a**2 + n * a

        # min((n - a) / b, (m - b) / a)
        # (n - a) / b = (m - b) / a
        # na - a^2 = mb - b^2
        # b^2 - a^2 = mb - na
        # b^2 - mb - a^2 + na = 0
        midpoint = m // 2
        l, r = 1, midpoint + 1
        while l < r:
            mid = (l + r) // 2
            if f(mid) > 0:
                l = mid + 1
            else:
                r = mid
        first_bound = l
        l, r = midpoint, m
        while l < r:
            mid = (l + r + 1) // 2
            if f(mid) < 0:
                l = mid
            else:
                r = mid - 1
        second_bound = l

        bounds = [0]
        for x in range(1, n - a + 1):
            if x * x > n - a:
                break
            bounds.append(x)
            if x != (n - a) // x:
                bounds.append((n - a) // x)
        bounds.sort()

        def floors_sum(last: int):
            if last <= 0:
                return 0
            # (1 / a) to (last / a)
            last_multiple = last - last % a
            k = (last_multiple - 1) // a
            tot = a * (k * (k + 1) // 2)
            # if last % a:
            tot += (last % a + 1) * (last // a)
            return tot

        # (m - 1) / a to (m - first_bound + 1) / a

        ans += floors_sum(m - 1) - floors_sum(m - first_bound)

        # for b in range(1, first_bound):
        #     assert f(b) >= 0
        #     ans += (m - b) // a

        if first_bound <= second_bound:
            for i, bound in enumerate(bounds):
                if bound < first_bound:
                    continue
                if bound >= second_bound:
                    ans += (
                        (n - a)
                        // bound
                        * (second_bound - max(first_bound, bounds[i - 1] + 1) + 1)
                    )
                    break
                ans += (
                    (n - a) // bound * (bound - max(first_bound, bounds[i - 1] + 1) + 1)
                )
        # for b in range(first_bound, second_bound + 1):
        #     assert f(b) <= 0
        #     ans += (n - a) // b

        ans += floors_sum(m - (second_bound + 1))

        # for b in range(second_bound + 1, m):
        #     assert f(b) >= 0
        #     ans += (m - b) // a

    return ans * 2 - n_squares


n, m = map(int, input().split())

# print(unoptimized(n, m))
print(fast(n, m))
# print(brute_force(n, m))

# a, b -> min()
