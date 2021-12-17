# 분해합
# 브루트포스 알고리즘

n = int(input())
for i in range(1,n+1):
    gen = sum(map(int,str(i)))
    result = i + gen

    if result == n:
        print(i)
        break
else:
    print(0)