# 균형잡힌 세상
# 문자열/스택(LIFO)

import sys

while True:
    str_ = sys.stdin.readline().rstrip()
    stack = []
    ans = 0

    if str_ == '.':
        break

    for i in str_:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[': # 열린 괄호가 없거나 열린 대괄호가 나올 때
                print('no')
                ans = 1
                break
            else:
                stack.pop()

        elif i == ']':
            if not stack or stack[-1] == '(': # 열린 괄호가 없거나 열린 소괄호가 나올 때
                print('no')
                ans = 1
                break
            else:
                stack.pop()

    if ans == 0:
        if not stack: # 모든 괄호가 짝을 맞췄을 때
            print('yes')
        else:
            print('no')