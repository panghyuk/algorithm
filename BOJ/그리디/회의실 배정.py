# 1931

import sys

n = int(input())
input = sys.stdin.readline

meets = []
for i in range(n):
    meets.append(list(map(int,input().split())))

meets.sort(key = lambda x:(x[1],x[0]))
cnt = 0
end = 0

for meet in meets:
    if end <= meet[0]: # 현재 회의가 끝나는 시간이 다음 회의 시작 시간보다 작을 때 
        end = meet[1] # 회의 끝나는 시간을 다음 회의 끝나는 시간으로 변경
        cnt += 1

print(cnt)