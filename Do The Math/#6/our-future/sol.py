def solve(h1: int, h2: int) -> int:
    smaller, larger = h1, h2
    if smaller > larger:
        smaller, larger = larger, smaller
    ans = (larger - smaller) // 2
    same_sum_products = []  # i * (h1 + h2 - i) for i <= h1
    for i in range(1, smaller + 1):
        j = h1 + h2 - i
        same_sum_products.append(i * j)
    product = h1 * h2
    same_product_sums = []
    for i in range(1, product + 1):
        if i * i > product:
            break
        if product % i:
            continue
        same_product_sums.append(i + product // i)
    ans += len(set([*same_product_sums, *same_sum_products]))
    return ans


# while True:
#     h1 = randint(1, 10**5)
#     h2 = randint(1, 10**5)
#     print(h1, h2)
#     solve(h1, h2)


h1, h2 = map(int, input().split())
print(solve(h1, h2))
