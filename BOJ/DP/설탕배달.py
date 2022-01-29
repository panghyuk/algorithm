# 2839 

''' DP 풀이 '''
import sys

input = sys.stdin.readline
n = int(input())
cnt = 0

dp = [5001] * (n + 5) # n의 값이 5보다 작은 경우 index out of range 오류 방지
dp[3] = 1
dp[5] = 1

for i in range(6,n+1):
    dp[i] = min(dp[i-3],dp[i-5]) + 1

if dp[n] < 5001:
    print(dp[n])
else:
    print(-1)


''' 다른 풀이 '''
# n = int(input())
# cnt = 0

# while n >= 0:
#     if n % 5 == 0:
#         cnt += (n//5)
#         print(cnt)
#         break
#     n -= 3
#     cnt += 1

# else:
#     print(-1)