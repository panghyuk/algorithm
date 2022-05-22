# 7562

from collections import deque
import sys

input = sys.stdin.readline
dx = [-1,-1,1,1,2,2,-2,-2]
dy = [2,-2,2,-2,-1,1,-1,1]

def bfs(s1,s2,e1,e2):
    q = deque()
    q.append([s1,s2])

    while q:
        a,b = q.popleft()
        if a == e1 and b == e2:
            print(graph[e1][e2])
            return 

        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
        
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                q.append([nx,ny])
                graph[nx][ny] = graph[a][b] + 1

t = int(input())

for _ in range(t):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    x,y = map(int,input().split())
    fx,fy = map(int,input().split())
    bfs(x,y,fx,fy)

