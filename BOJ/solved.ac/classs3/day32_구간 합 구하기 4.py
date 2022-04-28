# 11659 누적합

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
ans = [0]

res = 0
for i in arr:
    res += i
    ans.append(res)

for i in range(m):
    x, y = map(int,input().split())
    print(ans[y]-ans[x-1])