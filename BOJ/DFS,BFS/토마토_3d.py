# 7569

from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

m,n,h = map(int,input().split())
graph = []
q = deque()

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append((i,j,k))
    graph.append(tmp)

def bfs():
    
    while q:
        x,y,z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    q.append((nx,ny,nz))

bfs()
ans = 0

for matrix in graph:
    for row in matrix:
        for x in row:
            if x == 0:
                print(-1)
                exit()
        ans = max(max(row),ans)
print(ans - 1)