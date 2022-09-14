# 안녕

import sys

input = sys.stdin.readline
n = int(input())
L = [0] + list(map(int,input().split())) # 잃는 체력
J = [0] + list(map(int,input().split())) # 얻는 기쁨
health = 100
happy = 0
dp = [[0] * 101 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][-2])