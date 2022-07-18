# 9375

t = int(input())

for _ in range(t):
    n = int(input())
    fashion = {}

    for i in range(n):
        a,b = input().split()
        if b in fashion.keys():
            fashion[b] += 1
        else:
            fashion[b] = 1
    cnt = 1

    for k in fashion.keys():
        cnt *= (fashion[k] + 1)
    
    print(cnt-1)
