# 11047

n, k = map(int,input().split())
coin_list = []

for i in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse = True)
cnt = 0

for coin in coin_list:
    cnt += k//coin # 몫
    k = k % coin # 나머지

print(cnt)
