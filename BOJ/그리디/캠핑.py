# 4796

import sys
input = sys.stdin.readline
cnt = 1

while True:
    l,p,v = map(int,input().split())

    if p == l == v == 0:
        break

    day = (v // p) * l
    day += min((v % p),l)

    print('Case '+ str(cnt) + ': ' + str(day))
    cnt += 1