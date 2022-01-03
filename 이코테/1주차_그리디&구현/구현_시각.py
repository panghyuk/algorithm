# 책 풀이(완전탐색/브루트 포스)
h = int(input())
cnt = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1

print(cnt)