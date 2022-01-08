# 덩치
# 브루트포스

n = int(input())

w_list = []

for i in range(n):
    w_list.append(list(map(int,input().split())))

rank = [1 for _ in range(n)]

for j in range(n):
    for k in range(n):
        if w_list[j][0] < w_list[k][0] and w_list[j][1] < w_list[k][1]:
            rank[j] += 1

for i in rank:
    print(i, end = ' ')
