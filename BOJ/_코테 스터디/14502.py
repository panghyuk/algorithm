from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

ans = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = graph[i][j]

    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i,j))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    q.append((nx,ny))
    
    cnt = 0
    global ans

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                cnt += 1

    ans.append(cnt)

def wall(num):
    if num == 3:
        bfs()
        return None

    for k in range(n):
        for l in range(m):
            if graph[k][l] == 0:
                graph[k][l] = 1
                wall(num + 1)
                graph[k][l] = 0

wall(0)
print(max(ans))