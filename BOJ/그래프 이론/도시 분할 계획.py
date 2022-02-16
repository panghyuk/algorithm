# 1647 크루스칼 알고리즘

import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    rootA = find(parent,a)
    rootB = find(parent,b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

n,m = map(int,input().split())
parent = [i for i in range(n+1)] # 부모를 자기 자신으로 초기화
edges = []
res = []

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

# 크루스칼 알고리즘
for edge in edges:
    cost,s,e = edge
    if find(parent,s) != find(parent,e):
        union(parent,s,e)
        res.append(cost)

print(sum(res[:-1]))