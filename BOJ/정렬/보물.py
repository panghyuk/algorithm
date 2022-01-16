# 1026

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
a.sort()

for i in range(n):
    max_b = b.pop(b.index(max(b)))
    ans += max_b * a[i]

print(ans)


# a,b 둘 다 정렬한 풀이
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse = True)
b.sort()

ans = 0

for i in range(n):
    ans += a[i]*b[i]

print(ans)