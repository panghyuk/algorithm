# 소수 구하기
# 수학, 에라토네스의 체
import math

def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1): # 제곱근까지만 찾아보기
            if x % i == 0:
                return False
        return True

m,n = map(int,input().split())
for j in range(m,n+1):
    if prime(j):
        print(j)

# # 시간초과...
# m,n = map(int,input().split())

# def prime_over(x):
#     if x < 2:
#         return False
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#     return True

# for j in range(m,n+1):
#     if prime_over(j):
#         print(j)