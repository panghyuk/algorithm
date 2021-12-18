# 설탕 배달
# DP, Greedy

n = int(input())
cnt = 0

while n >= 0:
    if n % 5 == 0: # 5로 나누어 떨어지면 cnt에 5로 나눈 몫 더하기
        cnt += (n//5)
        print(cnt)
        break
    # 5로 나누어 떨어지지 않으면 전체 양(n)에서 - 3 & cnt에 + 1
    n -= 3
    cnt += 1

else:
    print(-1)