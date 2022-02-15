# 4386
import math

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n+1)]
arr = []
edges = []
res = 0

for _ in range(n):
    a,b = map(float,input().split())
    arr.append((a,b))

for i in range(n-1):
    for j in range(i+1,n):
        edges.append((math.sqrt((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2),i,j))

edges.sort()

for edge in edges:
    cost,s,e = edge

    if find(parent,s) != find(parent,e):
        union(parent,s,e)
        res += cost

print('{:.1f}'.format(res))