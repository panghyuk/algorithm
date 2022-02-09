# 1916

import heapq,sys
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)

        if dis[now] < d:
            continue

        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))
                
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dis = [INF]*(n+1)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

s, e = map(int, input().split())

dijkstra(s)
print(dis[e])