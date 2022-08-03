# 치킨 배달
# 0: 빈칸
# 1: 집
# 2: 치킨집

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

chickens = []
homes = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집
            homes.append([i,j])
        elif graph[i][j] == 2: # 치킨집
            chickens.append([i,j])