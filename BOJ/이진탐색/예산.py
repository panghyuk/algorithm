# 2512

import sys

input = sys.stdin.readline
n = int(input())
budget = list(map(int,input().split()))
m = int(input())

start = 1
end = max(budget)
ans = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for x in budget:
        if x > mid:
            total += mid
        else:
            total += x
    
    if total > m:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)