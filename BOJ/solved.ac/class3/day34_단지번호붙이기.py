# 2667

from collections import deque
import sys

# bfs 실행
def bfs(a,b):
    cnt = 1
    q = deque()
    q.append([a,b])
    graph[a][b] = 0 # 처음 노드 방문처리
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx,ny])
                cnt += 1
    ans.append(cnt)

input = sys.stdin.readline
n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
ans = []
res = 0

# input 입력
for _ in range(n):
    graph.append(list(map(int,input().strip())))

# 이중 for문 돌면서 bfs 실행
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            res += 1

# 오름차순 정렬
ans.sort()

print(len(ans))
for i in ans:
    print(i)