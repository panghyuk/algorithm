# 큐

import sys

n = int(input())
input = sys.stdin.readline
que = []

for i in range(n):
    word = input().split()

    if word[0] == 'push':
        que.append(word[1])
    elif word[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif word[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])
    elif word[0] == 'size':
        print(len(que))
    elif word[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que[0])
            que.pop(0)
    else:
        if not que:
            print(1)
        else:
            print(0)