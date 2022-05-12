# 9375
''' sol.1 '''
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
    

''' sol.2 '''

from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1 # 각 종류마다 항목의 개수

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)