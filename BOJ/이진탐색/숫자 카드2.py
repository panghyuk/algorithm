# 10816

import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort() # 오름차순 정렬(이분 탐색 기본 세팅)

m = int(input())
m_list = list(map(int,input().split()))

cnt = {}

for x in n_list:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

print(cnt)

def binary(arr,target,start,end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target:
        return cnt[target]
    
    elif arr[mid] > target:
        return binary(arr,target,start,mid-1)

    else:
        return binary(arr,target,mid+1,end)

for i in m_list:
    print(binary(n_list,i,0,len(n_list)-1),end = ' ')


''' Counter 사용 '''
# import sys
# from collections import Counter

# input = sys.stdin.readline
# n = int(input())
# n_list = list(map(int,input().split()))

# m = int(input())
# m_list = list(map(int,input().split()))

# cnt = Counter(n_list)

# for i in m_list:
#     print(cnt[i],end = ' ')