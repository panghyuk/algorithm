# 1446

n, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dis = [i for i in range(d+1)]

for i in range(d+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in graph:
        if i == s and e <= d and dis[i] + d < dis[e]:
            dis[e] = dis[i]+d

print(dis[d])


''' 다른 사람 풀이 '''
n,d = map(int,input().split())
graph = [[] for _ in range(10001)]

for _ in range(n):
    s,e,w = map(int,input().split())
    graph[s].append([w,e])

dis = [i for i in range(d+1)]

for i in range(d+1):
    if i != 0:
        dis[i] = min(dis[i],dis[i-1] + 1)
    for w,e in graph[i]:
        if e <= d and dis[e] > w + dis[i]:
            dis[e] = w + dis[i]

print(dis[d])