# Hashing
# 해시

l = int(input())
l_str = input()

ans = 0
for i in range(l):
    ans += (ord(l_str[i]) - 96) * (31 ** i)

print(ans % 1234567891)