# 2910

n,c = map(int,input().split())
n_list = list(map(int,input().split()))
result = {}

for i in n_list:
    if i not in result: # i가 딕셔너리 안에 없을 때
        result[i] = 0 # 0으로 초기화
    result[i] += 1

print(result.items())

ans = sorted(result.items(), key = lambda x: x[1], reverse = True) # 빈도에 따라 내림차순 정렬

print(ans)

for k,v in ans:
    for i in range(v):
        print(k, end = ' ')