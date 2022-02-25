# 21919

import sys,math
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
res = []
ans = 1

def prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

for x in arr:
    if prime(x):
        if x in res:
            continue
        else:
            res.append(x)

if len(res) == 0:
    print(-1)
else:
    for i in res:
        ans *= i
    print(ans)