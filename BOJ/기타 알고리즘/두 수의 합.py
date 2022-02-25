# 3273

''' 투 포인터 풀이'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
x = int(input())

ans = 0
s, e = 0, n-1

while s < e:
    if arr[s] + arr[e] == x:
        ans += 1
        s += 1

    elif arr[s] + arr[e] < x:
        s += 1

    else:
        e -= 1
print(ans)


''' 이분 탐색 풀이'''
# import sys
# input = sys.stdin.readline

# def binary(start,end,target):
#     while start <= end:
#         mid = (start + end) // 2    
#         if arr[mid] == target:
#             return True
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# n = int(input())
# arr = list(map(int,input().split()))
# arr.sort()
# x = int(input())

# start = 0
# end = n -1
# cnt = 0

# for i in arr:
#     if binary(start,end,x-i):
#         cnt += 1
# print(cnt//2)