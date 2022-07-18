# 벽 부수고 이동하기
from collections import deque

n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

# print(graph)

cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit = [[0] * m for _ in range(n)]

def bfs(a,b):
    q = deque()
    q.append([a,b])
    while q:
        x,y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] ==0 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx,ny])

ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and cnt == 0:
            cnt += 1
            graph[i][j] = 0
            bfs(i,j)
        elif graph[i][j] == 0:
            bfs(i,j)
            ans += 1
