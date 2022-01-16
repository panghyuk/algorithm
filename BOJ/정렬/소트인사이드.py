# 1427

arr = input()
ans = []
for i in arr:
    ans.append(int(i))

ans.sort(reverse = True)

for i in ans:
    print(i,end = "")