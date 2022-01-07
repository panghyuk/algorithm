# 마인크래프트
# 브루트포스(완전 탐색)

import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
cnt = 0
total_time = 0

land = []
for _ in range(n):
    land.append(list(map(int,input().split())))
