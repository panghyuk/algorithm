# 9251 최장 공통 부분 수열

str1 = input()
str2 = input()

lcs = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1,len(str1) + 1):
    for j in range(1,len(str2) + 1):
        if str1[i-1] == str2[j-1]: # 같으면 lcs + 1
            lcs[i][j] = lcs[i-1][j-1] + 1
        else: # 다르면 인접한 것 중 큰 것 선택
            lcs[i][j] = max(lcs[i][j-1],lcs[i-1][j])

print(lcs[-1][-1])