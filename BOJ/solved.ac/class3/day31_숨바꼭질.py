# 1697

import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    q = deque()
    q.append(num)
    
    while q:
        v = q.popleft()
        if v == k:
            return time[v]

        for i in [v-1,v+1,2*v]:
            if 0 <= i <= 100000 and not time[i]:
                time[i] = time[v] + 1
                q.append(i)

n,k = map(int,input().split())
time = [0] * (100001)

print(bfs(n))