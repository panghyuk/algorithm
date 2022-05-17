import math

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

n = int(input())
num = list(map(int,input().split()))
cnt = 0

for j in num:
    if prime(j):
        cnt += 1

print(cnt)