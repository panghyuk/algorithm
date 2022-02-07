# 2739

n = int(input())

m = 10**6
n %= 15*(10**5)

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2,n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % m

print(dp[n])