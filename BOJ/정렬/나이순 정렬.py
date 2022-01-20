# 10841

import sys

input = sys.stdin.readline
n = int(input())
n_list = []

for i in range(n):
    a,b = input().split()
    n_list.append([i,int(a),b])

n_list.sort(key = lambda x: (x[1],x[0]))

for i in n_list:
    print(i[1],i[2])


# 옛날 풀이
n=int(input())
s_list=[]

for i in range(n):
    age,name=input().split()
    age=int(age)
    s_list.append([age,name])
    
s_list.sort(key=lambda x:x[0])

for i in s_list:
    print(i[0],i[1])