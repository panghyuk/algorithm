# 1254

s = input()
reversed_s = s[::-1]
n = len(s)

for i in range(n):
    if s[i:] == reversed_s[0:n-i]:
        print(n+i)
        break