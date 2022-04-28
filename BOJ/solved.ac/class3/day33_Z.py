# 1074 분할 정복/재귀

import sys
input = sys.stdin.readline

n,r,c = map(int,input().split())
ans = 0

def divide(n,x,y):
    global ans
    if x == r and y == c:
        print(ans)
        exit(0)
    
    if n == 1:
        ans += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        ans += n ** 2
        return
    
    n //= 2
    divide(n, x, y)
    divide(n, x, y+n) 
    divide(n, x+n, y)
    divide(n, x+n, y+n)

divide(2**n, 0, 0)




'''
# 다른 풀이
n, r, c = map(int,input().split())
ans = 0

while n != 0:
    n -= 1

    # 1사분면
    if r < 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 0
    # 2사분면
    elif r < 2 ** n and c >= 2 ** n:
        ans += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)
    # 3사분면
    elif r >= 2 ** n and c < 2 ** n:
        ans += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)
    # 4사분면
    else:
        ans += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)

print(ans)
'''