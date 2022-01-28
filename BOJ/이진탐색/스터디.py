# 1654 랜선 자르기

import sys

input = sys.stdin.readline
k,n = map(int,input().split())
lan = []

for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for x in lan:
        cnt += x // mid
    
    if cnt >= n: # 더 크게 잘라야 함
        start = mid +1
    else: # 더 작게 잘라야 함
        end = mid - 1

print(end)
print(start)