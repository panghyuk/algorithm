# 2579

''' Top-Down 방식 '''
import sys

input = sys.stdin.readline
n = int(input())
dp = [0] * 301
score = [0] * 301

for i in range(1,n+1):
    score[i] = int(input())

dp[1] = score[1]
dp[2] = score[1] + score[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3] + score[i-1], dp[i-2]) + score[i]

print(dp[n])