# 1890

n = int(input())
game = []
visit = [[0] * n for _ in range(n)]
visit[0][0] = 1

for _ in range(n):
    game.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(visit[i][j])
        
        tmp = game[i][j]

        if i + tmp < n: # 아래쪽으로
            visit[i + tmp][j] += visit[i][j]
        
        if j + tmp < n: # 오른쪽으로
            visit[i][j + tmp] += visit[i][j]