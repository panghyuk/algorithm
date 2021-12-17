# 부녀회장이 될테야

test = int(input())

for i in range(test):
    k= int(input())
    n= int(input())

    apart = [i for i in range(1,n+1)]

    for i in range(k):
        for j in range(1,n):
            apart[j] += apart[j-1]
    print(apart[-1])