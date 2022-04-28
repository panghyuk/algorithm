# 2630 분할 정복/재귀

import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

cnt_w = 0
cnt_b = 0

def divide(x,y,n):
    global cnt_w,cnt_b
    c = arr[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if c != arr[i][j]:
                divide(x, y, n//2)
                divide(x, y + n//2, n//2)
                divide(x + n//2, y , n//2)
                divide(x + n//2, y + n//2, n//2)
                return None # 실행 중단 코드
    if c == 1:
        cnt_b += 1
    else:
        cnt_w += 1

divide(0,0,n)
print(cnt_w)
print(cnt_b)