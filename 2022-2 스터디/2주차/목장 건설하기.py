# 14925 해결 X

from collections import deque

m,n = map(int,input().split())
land = []

for _ in range(m):
    land.append(list(map(int,input().split())))

visit = [[0] * m for _ in range(n)]
visit[0][0] = 1

for i in range(1,m):
    for j in range(1,n):
        if land[i-1][j-1] == 0:
            visit[i][j]


'''
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    q = deque()
    q.append([a,b])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if land[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx,ny])
'''