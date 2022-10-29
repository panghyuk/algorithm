# 2002

n = int(input())
s = {}
e = []

for i in range(n):
    s[input()] = i

for j in range(n):
    e.append(input())

ans = 0

for k in range(n-1):
    for l in range(k+1, n):
        if s[e[k]] > s[e[l]]:
            ans += 1
            break

print(ans)