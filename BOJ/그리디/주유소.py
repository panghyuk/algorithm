# 13305

n = int(input())
dis = list(map(int,input().split()))
cost = list(map(int,input().split()))

ans = 0
min_cost = cost[0]

for i in range(n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
        ans += min_cost * dis[i]
    else:
        ans += min_cost * dis[i]

print(ans)