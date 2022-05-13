# 2559

n, k = map(int, input().split())
arr = list(map(int, input().split()))
tmp = sum(arr[:k])
result = tmp

for i in range(k, n):
    tmp += arr[i] - arr[i-k]
    result = max(result, tmp)

print(result)
