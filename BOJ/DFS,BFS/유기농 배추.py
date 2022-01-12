# 1012

from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))

for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [([0] * m) for _ in range(n)]
    
    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1

    cnt = 0

    for i in range(n): # 세로
        for j in range(m): # 가로
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)


# 내 풀이_DFS(런타임에러)

import sys
# 재귀 최대 깊이 설정
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [([0] * m) for _ in range(n)]
    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1

    cnt = 0

    for i in range(m):
        for j in range(n):
            if dfs(i,j) == True:
                cnt += 1

    print(cnt)