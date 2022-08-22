# 시험감독

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
cnt = 0

for i in a:
    cnt += 1
    i -= b
    
    if i > 0:
        if i % c != 0: # 나머지가 존재할 때
            cnt += (i//c) + 1
        else: # 나머지가 없을 때
            cnt += (i//c)

print(cnt)