# 2003

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
interval = 0
end = 0

for start in range(n):
    while interval < m and end < n:
        interval += arr[end]
        end += 1
    if interval == m:
        cnt += 1
    interval -= arr[start]

print(cnt)