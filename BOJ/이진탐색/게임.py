# 1072

x,y = map(int,input().split())

z = y * 100 // x

if z >= 99: # 예외 처리
    print(-1)

else:
    ans = 0
    start = 1
    end = x

    while start <= end:
        mid = (start + end) // 2
        
        if (y + mid) * 100 // (x + mid) > z:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    
    print(ans)