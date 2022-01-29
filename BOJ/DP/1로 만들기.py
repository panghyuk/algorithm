# 1463

import sys

input = sys.stdin.readline
x = int(input())

dp = [0] * (x + 1)

for i in range(2,x+1):
    dp[i] = dp[i-1] + 1 # 1 빼는 연산을 먼저하는 이유: 어차피 아래의 연산 과정에서 교체

    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3] + 1)

print(dp[x])