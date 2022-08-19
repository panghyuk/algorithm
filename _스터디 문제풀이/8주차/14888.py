# 연산자 끼워넣기

from itertools import permutations
import sys

input = sys.stdin.readline
n = int(input())
n_list = list(map(int,input().split()))
opr_num = list(map(int,input().split()))
opr_list = ['+', '-', '*', '/']
opr = []

for i in range(4):
    for j in range(opr_num[i]):
        opr.append(opr_list[i])

maxnum = -1e9
minnum = 1e9
permus = permutations(opr, n-1) # 연산자 순서 조합

for permu in permus:
    ans = n_list[0] # n_list의 첫번째 숫자 할당
    for l in range(1,n):
        if permu[l-1] == '+':
            ans += n_list[l]

        elif permu[l-1] == '-':
            ans -= n_list[l]

        elif permu[l-1] == '*':
            ans *= n_list[l]

        elif permu[l-1] == '/':
            ans /= n_list[l]
            ans = int(ans)
    
    maxnum = max(ans,maxnum)
    minnum = min(ans,minnum)

print(maxnum)
print(minnum)