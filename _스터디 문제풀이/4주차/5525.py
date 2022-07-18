# IOIOI

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip()

ans, cnt, num = 0, 0, 0

while num < m - 1:
    if s[num:num+3] == 'IOI':
        cnt += 1
        num += 2
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        num += 1
        cnt = 0

print(ans)

''' 50점 풀이 '''
# import sys

# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# s = list(input())

# target = list('IO' * n + 'I')
# ans = 0

# for i in range(n,m-n):
#     if s[i-n:i+n+1] == target:
#         ans += 1

# print(ans)