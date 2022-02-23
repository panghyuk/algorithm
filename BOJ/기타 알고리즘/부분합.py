# 1806

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))

cnt = []
interval = 0
end = 0

for start in range(n):
    while interval < m and end < n:
        interval += arr[end]
        end += 1
    if interval >= m:
        cnt.append(end - start)
    interval -= arr[start]

if len(cnt) >= 1:
    print(min(cnt))
else:
    print(0)