# 14425
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
name = set()
cnt = 0

for _ in range(n):
    name.add(input())

for _ in range(m):
    check = input()

    if check in name:
            cnt += 1
            
print(cnt)