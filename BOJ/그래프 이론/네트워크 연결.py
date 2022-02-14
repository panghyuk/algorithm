# 1922

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find(parent,x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = [0] * (n+1)
edges = []
result = 0

# 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort() # 비용 순으로 정렬

for edge in edges:
    cost,s,e = edge
    if find(parent,s) != find(parent,e):
        union(parent,s,e)
        result += cost

print(result)