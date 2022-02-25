# 1644

import sys, math
input = sys.stdin.readline

# 에라토스테네스의 체
n = int(input())
prime = []
arr = [True for _ in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if arr[i]: 
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

for num in range(2,n+1):
    if arr[num]:
        prime.append(num)

# 투 포인터
cnt = 0
interval = 0
end = 0

for start in range(len(prime)):
    while interval < n and end < len(prime):
        interval += prime[end]
        end += 1

    if interval == n:
        cnt += 1
    interval -= prime[start]

print(cnt)