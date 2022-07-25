# 안전 영역

from collections import deque

n = int(input())
graph = []
ans = 0

for _ in range(n):
    graph.append(list(map(int,input().split())))

max_h = max(max(graph))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b,height):
    q = deque()
    q.append([a,b])
    visit[a][b] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] >= height and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx,ny])

for h in range(1,max_h + 1):
    visit = [[0] * n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] >= h and visit[j][k] == 0:
                bfs(j,k,h)
                cnt += 1
    
    ans = max(ans,cnt)

print(ans)