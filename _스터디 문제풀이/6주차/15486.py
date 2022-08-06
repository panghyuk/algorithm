# 퇴사 2

''' sol.1'''
n = int(input())
t = []
p = []
dp = [0] * (n + 1)

for _ in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)

for i in range(n):
    if t[i] <= n - i: # 남은 날 안에 끝낼 수 있는지 확인
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])
        
    dp[i + 1] = max(dp[i + 1], dp[i])
    
print(dp[n])

''' sol.2 '''
# import sys

# input = sys.stdin.readline
# n = int(input())

# dp = [0] * (n+1)
# time = []
# profit = []

# for _ in range(n):
#     t,p = list(map(int,input().split()))
#     time.append(t)
#     profit.append(p)

# for i in range(n-1,-1,-1):
#     if time[i] + i > n:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(profit[i] + dp[i + time[i]], dp[i+1])

# print(dp[0])