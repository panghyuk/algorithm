# 1449

n,l = map(int,input().split())
water = list(map(int,input().split()))
water.sort()

cnt = 1
start = water[0]
end = water[0] + l - 0.5

for i in range(1,n):
    if water[i] < end:
        continue
    cnt += 1
    end = water[i] + l - 0.5

print(cnt)


# 다른 풀이
n,l = map(int,input().split())
water = list(map(int,input().split()))
water.sort()

start = water[0]
end = water[0] + l - 0.5
cnt = 1

for i in range(1,n):
	if end < water[i]:
		cnt += 1
		end = water[i] + l - 0.5
print(cnt)