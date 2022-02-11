# 17396

import heapq,sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
vision = list(map(int,input().split()))
vision[-1] = 0
graph = [[] for _ in range(n)]


for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))


q = []
heapq.heappush(q,(0,0))
dis = [INF] * n
dis[0] = 0

while q:
    d, now = heapq.heappop(q)
    if dis[now] < d:
        continue

    for i in graph[now]:
        cost = d + i[1]

        if cost < dis[i[0]]:
            if vision[i[0]] == 0:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

if dis[-1] == INF:
    print(-1)
else:
    print(dis[-1])