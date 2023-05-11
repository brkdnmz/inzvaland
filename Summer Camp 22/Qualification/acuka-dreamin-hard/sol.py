

n = int(input())
p = [0]*11
m = [0]*11
for i in range(11):
  p[i], m[i] = map(int, input().split())
portions = []
cycle_start = [0] * 11
for i in range(11):
  portions.append([])
  vis = [False] * m[i]
  cur = p[i] % m[i]
  pos_of = [0] * m[i]
  while not vis[cur]:
    pos_of[cur] = len(portions[i])
    portions[i].append(cur)
    vis[cur] = True
    cur = cur * (i+1) % m[i]
  cycle_start[i] = pos_of[cur]
sums = [[0] * (len(portions[i]) + 1) for i in range(11)]
for i in range(11):
  for j in range(1, len(portions[i]) + 1):
    sums[i][j] = sums[i][j-1] + portions[i][j-1]


def is_ovf(a, b, c):
  # a * b exceeds c
  if a == 0 or b == 0:
    return c < 0
  return a > c // b


lo, hi = 0, n + 1
while lo < hi:
  mid = (lo + hi + 1) // 2
  total = n
  for i in range(11):
    n_portions = len(portions[i])
    if portions[i][-1] == 0 or mid <= n_portions:
      total -= sums[i][min(mid, n_portions)]
      continue

    total -= sums[i][n_portions]
    days_left = mid - n_portions

    n_cycle = n_portions - cycle_start[i]
    cycle_sum = sums[i][-1] - sums[i][cycle_start[i]]
    # if is_ovf(days_left // n_cycle, cycle_sum, total):
    #   total = -1
    #   break
    total -=\
        days_left // n_cycle * cycle_sum \
        + sums[i][cycle_start[i] + days_left % n_cycle] \
        - sums[i][cycle_start[i]]
  if total < 0:
    hi = mid-1
  else:
    lo = mid
ans = lo if lo <= n else -1
print(ans)
