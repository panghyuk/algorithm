# 2468

from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = []
MaxNum = 0

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        MaxNum = max(MaxNum, graph[i][j])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b,height):
    q = deque()
    q.append([a,b])
    visit[a][b] = 1 # 방문처리

    while q:
        x,y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
        
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > height and visit[nx][ny] == 0: # 현재 높이보다 높고 방문 하지 않은 곳
                    visit[nx][ny] = 1
                    q.append([nx,ny])
ans = 0

for h in range(MaxNum):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visit[i][j] == 0: # 현재 높이보다 높고 방문 하지 않은 곳 확인
                bfs(i,j,h)
                cnt += 1

    ans = max(ans, cnt)

print(ans)