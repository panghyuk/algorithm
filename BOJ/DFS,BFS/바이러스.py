# 2606

# DFS 활용
c = int(input())
pair = int(input())
graph = [[] for _ in range(c+1)]
visit = [False] * (c+1)

for _ in range(pair):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def dfs(n):
    global cnt
    visit[n] = True
    for i in graph[n]:
        if not visit[i]:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)

# BFS 활용
from collections import deque

c = int(input())
pair = int(input())
graph = [[] for _ in range(c+1)]
visit = [False] * (c+1)

for _ in range(pair):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def bfs(n):
    q = deque()
    q.append(n)
    visit[n] = True
    global cnt
    
    while q:
        v = q.popleft()
 
        for i in graph[v]:
            if not visit[i]:
                q.append(i)
                cnt += 1
                visit[i] = True
bfs(1)
print(cnt)