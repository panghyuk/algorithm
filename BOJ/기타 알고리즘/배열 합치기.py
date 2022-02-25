# 11728

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))
res = []

a = 0
b = 0

# merge sort 알고리즘
while a != n or b != m:
    if a == n:
        res.append(arrB[b])
        b += 1
    elif b == m:
        res.append(arrA[a])
        a += 1
    else:
        if arrA[a] < arrB[b]:
            res.append(arrA[a])
            a += 1
        else:
            res.append(arrB[b])
            b += 1

for i in res:
    print(i, end = ' ')


''' 정렬 '''
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# arrA = list(map(int,input().split()))
# arrB = list(map(int,input().split()))
# res = arrA + arrB
# res.sort()

# for i in res:
#     print(i,end = ' ')