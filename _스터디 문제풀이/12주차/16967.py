# 배열 복원하기

import sys

input = sys.stdin.readline
h,w,x,y = map(int,input().split())
arr_B = [] # 배열 B

for i in range(h+x):
    arr_B.append(list(map(int,input().split())))

arr_A = [[0]*w for _ in range(h)]

# 배열 A 선언
for i in range(h):
    for j in range(w):
        arr_A[i][j] = arr_B[i][j]

# 겹치는 부분 처리
for i in range(x,h):
    for j in range(y,w):
        # B(i,j) = A(i,j) + A(i-x,j-y) -> A(i,j) = B(i,j) - A(i-x,j-y)
        arr_A[i][j] = arr_B[i][j] - arr_A[i-x][j-y] 

for i in range(h):
    for j in range(w):
        print(arr_A[i][j], end = ' ')
    print()