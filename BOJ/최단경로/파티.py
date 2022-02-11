# 1238

import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,time = map(int,input().split())
    graph[a].append((b,time))

def dijkstra(start):
    q = []
    dis = [INF] * (n+1)
    
    heapq.heappush(q,(0,start))
    dis[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if dis[now] < dist: # 아래 코드를 실행하지 않고 건너뜀
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return dis

res = 0

for i in range(1,n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    res = max(res,go[x] + back[i])

print(res)