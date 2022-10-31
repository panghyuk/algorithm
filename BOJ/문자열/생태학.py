# 4358

import sys

input = sys.stdin.readline
ecology = {}
i = 0

while True:
    tree = input().rstrip()

    if not tree:
        break

    if tree in ecology:
        ecology[tree] += 1
        i += 1
    else:
        ecology[tree] = 1
        i += 1
    
eco = sorted(ecology.items(), key = lambda x:x[0])

for k,v in eco:
    print("{} {:.4f}".format(k,v/i * 100))
