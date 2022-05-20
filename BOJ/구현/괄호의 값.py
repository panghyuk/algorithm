# 2504

sym = list(input())
stack = []
ans = 0
tmp = 1

for i in range(len(sym)):
    if sym[i] == '(':
        stack.append('(')
        tmp *= 2

    elif sym[i] == '[':
        stack.append('[')
        tmp *= 3

    elif sym[i] == ')':
        if not stack or stack[-1] == '[': # stack의 가장 상위 값이 '['일 때 0
            ans = 0
            break

        if sym[i-1] == '(': # 리스트에서 이전 값이 '('일 때
            ans += tmp # tmp 값 추가
        stack.pop()
        tmp //= 2 # 괄호가 닫히기 때문에 2로 나눔

    else:
        if not stack or stack[-1] == '(':  # stack에 가장 위에 값이 '('일 때 0
            ans = 0
            break
        
        if sym[i-1] == '[': # 리스트에서 이전 값이 '['일 때
            ans += tmp # tmp 값 추가
        stack.pop()
        tmp //= 3 # 괄호가 닫히기 때문에 2로 나눔

if stack:
    print(0)
else:
    print(ans)