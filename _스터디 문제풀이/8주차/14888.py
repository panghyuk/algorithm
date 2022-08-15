# 연산자 끼워넣기

from itertools import permutations

n = int(input())
n_list = list(map(int,input().split()))
opr_num = list(map(int,input().split()))
opr_list = ['+', '-', '*', '/']
opr = []

for i in range(4):
    for j in range(opr_num[i]):
        opr.append(opr_list[i])

maxnum = 0
minnum = 101
permu = permutations(opr,n-1)

for k in permu:
    ans = n_list[0]
    for l in range(1,n):
        if k[l-1] == '+':
            ans += n_list[l]

        elif k[l-1] == '-':
            ans -= n_list[l]

        elif k[l-1] == '*':
            ans *= n_list[l]

        elif k[l-1] == '/':
            ans = int(ans / n_list[l])
    
    if ans > maxnum:
        maxnum = ans
    if ans < minnum:
        minnum = ans

print(maxnum)
print(minnum)