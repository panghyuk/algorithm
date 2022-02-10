# 1916

import heapq,sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dis = [INF] * (n+1)

for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

start,end = map(int,input().split())

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

dijkstra(start)
print(dis[end])