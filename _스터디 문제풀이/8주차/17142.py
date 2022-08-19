# 연구소 3

# 0: 빈 칸/1: 벽/2: 바이러스

from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
visit = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int,input().split())))

