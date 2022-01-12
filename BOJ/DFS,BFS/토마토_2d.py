# 7576

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int,input().split())
graph = []
q = deque()

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))

bfs()
ans = 0

for row in graph:
    for x in row:
        if x == 0:
            print(-1)
            exit()
    ans = max(max(row),ans)
print(ans - 1)