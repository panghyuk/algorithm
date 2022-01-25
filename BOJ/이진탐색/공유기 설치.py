# 2110

import sys

input = sys.stdin.readline
n,c = map(int,input().split())
x = []

for _ in range(n):
    x.append(int(input()))

x.sort()

start = 1 # 최소 거리
end = max(x) - min(x) # 최대 거리
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    now = x[0]

    for i in x:
        if i == x[0]: # 예외 처리
            pass

        if i >= now + mid:
            cnt += 1
            now = i
    
    if cnt >= c:
        ans = mid
        start = mid + 1
    
    else:
        end = mid - 1

print(ans)