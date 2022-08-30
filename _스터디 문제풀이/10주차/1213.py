# 팰린드롬 만들기

name = list(input())
name.sort() # 알파벳 순으로 정렬
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
    if v % 2 == 1: # 개수가 홀수일 때
        cnt += 1
        center += k # 중간에 위치하는 문자열 추가
    palindrome += k * (v//2) 

if cnt > 1: # 중간에 위치하는 문자 개수가 1보다 클 때 팰린드롬 만족 X
    print("I'm Sorry Hansoo")
else:
    print(palindrome + center + palindrome[::-1]) # 팰린드롬 뒤집어서 추가
