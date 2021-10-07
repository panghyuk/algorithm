# 팰린드롬수
# 구현/문자열

while True:
    n = str(input())
    rev_n = n[::-1]
    if n == '0':
        break
    if n == rev_n:
        print("yes")
    else:
        print('no')
    