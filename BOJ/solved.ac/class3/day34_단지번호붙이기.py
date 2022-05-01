# 2667

from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
cnt = 0
ans = []

for i in range(n):
    graph.append(list(map(int,input().strip())))


def bfs(a,b):
    q = deque([a,b])
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                return

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            cnt += 1
