# 덱
import sys

n = int(input())
deque = []
input = sys.stdin.readline

for i in range(n):
    word = input().split()

    if word[0] == 'push_back':
        deque.append(word[1])
    elif word[0] == 'push_front':
        deque.insert(0,word[1])
    elif word[0] == 'back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])
    elif word[0] == 'front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif word[0] == 'pop_front':
        if not deque:
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif word[0] == 'pop_back':
        if not deque:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif word[0] == 'size':
        print(len(deque))
    else:
        if not deque:
            print(1)
        else:
            print(0)
