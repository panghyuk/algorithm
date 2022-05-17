# 1929

n,m = map(int,input().split())
num = [i for i in range(n,m+1)]

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(x ** (1/2)) + 1):
            if x % i == 0:
                return False
        return True

for j in num:
    if prime(j):
        print(j)