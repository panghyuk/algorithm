n, k = map(int,input().split())
coin_list = []

for i in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse = True)
count = 0

for j in range(n):
    count += k//coin_list[j]
    k = k % coin_list[j]

print(count)
