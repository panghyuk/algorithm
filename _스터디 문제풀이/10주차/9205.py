# 맥주 마시면서 걸어가기

from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

def bfs(a,b):
    q = deque()
    q.append([a,b])

    while q:
        x,y = q.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000: # 현재 위치에서 페스티벌 위치까지 <= 맥주 20병 * 50미터 (= 1000)
            return 1

        for i in range(n):
            if not visit[i]:
                nx, ny = gs[i]

                if abs(x - nx) + abs(y - ny) <= 1000: # 현재 위치에서 편의점 위치까지 <= 맥주 20병 * 50미터 (= 1000)
                    q.append([nx,ny])
                    visit[i] = 1
    return 0

for _ in range(t):
    n = int(input())
    gs = []
    home = list(map(int,input().split()))
    
    for i in range(n):
        gs.append(list(map(int,input().split())))
           
    festival = list(map(int,input().split()))

    visit = [0 for _ in range(n+1)] # 

    flag = bfs(home[0], home[1])
    
    if flag == 1:
        print('happy')
    else:
        print('sad')