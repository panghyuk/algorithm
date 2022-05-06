# 1049

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
cost = []
ans = 0

for _ in range(m):
    package, unit = map(int,input().split())
    cost.append([package,unit])

cost_p = sorted(cost)
cost_u = sorted(cost,key = lambda x:x[1])

p = cost_p[0][0]
u = cost_u[0][1]

if p <= u * 6:
    ans = p * (n // 6) + u * (n % 6)
    if p < u * (n % 6):
        ans = p * (n // 6 + 1)
else:
    ans = u * n
    
print(ans)