# 10451

# dfs 정의
def dfs(n):
    visit[n] = True
    next = graph[n] # 다음 노드로 이동
    if not visit[next]:
        dfs(next)

t = int(input())

for _ in range(t):
    num = int(input())
    visit = [False] * (num + 1)
    cnt = 0
    graph = [0] + (list(map(int,input().split())))
    
    for i in range(1,num+1):
        if visit[i] == False:
            dfs(i)
            cnt += 1
    print(cnt)

