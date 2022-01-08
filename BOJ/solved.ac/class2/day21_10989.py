# 수 정렬하기 3

import sys

n = int(input())
num_list =[0] * 100001

input = sys.stdin.readline

for _ in range(n):
    num_list[int(input())] += 1 # 입력 숫자에 해당하는 idx += 1 

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)