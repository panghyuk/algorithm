for tc in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))

    dp = []
    idx = 0

    for _ in range(n):
        dp.append(arr[idx:idx + m])
        idx += m
    
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            # DP 점화식
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    
    res = 0

    for i in range(n):
        res = max(res,dp[i][m-1])
    
    print(res)