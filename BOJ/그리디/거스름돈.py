# 5585

n = int(input())

change = 1000 - n
cnt = 0
coin_list = [500,100,50,10,5,1]

for coin in coin_list:
    cnt += change//coin # 몫
    change %= coin # 나머지

print(cnt)