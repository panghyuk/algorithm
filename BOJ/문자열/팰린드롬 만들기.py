# 1213

name = list(input())
name.sort()
word = {}

for i in name:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

cnt = 0
center = ''
palindrome = ''

for k,v in word.items():
    if v % 2 == 1:
        cnt += 1
        center += k
    
    palindrome += k * (v//2)

if cnt > 1:
    print("I'm Sorry Hansoo")

else:
    print(palindrome + center + palindrome[::-1])
