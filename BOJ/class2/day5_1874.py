# 스택 수열
# 자료구조, 스택

n = int(input())
stack = []
result = []
cnt = 1
answer = True

for i in range(n):
    num = int(input())

    while cnt <= num: # 입력한 수까지 오름차순으로 push
        stack.append(cnt)
        result.append('+')
        cnt += 1
    
    if stack[-1] == num: # stack의 맨 위가 num일 때
        stack.pop() # stack에서 꺼내고(pop)
        result.append('-') # result에 '-' 값 추가
    else:
        answer = False

if answer == False: # 스택 수열이 완성되지 않을 경우
    print('NO')
else:
    for sign in result:
        print(sign)