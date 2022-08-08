# 녹색 옷 입은 애가 젤다지?

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b,arr):
    cnt = 0
    q = deque()
    q.append([a,b])

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny < n:
                if visit[nx][ny] == 0:
                    return 0
    
    return 0

while True:
    n = int(input())
    i = 0

    if n == 0:
        exit()

    else:
        graph = []
        for _ in range(n):
            graph.append(list(map(int,input().split())))

        visit = [[0] * n for _ in range(n)]
        ans = [[0] * n for _ in range(n)]