# 1920

import sys

input = sys.stdin.readline
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

n_list.sort()

def binary(arr,target,start,end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary(arr,target,start,mid-1)
    elif arr[mid] < target:
        return binary(arr,target,mid+1,end)

for i in m_list:
    start = 0
    end = len(n_list)-1
    print(binary(n_list,i,start,end))