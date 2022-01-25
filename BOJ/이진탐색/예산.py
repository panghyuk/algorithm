# 2512

import sys

input = sys.stdin.readline
n = int(input())
budget = list(map(int,input().split()))
m = int(input())

start = 0
end = max(budget)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in budget:
        if x > mid:
            total += mid
        else:
            total += x
    
    if total > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)