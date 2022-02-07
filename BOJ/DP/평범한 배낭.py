# 12865

import sys

input = sys.stdin.readline
n,k = map(int,input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
weight = []
value = []

for _ in range(n):
    w,v = map(int,input().split())
    weight.append(w)
    value.append(v)
    
for i in range(1,n+1):
    for j in range(1,k+1):
        if j < weight[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + value[i-1])

print(dp[n][k])


''' 숏코딩 '''
n,k = map(int,input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w,v = map(int,input().split())
    for j in range(k+1):
        if w > j :
            dp[i][j] = dp[i-1][j]            
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])