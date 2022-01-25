#  2343

import sys

input = sys.stdin.readline
n,m = map(int,input().split())
guitar = list(map(int,input().split()))

start = max(guitar) # 가장 작은 크기의 블루레이
end = sum(guitar) # 가장 큰 크기의 블루레이
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    total = 0

    for x in guitar:
        if total + x > mid: # total이 mid보다 커지면 새로운 블루레이 필요
            cnt += 1
            total = 0

        total += x

    if total: # for 문 다 돌고 나서 마지막 남은 블루레이 처리
        cnt += 1

    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)




''' 시간 초과'''
# import sys

# input = sys.stdin.readline
# n,m = map(int,input().split())
# guitar = list(map(int,input().split()))

# ans = 0
# res1 = 0
# res2 = 0
# res3 = 0

# for i in range(n):
#     for j in range(i,n):
#         res1 = sum(guitar[:i])
#         res2 = sum(guitar[i:j])
#         res3 = sum(guitar[j:])
#         tmp = max(res1,res2,res3)
#         if ans == 0:
#             ans = tmp
#         elif ans > tmp:
#             ans = tmp

# print(ans)