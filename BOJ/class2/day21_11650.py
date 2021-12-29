# 좌표 정렬하기

import sys

input = sys.stdin.readline
n = int(input())

xy_list = []

for _ in range(n):
    [a,b] = map(int,input().split())
    xy_list.append([a,b])

xy_list.sort(key = lambda x:(x[0],x[1]))

for arr in xy_list:
    print(arr[0],arr[1])