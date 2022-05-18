# 4948
import sys,math
input = sys.stdin.readline

def prime(x):
    if x == 1:
        return False
    
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

all_list = list(range(2,246913))
prime_num = []

for j in all_list:
    if prime(j):
        prime_num.append(j)

while True:
    n = int(input())
    cnt = 0

    if n == 0:
        break

    for i in prime_num: # 시간초과 해결!
        if n < i <= 2 * n:
            cnt += 1
    
    print(cnt)