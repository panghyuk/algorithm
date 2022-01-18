# 2217

import sys

input = sys.stdin.readline
n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse = True) # 내림차순 정렬
w = 0

for i in range(n):
    w = max(w,rope[i]*(i+1))

print(w)