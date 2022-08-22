# 현수막

import sys
from collections import deque

input = sys.stdin.readline
m,n = map(int,input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int,input().split())))

dx = [0,1,1,0,-1,-1,1,-1]
dy = [1,0,1,-1,0,-1,-1,1]
cnt = 0

def bfs(b,a): # x,y 값 바꿔서 넣어주기
    q = deque()
    q.append([b,a])

    while q:
        y,x = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append([ny,nx])
        
# 반복문 돌면서 확인
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            cnt += 1

print(cnt)