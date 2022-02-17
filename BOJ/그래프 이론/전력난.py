# 6497

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m,n = map(int,input().split())
    if m == n == 0:
        break
    parent = [i for i in range(m+1)]
    edges = []
    res = 0

    for _ in range(n):
        x,y,z = map(int,input().split())
        edges.append((z,x,y))

    edges.sort()

    for edge in edges:
        cost,s,e = edge
        if find(s) != find(e):
            union(s,e)
        else:
            res += cost

    print(res)
