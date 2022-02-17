# 14567

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
indegree = [0] * (n+1)
semester = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology():
    res = []
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append((i,1))
            semester[i] = 1
    
    while q:
        now,cnt = q.popleft()
        res.append(now)
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append((i,cnt + 1))
                semester[i] = cnt + 1
    
    for i in range(len(semester)-1):
        print(semester[i+1], end = " ")

topology()