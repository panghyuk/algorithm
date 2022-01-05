# 1080
 
n,m = map(int,input().split())
arr1 = [list(map(int,input())) for _ in range(n)]
arr2 = [list(map(int,input())) for _ in range(n)]
cnt = 0

def reverse(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            arr1[i][j] = 1 - arr1[i][j]

for i in range(n-2):
    for j in range(m-2):
        if arr1[i][j] != arr2[i][j]: # 값이 다를 때
            reverse(i,j)
            cnt += 1

result = True

# 최종 확인
for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j]:
            result = False
            break

if result:
    print(cnt)
else:
    print(-1)

