# 2644

from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1) # 방문 확인
result = [0] * (n+1) # 방문 후 리스트 값 변경
a,b = map(int,input().split())
m = int(input())

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(num):
    q = deque()
    q.append(num)
    visit[num] = True
    
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = True
                result[i] = result[v] + 1
                q.append(i)

bfs(a) # bfs 실행

if result[b] != 0:
    print(result[b])
else:
    print(-1)