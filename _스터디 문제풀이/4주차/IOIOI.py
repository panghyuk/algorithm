# 5525

import sys

input = sys.stdin.readline
n = int(input())

target = list('IO' * n + 'I')

m = int(input())
s = list(input())

ans = 0

for i in range(n,m-n):
    if s[i-n:i+n+1] == target:
        ans += 1

print(ans)