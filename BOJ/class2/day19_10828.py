# 스택

import sys

n = int(input())
stack = []
input = sys.stdin.readline

for i in range(n):
    word = input().split()

    if word[0] == 'push':
        stack.append(int(word[1]))
    elif word[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif word[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()