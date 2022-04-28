# 11286

import heapq,sys

input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
    res = int(input())
    
    if res != 0:
        heapq.heappush(heap,(abs(res),res))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])