# 11724
import sys
sys.setrecursionlimit(1000000) # 최대 재귀 깊이 설정
input = sys.stdin.readline

def dfs(num):
    visit[num] = True
    for i in graph[num]:
        if not visit[i]:
            dfs(i)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
cnt = 0

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if not visit[i]:
        dfs(i)
        cnt += 1

print(cnt)