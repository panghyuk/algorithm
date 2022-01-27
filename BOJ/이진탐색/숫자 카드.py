# 10815

import sys

input = sys.stdin.readline
n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

def binary(arr,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return 1
        
        elif arr[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return 0

for x in m_list:
    print(binary(n_list,x,0,len(n_list)-1),end = " ")