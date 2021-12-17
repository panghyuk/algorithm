# 소수 찾기
# 에라토네스의 체
import math

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1): # 제곱근까지만 찾아보기
            if x % i == 0:
                return False
        return True

n = int(input())
cnt = 0
n_list = list(map(int,input().split()))

for j in n_list:
    if prime(j):
        cnt += 1
print(cnt)