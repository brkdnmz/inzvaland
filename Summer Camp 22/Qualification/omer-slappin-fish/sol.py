from collections import deque


def solve(n, m):
  assert n*m <= 10**6
  g = [1 for i in range(n)]
  for i in range(n):
    g[i] = input()
  q = deque([])
  fish_dist = [[10**9]*m for _ in range(n)]
  omer_dist = [[10**9]*m for _ in range(n)]
  omer_dist[0][0] = 0
  q.append((0, 0))
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]

  def safe(i, j):
    return 0 <= i < n and 0 <= j < m
  # Perform BFS from Omer
  while len(q):
    cur = q.popleft()
    ci, cj = cur
    for d in range(4):
      i = ci + dx[d]
      j = cj + dy[d]
      if not safe(i, j):
        continue
      if omer_dist[i][j] <= omer_dist[ci][cj] + 1:
        continue
      omer_dist[i][j] = omer_dist[ci][cj] + 1
      q.append((i, j))
  # Perform multisource BFS from the fish
  for i in range(n):
    for j in range(m):
      if g[i][j] == 'F':
        q.append((i, j))
        fish_dist[i][j] = 0
  is_slap = [[0]*m for _ in range(n)]
  while len(q):
    cur = q.popleft()
    ci, cj = cur
    if omer_dist[ci][cj] >= fish_dist[ci][cj]:
      is_slap[ci][cj] = 1
    for d in range(4):
      i = ci + dx[d]
      j = cj + dy[d]
      if not safe(i, j):
        continue
      if fish_dist[i][j] <= fish_dist[ci][cj] + 1:
        continue
      fish_dist[i][j] = fish_dist[ci][cj] + 1
      q.append((i, j))
  # Calculate the minimum number of slaps until each cell
  min_slaps = [[10**9]*m for _ in range(n)]
  min_slaps[0][0] = is_slap[0][0]
  q.append((0, 0))
  while len(q):
    cur = q.popleft()
    ci, cj = cur
    for d in range(4):
      i = ci + dx[d]
      j = cj + dy[d]
      if not safe(i, j):
        continue
      if min_slaps[i][j] <= min_slaps[ci][cj] + is_slap[i][j]:
        continue
      min_slaps[i][j] = min_slaps[ci][cj] + is_slap[i][j]
      q.append((i, j))
  print(min_slaps[n-1][m-1])


n, m = map(int, input().split())
print(solve(n, m))
