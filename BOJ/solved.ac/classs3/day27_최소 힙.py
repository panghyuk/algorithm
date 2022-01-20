# 1927

import heapq,sys

input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
    res = int(input())
    
    if res == 0:
        if not heap:
            print(0)
        else:
            ans = heapq.heappop(heap)
            print(ans)
    
    else:
        heapq.heappush(heap,res)
