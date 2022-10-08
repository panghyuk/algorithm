# 14503

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
visit = [[0] * m for _ in range(n)]

# d = 0: 북/d = 1 동/d = 2 남/ d = 3 서
r,c,d = map(int,input().split())

# 회전하는 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 현재 위치 방문처리
visit[r][c] = 1
cnt = 1

while True:
    flag = False # 청소 X

    for i in range(4):
        d = (d+3) % 4 # 왼쪽으로 회전
        nx, ny = r + dx[d], c + dy[d]

        if 0 <= nx < n and 0 <= ny < m: # 범위 안에 포함
            if graph[nx][ny] == 0:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1 # 청소 진행
                    cnt += 1
                    r,c = nx, ny
                    flag = True # 청소 O
                    break
        
    if not flag: # 청소 불가능
        if graph[r - dx[d]][c - dy[d]] == 1: # 뒤 위치가 벽일 때
            print(cnt)
            break
        else:
            r = r - dx[d]
            c = c - dy[d]