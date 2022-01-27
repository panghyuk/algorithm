# 16401

import sys

input = sys.stdin.readline
m,n = map(int,input().split())
cookie = list(map(int,input().split()))

start = 1
end = max(cookie)
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for x in cookie:
        if x >= mid:
            cnt += x // mid
    
    if cnt >= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)