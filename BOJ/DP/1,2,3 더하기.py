# 9095

t = int(input())
for _ in range(t):
    
    n = int(input())
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])


''' 다른 사람 풀이'''
# t = int(input())

# def sol(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return sol(n-1) + sol(n-2) + sol(n-3)

# for i in range(t):
#     n = int(input())
#     print(sol(n))