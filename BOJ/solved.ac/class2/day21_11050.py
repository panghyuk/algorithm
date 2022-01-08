# 이항 계수 1

n,k = map(int,input().split())

def facto(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

ans = int(facto(n)/(facto(k)*facto(n-k)))
print(ans)