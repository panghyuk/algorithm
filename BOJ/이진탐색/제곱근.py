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