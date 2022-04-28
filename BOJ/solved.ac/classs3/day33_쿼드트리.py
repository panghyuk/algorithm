# 1992 분할 정복/재귀
import sys

input = sys.stdin.readline 
n = int(input())
arr = [list(map(int,input().strip())) for _ in range(n)]

res = ''

def quad_tree(x,y,n):
    global res
    c = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if c != arr[i][j]:
                res += "("
                quad_tree(x, y, n//2)
                quad_tree(x, y + n//2, n//2)
                quad_tree(x + n//2, y , n//2)
                quad_tree(x + n//2, y + n//2, n//2)
                res += ")"
                return
    res += str(c)

quad_tree(0,0,n)
print(res)