# 10816

import sys

input = sys.stdin.readline
n = int(input())
n_list = list(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

def binary(arr,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary(arr,target,start,mid-1)
    else:
        return binary(arr,target,mid+1,end)


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