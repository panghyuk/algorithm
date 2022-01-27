# 2792

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
jewerly = []

for _ in range(m):
    jewerly.append(int(input()))

ans = 0
start = 1
end = max(jewerly)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for x in jewerly:
        if x % mid == 0: # mid로 나누어 떨어질 때
            cnt += x // mid
        else: # mid로 나누어 떨어지지 않을 때
            cnt += x // mid + 1
    
    if cnt > n:
        start = mid + 1
    else:
        end = mid - 1

print(start)