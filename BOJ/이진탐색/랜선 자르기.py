# 1654

import sys

input = sys.stdin.readline
k,n = map(int,input().split())
n_list = []

for i in range(k):
    n_list.append(int(input()))

start = 1
end = max(n_list)
 
while (start <= end):
    cnt = 0
    mid = (start + end) // 2

    for x in n_list:
        cnt += x // mid
    
    if cnt >= n: # cnt가 목표치(n) 이상이면 더 크게 잘라야 함
        start = mid + 1
    else: # cnt가 목표치 미만이면 더 작게 잘라야 함
        end = mid - 1

print(end)