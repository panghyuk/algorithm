# 17266

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
x = list(map(int,input().split()))

start = 0
end = n
ans = 0

if len(x) == 1:
    ans = max(x[0],n - x[0])

else:
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        now = 0

        for i in x:
            if i >= now + mid:
                cnt += 1
                now = i
        
        if cnt >= m:
            start = mid + 1
            ans = mid
        
        else:
            end = mid - 1

print(ans)

