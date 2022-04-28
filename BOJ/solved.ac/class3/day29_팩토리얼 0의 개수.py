# 1676

''' 수학적 풀이 '''
import sys

input = sys.stdin.readline
n = int(input())
cnt = 0

while n >= 5:
    cnt += n // 5
    n //= 5 

print(cnt)


''' 문자열 풀이 '''
# import sys

# input = sys.stdin.readline
# n = int(input())
# cnt = 0

# def facto(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return facto(n-1) * n

# ans = facto(n)

# for x in str(ans)[::-1]:
#     if x != '0':
#         break
#     else:
#         cnt += 1

# print(cnt)