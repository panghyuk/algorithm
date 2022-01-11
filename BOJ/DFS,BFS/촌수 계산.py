# 2644

from collections import deque

def bfs(num):
    q = deque()
    q.append(num)
    visit[num] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[v] + 1
                q.append(i)

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1) # 방문 확인
result = [0] * (n+1) # 방문 후 리스트 값 변경
a,b = map(int,input().split())
m = int(input())

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)
if result[b] != 0:
    print(result[b])
else:
    print(-1)
