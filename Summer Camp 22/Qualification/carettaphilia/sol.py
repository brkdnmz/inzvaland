import numba
N = 10**6
is_prime_power = [True] * (N+5)
fac = [0] * (N+5)
inv_fac = [0] * (N+5)
mod = 10**9 + 7


def precalc(is_prime_power, fac, inv_fac):
  for i in range(2, N+5):
    if not is_prime_power[i]:
      continue
    for j in range(i*i, N+5, i):
      is_prime_power[j] = False
    j = i
    while j*i <= N+5:
      j *= i
      is_prime_power[j] = True

  def pow(n, e, mod):
    res = 1
    pw = n
    while e:
      if e & 1:
        res = res * pw % mod
      e >>= 1
      pw = pw * pw % mod
    return res
  fac[0] = 1
  for i in range(1, N+5):
    fac[i] = i * fac[i-1] % mod
  inv_fac[N] = pow(fac[N], mod-2, mod)
  for i in range(N-1, -1, -1):
    inv_fac[i] = inv_fac[i+1] * (i+1) % mod


precalc(is_prime_power, fac, inv_fac)


def solve(n, m):
  def C(n, k):
    return (fac[n] * inv_fac[k] % mod) * inv_fac[n-k] % mod
  ans = 0
  for i in range(3, m+1):
    if not is_prime_power[i] or i % 2 == 0:
      continue
    ans = (ans + C(m, i)) % mod
  return ans


n, m = map(int, input().split())

print(solve(n, m))
