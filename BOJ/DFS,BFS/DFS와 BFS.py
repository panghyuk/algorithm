# 1260

import sys
from collections import deque

input = sys.stdin.readline
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit1 = [False] * (n+1)
visit2 = [False] * (n+1)

# 그래프 입력
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# input 오름차순 정렬
for i in range(1,n+1):
    graph[i].sort()

# DFS
def dfs(num):
    visit1[num] = True # 방문 처리
    print(num, end = ' ')
    for i in graph[num]:
        if not visit1[i]:
            dfs(i)

# BFS
def bfs(num):
    q = deque([num])
    visit2[num] = True # 방문 처리
    while q:
        v = q.popleft() # 첫번째 값 빼기
        print(v, end = ' ')
        for i in graph[v]:
            if not visit2[i]:
                q.append(i)
                visit2[i] = True

dfs(v)
print()
bfs(v)