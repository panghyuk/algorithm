# 책 풀이 1
n,k = map(int,input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# 책 풀이 2 (시간 복잡도 완전 우수)
n,k = map(int,input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)

# 내 풀이
n,k = map(int,input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)