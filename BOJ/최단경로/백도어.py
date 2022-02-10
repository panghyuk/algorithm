# 17396

import heapq,sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
vision = list(map(int,input().split()))
graph = [[] for _ in range(n)]
dis = [INF] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if d < dis[now]:
            continue

        for i in graph[now]:
            cost = d + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
