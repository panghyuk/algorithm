# 4948
import sys
input = sys.stdin.readline

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(x**(1/2)) + 1):
            if x % i == 0:
                return False
        return True

all_list = [range(2,246913)]
prime_num = []

for i in all_list:
    if prime(i):
        prime_num.append(i)

while True:
    cnt = 0
    n = int(input())

    if n == 0:
        break
    else:
        for i in range(n, 2*n + 1):
            if i in prime_num:
                cnt += 1
        
        print(cnt)