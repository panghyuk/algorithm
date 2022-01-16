# 11399

# 내 풀이
n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
result = []
ans = 0

for i in n_list:
    ans += i
    result.append(ans)

print(sum(result))


# 다른 사람 풀이
n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
ans = 0

for i in range(1,n+1):
    ans += sum(n_list[:i])

print(ans)