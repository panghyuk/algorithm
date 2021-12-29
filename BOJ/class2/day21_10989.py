# 수 정렬하기 3

import sys
input = sys.stdin.readline

n = int(input())
n_list =[0] * 100001

for _ in range(n):
    n_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)