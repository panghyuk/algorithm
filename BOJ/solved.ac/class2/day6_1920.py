# 수 찾기
# 이분 탐색
import sys
n = int(input())
n_list = sorted(map(int,sys.stdin.readline().split()))

m = int(input())
m_list = map(int,sys.stdin.readline().split())

def binary(l,n_list,start,end):
    if start > end:
        return 0
    mid = (start+end) // 2 
    if l == n_list[mid]: # 동일한 값이면 1 반환
        return 1
    elif l < n_list[mid]: # 값이 크면? 중간보다 윗 부분에서 탐색
        return binary(l,n_list,start,mid-1)
    else: # 값이 작으면? 중간보다 작은 부분에서 탐색
        return binary(l,n_list,mid+1,end)

for l in m_list:
    start = 0
    end = len(n_list) - 1
    print(binary(l,n_list,start,end))

# # 내가 푼 풀이(시간초과)
# n = int(input())
# result = [0] * n
# n_list = []

# n_list = list(map(int,input().split()))

# m = int(input())
# m_list = []

# m_list = list(map(int,input().split()))

# for k in range(len(m_list)):
#     if m_list[k] in n_list:
#         result[k] = 1
#     else:
#         result[k] = 0

# for i in result:
#     print(i)
