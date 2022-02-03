# 14501

import sys

input = sys.stdin.readline
n = int(input())

dp = [0] * (n+1)
time = []
profit = []

for _ in range(n):
    t,p = list(map(int,input().split()))
    time.append(t)
    profit.append(p)

for i in range(n-1,-1,-1):
    if time[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(profit[i] + dp[i + time[i]], dp[i+1])

print(dp[0])