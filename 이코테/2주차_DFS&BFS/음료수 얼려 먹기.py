# DFS

def dfs(x,y):
    # 주어진 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았을 때
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상/하/좌/우 재귀로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m = map(int,input().split())
graph = []
cnt = 0

for _ in range(m):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt += 1
print(cnt)