# 10815

import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

result = {m_list[i]:0 for i in range(m)}

for i in range(n):
    if n_list[i] in result.keys():
        result[n_list[i]] += 1

for v in result.values():
    print(v,end = ' ')