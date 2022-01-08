# ACM 호텔

test = int(input())

for i in range(test):
    h,w,n =map(int,input().split())
    floor = n % h
    room = n//h + 1

    if floor == 0:
        room -= 1
        floor = h
    
    print(floor*100 + room)

# 내 풀이
test = int(input())

for i in range(test):
    h,w,n = map(int,input().split())
    
    c_cnt = 1
    while h < n:
        n -= h
        c_cnt += 1

    if n == 0: # n이 h의 배수일 때 처리
        c_cnt -= 1
        n = h

    result = n * 100 + c_cnt
    print(result)
