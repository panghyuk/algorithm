# 11497

t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int,input().split()))
    n_list.sort(reverse = True)
    ans = 0

    for j in range(n-2):
        ans = max(n_list[j] - n_list[j+2],ans)

    print(ans)