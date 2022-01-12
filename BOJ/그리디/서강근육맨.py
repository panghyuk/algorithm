# 20300

import sys

input = sys.stdin.readline
n = int(input())
muscle = list(map(int,input().split()))
muscle.sort() # 오름차순 정렬
m = 0

if len(muscle) % 2 == 0: # 개수가 짝수일 때
    for i in range(n//2):
        m = max(m,muscle[i]+muscle[n-i-1])
else: # 개수가 홀수 일 때
    for j in range(n//2):
        m = max(m,muscle[j]+muscle[n-j-2])
    m = max(m,muscle[-1]) # 맨 마지막이랑 비교

print(m)