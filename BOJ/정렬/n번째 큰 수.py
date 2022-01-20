# 2075

import sys, heapq

input = sys.stdin.readline 
n = int(input())
heap = []

for _ in range(n):
    nums = list(map(int,input().split()))

    if not heap: # heap이 비어 있을 때 (처음 입력이 들어올 때)
        for num in nums:
            heapq.heappush(heap,num)
    
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap,num) # heap에 원소 추가
                heapq.heappop(heap) # heap에서 제일 작은 원소 삭제

print(heap[0])