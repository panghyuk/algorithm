# 2531

import sys
input = sys.stdin.readline

# n: 회전 초밥 벨트에 놓인 접시의 수
# d: 초밥의 가짓수
# k: 연속해서 먹는 접시의 수
# c: 쿠폰 번호
n,d,k,c = map(int,input().split())
arr = [int(input()) for _ in range(n)]
left= 0
ans = 0