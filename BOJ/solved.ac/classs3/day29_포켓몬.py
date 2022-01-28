# 1620

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
pk_list = []
pk_dict = {}

for i in range(1,n+1):
    data = input().rstrip()
    pk_list.append(data)
    pk_dict[data] = i

for _ in range(m):
    question = input().rstrip()
    
    if question.isdigit():
        print(pk_list[int(question)-1])
    else:
        print(pk_dict[question])