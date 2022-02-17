# 9372

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

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    parent = [i for i in range(n+1)]

    edges = []
    res = 0

    for i in range(m):
        a,b = map(int,input().split())
        edges.append((a,b))

    for edge in edges:
        s,e = edge
        if find(s) != find(e):
            res += 1
            union(s,e)
    print(res)