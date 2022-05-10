# 11478

res = str(input())
cnt = []

for i in range(len(res)):
    for j in range(len(res) - i):
        cnt.append(res[j:j+i+1])

print(len(set(cnt)))