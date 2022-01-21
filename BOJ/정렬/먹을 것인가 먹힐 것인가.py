# 7795
# 이분 탐색 활용

import sys, bisect

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    list_a = list(map(int,input().split()))
    list_b = list(map(int,input().split()))

    list_a.sort()
    list_b.sort()
    cnt = 0

    for i in list_a:
        cnt += bisect.bisect_left(list_b, i) # 값이 동일할 경우 인덱스가 해당 값 좌측으로

    print(cnt)
