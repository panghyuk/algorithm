# 9375

t = int(input())

for _ in range(t):
    n = int(input())
    cloth = dict()

    for _ in range(n):
        a,b = input().split()
        if b in cloth.keys():
            cloth[b] += 1
        else:
            cloth[b] = 1 
        
    ans = 1

    for k in cloth.keys():
        ans *= (cloth[k] + 1)

    print(ans - 1)
    
