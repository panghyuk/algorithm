# 퇴사

n = int(input())
t = []
p = []
dp = [0] * 16

for _ in range(n):
    time,profit = map(int,input().split())
    t.append(time)
    p.append(profit)

for i in range(n-1,-1,-1): # -1씩 거꾸로
    if t[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])

print(dp[0])