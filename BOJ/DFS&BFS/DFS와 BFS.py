# 1260

import sys
from collections import deque

input = sys.stdin.readline
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit1 = [False] * (n+1)
visit2 = [False] * (n+1)

# 입력 받는 값 1로 바꾸기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

# DFS
def dfs(num):
    visit1[num] = True
    print(num, end = ' ')
    for i in graph[num]:
        if not visit1[i]:
            dfs(i)

# BFS
def bfs(num):
    que = deque([num])
    visit2[num] = True
    while que:
        v = que.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visit2[i]:
                que.append(i)
                visit2[i] = True

dfs(v)
print()
bfs(v)