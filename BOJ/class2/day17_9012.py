# 괄호
# 문자열/스택(LIFO)

for i in range(int(input())):
    str_ = input()
    stack = []
    ans = 0

    for i in str_:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack: # 스택 안에 괄호가 없을 때
                print('NO')
                ans = 1
                break
            else:
                stack.pop()
    if ans == 0:
        if not stack: # 모든 괄호가 짝을 맞췄을 때
            print('YES')
        else:
            print('NO')