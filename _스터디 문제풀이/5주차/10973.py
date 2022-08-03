# 이전 순열

n = int(input())
n_list = list(map(int,input().split()))
temp = -1

for i in range(n):
    if n_list[i-1] > n_list[i]:
        temp = i-1

if temp == -1: # 오름차순인 경우
    print(temp)
    
else:
    for j in range(temp + 1, n):
        if n_list[j] < n_list[temp]:
            fix = j
    
    # 순서 변경
    n_list[temp], n_list[fix] = n_list[fix], n_list[temp]

    ans = n_list[:temp + 1] + sorted(n_list[temp + 1:], reverse = True)

    for k in ans:
        print(k, end = " ")