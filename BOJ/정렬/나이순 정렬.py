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
