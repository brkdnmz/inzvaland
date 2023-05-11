def is_p(n):
  i = 1
  while (i+1)**2 <= n:
    i += 1
    if n % i == 0:
      return False
  return True


mxs = []
mx_is = []
for d in range(1, 12):
  mx = 0
  mx_i = 0
  for i in range(10**5, 10**5 - 1000, -1):
    cur = 1
    vis = [0] * i
    while not vis[cur]:
      vis[cur] = 1
      cur = cur * d % i
    if mx < sum(vis):
      mx = sum(vis)
      mx_i = i
  mxs.append(mx)
  mx_is.append(mx_i)
print(mxs, mx_is)
