# 8979

# # 리스트 활용 (100점)
# n,k = map(int,input().split())
# ranking = [[] for _ in range(n+1)]

# for _ in range(n):
#     country, gold, silver, bronze = map(int,input().split())
#     ranking[country] = [gold,silver,bronze]

# cnt = 1

# for i in range(1,n+1):
#     if ranking[k][0] < ranking[i][0]:
#         cnt += 1
#     elif ranking[k][0] == ranking[i][0]:
#         if ranking[k][1] < ranking[i][1]:
#             cnt += 1
#         elif ranking[k][1] == ranking[i][1]:
#             if ranking[k][2] < ranking[i][2]:
#                 cnt += 1

# print(cnt)


# sort(key=lambda 활용) 20점 풀이
n,k = map(int,input().split())
ranking = []

for i in range(n):
    ranking.append(list(map(int,input().split())))

ranking.sort(key = lambda x: (-x[1], -x[2], -x[3]))

cnt = 1

for idx in range(n):
    if ranking[idx][0] == k:
        k = idx

for i in range(n):
    if ranking[k][1] < ranking[i][1]:
        cnt += 1
    elif ranking[k][1] == ranking[i][1]:
        if ranking[k][2] < ranking[i][2]:
            cnt += 1
        elif ranking[k][2] == ranking[i][2]:
            if ranking[k][3] < ranking[i][3]:
                cnt += 1

print(cnt)