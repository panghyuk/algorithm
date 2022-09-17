# 배열 돌리기 1

import sys 

input = sys.stdin.readline
n,m,r = map(int,input().split())
arr = []
depth = min(n,m) // 2

for _ in range(n):
    arr.append(list(map(int,input().split())))

def rotate():
    for i in range(depth):
        x,y = i,i # 배열 시작 부분
        tmp = arr[x][y] # tmp에 저장

        for j in range(i + 1,n - i): # 하
            x = j
            pre = arr[x][y]
            arr[x][y] = tmp
            tmp = pre

        for j in range(i + 1,m - i): # 우
            y = j
            pre = arr[x][y]
            arr[x][y] = tmp
            tmp = pre

        for j in range(i + 1,n - i): # 상
            x = n - j - 1
            pre = arr[x][y]
            arr[x][y] = tmp
            tmp = pre

        for j in range(i + 1,m - i): # 좌
            y = m - j - 1
            pre = arr[x][y]
            arr[x][y] = tmp
            tmp = pre


for _ in range(r):
    rotate()

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()