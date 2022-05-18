# 1946
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    res = []


    for i in range(n):
        res.append(list(map(int,input().split())))
    
    res.sort()
    cnt = 1 # 첫번째 사람은 무조건 채용
    rank = res[0][1] # 첫번째 사람 면접 순위

    for i in range(1,n):
        if rank > res[i][1]: # 면접 순위가 더 낮으면
            cnt += 1
            rank = res[i][1] # 기존 순위를 변경
    
    print(cnt)
