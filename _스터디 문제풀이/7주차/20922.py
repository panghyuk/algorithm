# 겹치는 건 싫어

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
n_list = list(map(int,input().split()))
n_max = max(n_list) # n_list 중 가장 큰 수 뽑기
n_dict = {}
for i in range(n_max):
    n_dict[i + 1] = 0

s,e = 0, 0 # 시작과 끝 포인트 선언
ans = 0

while e < n:
    if n_dict[n_list[e]] < k:
        n_dict[n_list[e]] += 1
        e += 1

    else: # k개 이상일 때
        n_dict[n_list[s]] -= 1 # 이거 때문에 계속 틀림..
        s += 1

    ans = max(ans, e - s)

print(ans)