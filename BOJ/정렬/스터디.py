# 빈도 정렬 2910

n,c = map(int,input().split())
n_list = list(map(int,input().split()))
result = {}

for i in n_list:
    if i not in result:
        result[i] = 0
    result[i] += 1

ans = sorted(result.items(),key = lambda x: x[1],reverse = True)

for a,b in ans:
    for i in range(b):
        print(a,end = ' ')
