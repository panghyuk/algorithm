# 1753

import heapq,sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
dis = [INF] * (v+1)

for _ in range(e):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if dis[now] < d:
            continue

        for i in graph[now]:
            cost = d + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)

for i in range(1,v+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])