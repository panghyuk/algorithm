# 2156
import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
dp = [0] * (n + 1) 

for _ in range(n):
    wine.append(int(input()))

dp[1] = wine[1]

if n > 1: # 예외처리..
    dp[2] = wine[1] + wine[2]

for i in range(3,n+1):
    dp[i] = (max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i]))

print(dp[n])