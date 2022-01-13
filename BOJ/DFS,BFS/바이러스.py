# 2606

# DFS 활용
c = int(input())
pair = int(input())
graph = [[] for _ in range(c+1)]
visit = [False] * (c+1)
cnt = 0

for _ in range(pair):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    global cnt # 전역변수 선언
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
cnt = 0

for _ in range(pair):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(n):
    global cnt # 전역변수 선언
    q = deque([n])
    visit[n] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = True
                q.append(i)
                cnt += 1
bfs(1)
print(cnt)