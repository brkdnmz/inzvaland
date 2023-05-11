mx_divisors = 0
mx_num = 0
A = 10**14
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def f(num, p_index, prev_pow, cnt):
  if p_index >= len(primes):
    return
  global mx_divisors, mx_num
  cur = primes[p_index]
  for i in range(1, prev_pow+1):
    if num * cur <= A:
      if mx_divisors < cnt * (i+1):
        mx_divisors = cnt * (i+1)
        mx_num = num
      elif mx_divisors == cnt * (i+1):
        mx_num = max(mx_num, num)
      f(num*cur, p_index+1, i, cnt * (i+1))
    cur *= primes[p_index]


f(1, 0, 10000, 1)
print(mx_num, mx_divisors)
# 3373164194400 17280
