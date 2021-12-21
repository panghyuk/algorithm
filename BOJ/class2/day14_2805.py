# 나무 자르기
# 이분 탐색
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 0
end = max(tree)

# 이분탐색 알고리즘
while start <= end:
    mid = (start+end)//2
    cnt = 0 # 잘린 나무의 총합

    for i in tree:
        if mid < i: # mid보다 크면 나무 자름
            cnt += (i - mid)

    if cnt < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)