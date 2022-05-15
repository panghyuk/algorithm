# 2167

n,m = map(int,input().split())
graph = []
acc = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        acc[i][j] = graph[i-1][j-1] + acc[i][j-1] + acc[i-1][j] - acc[i-1][j-1]

k = int(input())

for _ in range(k):
    i,j,x,y = map(int,input().split())
    ans = acc[x][y] - acc[x][j-1] - acc[i-1][y] + acc[i-1][j-1]
    print(ans)