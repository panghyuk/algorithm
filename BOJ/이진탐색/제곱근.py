# 13706

n = int(input())
s = 1
e = n

while True:
    mid = (s + e) // 2

    if mid ** 2 == n:
        print(mid)
        break 

    elif mid ** 2 > n:
        e = mid - 1

    elif mid ** 2 < n:
        s = mid + 1


''' 복습 풀이 '''
# n = int(input())

# start = 0
# end = n

# while start <= end :
#     mid = (start + end) // 2

#     if mid ** 2 == n:
#         print(mid)
#         break
    
#     elif mid ** 2 > n:
#         end = mid - 1
    
#     else:
#         start = mid + 1