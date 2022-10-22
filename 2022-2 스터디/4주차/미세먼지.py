# 17144

import sys

input = sys.stdin.readline
r,c,t = map(int,input().split())
graph = [[0] * (c + 1)]
ans = 0

for _ in range(r):
    graph.append([0] + list(map(int,input().split())))

for i in range(r):
    if graph[i][1] == -1:
        u,d = i,i+1
        break

def dust():
    new_graph = [[0] * (c+1) for _ in range(r+1)]
    for i in range(1,r+1):
        for j in range(1,c+1):
            if graph[i][j] == 0 or graph[i][j] == -1:
                continue

            else:
                cnt = 0
                tmp = graph[i][j] // 5
                if i+1 <= r and graph[i+1][j] != -1:
                    cnt += 1
                    new_graph[i+1][j] += tmp
                if i-1 >= 1 and graph[i-1][j] != -1:
                    cnt += 1
                    new_graph[i-1][j] += tmp
                if j+1 <= c and graph[i][j+1] != -1:
                    cnt +=1
                    new_graph[i][j+1] += tmp
                if j-1 >= 1 and graph[i][j-1] != -1:
                    cnt += 1
                    new_graph[i][j-1] += tmp

                graph[i][j] -= cnt * tmp
    
    for k in range(1,r+1):
        for l in range(1,c+1):
            graph[k][l] += new_graph[k][l]

    return graph

def air_up():
    # 오른쪽 이동
    for i in range(2,c):
        tmp = graph[u][i+1]
        graph[u][i+1] = graph[u][i]
    
    # 위로 이동


    # 왼쪽으로 이동


    # 아래로 이동
    

    pass
    

def air_down():
    # 오른쪽으로 이동


    # 아래로 이동


    # 왼쪽으로 이동


    # 위로 이동


    pass

# for _ in range(t):
#     dust()
#     air_up()
#     air_down()

# for i in range(1,r+1):
#     ans += sum(graph[i])

# print(ans)