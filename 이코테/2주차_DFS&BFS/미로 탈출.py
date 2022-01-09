# BFS
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] == graph[x][y] + 1
                q.append((nx,ny))
    # 가장 오른쪽 아래까지의 거리 반환
    return graph[n-1][m-1]

n,m = map(int,input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int,input().split())))

# 상/하/좌/우 방향 벡터 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))