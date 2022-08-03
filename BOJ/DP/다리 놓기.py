# 1010

''' sol.1 Combination 활용 '''
# def facto(x):
#     res = 1
#     for i in range(1,x+1):
#         res *= i

#     return res

# t = int(input())

# for _ in range(t):
#     n,m = map(int,input().split()) # n <= m
#     print(facto(m) // (facto(n) * facto(m-n))) # mCn 조합으로 해결


''' sol.2 dp 활용 '''
t = int(input())

dp = [[1] * 31 for _ in range(31)]

for i in range(31):
    dp[1][i] = i

for i in range(2,31):
    for j in range(i+1, 31):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

for _ in range(t):
    n,m = map(int,input().split())
    print(dp[n][m])