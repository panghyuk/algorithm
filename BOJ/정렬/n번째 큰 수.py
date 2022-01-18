# 2075

# 내 풀이 메모리 초과
import sys
from collections import deque

n_list = []
input = sys.stdin.readline 

n = int(input())
for _ in range(n):
    n_list += (list(map(int,input().split())))

n_list.sort(reverse = True)
q = deque()
q.append(n_list)

print(q[0][n-1])
