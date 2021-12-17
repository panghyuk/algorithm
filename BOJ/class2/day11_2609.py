# 최대공약수와 최소공배수

# math 모듈 사용
import math

n,m = map(int,input().split())

print(math.gcd(n,m))
print(math.lcm(n,m))

# 유클리드 호제법
n,m = map(int,input().split())

def gcd(x,y):
    while y > 0:
        x,y = y, x % y
    return x

def lcm(x,y):
    return x * y // gcd(x,y)

print(gcd(n,m))
print(lcm(n,m))

# # 내 풀이(시간 초과)
# n,m = map(int,input().split())

# for i in range(min(m,n),0,-1):
#     if m % i ==0 and n % i == 0:
#         print(i)
#         break

# for j in range(max(m,n),(m*n)+1):
#     if j % m == 0 and j % n == 0:
#         print(j)
#         break