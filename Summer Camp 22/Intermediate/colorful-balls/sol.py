k = int(input())
c = int(input())
n = []
for i in range(c):
  n.append(int(input()))

l, r = 0, 10**18
while l < r:
  mid = (l+r+1)//2
  tot = 0
  for i in range(c):
    tot += min(n[i], mid)
  if tot//mid >= k:
    l = mid
  else:
    r = mid-1
print(l)
