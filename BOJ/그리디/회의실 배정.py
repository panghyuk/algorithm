# 1931
import sys

n = int(input())
input = sys.stdin.readline

meets = []
for i in range(n):
    meets.append(list(map(int,input().split())))

meets.sort(key = lambda x:(x[1],x[0]))
cnt = 0
end = -1

for meet in meets:
    if end <= meet[0]:
        end = meet[1]
        cnt += 1

print(cnt)