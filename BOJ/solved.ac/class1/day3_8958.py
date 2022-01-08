# OX 퀴즈
# 구현, 문자열
n = int(input())

for i in range(n):
    quiz = input()
    cnt_list = []
    cnt = 0
    for j in quiz:
        if j == "O":
            cnt +=1
            cnt_list.append(cnt)
        else:
            cnt = 0
    print(sum(cnt_list))