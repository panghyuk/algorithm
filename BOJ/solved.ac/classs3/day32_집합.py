# 11723

import sys
input = sys.stdin.readline

num = int(input())
s = set()

for _ in range(num):
    res = input().split()

    if len(res) == 1:
        if res[0] == 'all':
            s = set(i for i in range(1,21))
        else:
            s = set()

    else:
        x,n = res[0], int(res[1])

        if x == 'add':
            s.add(n)
        elif x == 'remove':
            s.discard(n)
        elif x == 'check':
            if n in s:
                print(1)
            else:
                print(0)
        elif x == 'toggle':
            if n in s:
                s.discard(n)
            else:
                s.add(n)