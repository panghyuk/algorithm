# 10841

import sys

input = sys.stdin.readline
n = int(input())
name = []

for _ in range(n):
    a,b = input().split()
    name.append((int(a),b))

name.sort(key = lambda x: x[0])

for i in name:
    print(i[0],i[1])


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