# 2178

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

def bfs(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
                    
    return graph[n-1][m-1]

print(bfs(0,0))