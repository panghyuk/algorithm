# 1457

num = list(map(int,input()))
cnt = {}
for i in range(10):
    cnt[i] = 0

for j in num:
    if j == 9:
        cnt[6] += 1
    else:
        cnt[j] += 1

if cnt[6] % 2 == 0:
    cnt[6] //= 2
else:
    cnt[6] //= 2
    cnt[6] += 1 

print(max(cnt.values()))
