# 숫자 카드 2
# 이분탐색/ 해시

# sol.1
n = int(input())
arr1 = list(map(int,input().split()))
dict1 = {}
for i in arr1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:
    if i in dict1:
        print(dict1[i], end = " ")
    else:
        print(0,end = " ")


# # 내 풀이(시간 초과)
# import sys

# n = int(sys.stdin.readline())
# n_list = list(map(int,sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# m_list = list(map(int,sys.stdin.readline().split()))

# result = [0 for _ in range(m)]

# for i in range(m):
#     for j in range(n):
#         if m_list[i] == n_list[j]:
#             result[i] += 1

# for k in result:
#     print(k,end=' ')